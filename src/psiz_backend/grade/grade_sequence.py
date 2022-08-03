# -*- coding: utf-8 -*-
# Copyright 2022 The PsiZ Backend Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
""""""

from datetime import time
import numpy as np

import db_psiz03
import grade
from sql.create_connection import create_connection


def grade_sequence(new_db_name, sequence_id, design_id):
    """Grade sequence.
    
    Route to grading strategy based on design factors and timestep kind.

    """
    # Open another MySQL connection to new database.
    cxn_psiz03 = create_connection(new_db_name)
    cursor_psiz03 = cxn_psiz03.cursor()

    # Grab design factor information for sequence.
    design_factors = db_psiz03.select_design_factors(cursor_psiz03, design_id)
    
    # Select timesteps associated with sequence.
    query = (
        "SELECT id, position, kind, time_begin, time_end, "
        "response_time_ms FROM timestep WHERE sequence_id=%s"
    )
    vals = (sequence_id,)
    cursor_psiz03.execute(query, vals)
    result_timestep = cursor_psiz03.fetchall()

    is_eligibile = grade.check_sequence_eligibility(
        design_factors, result_timestep
    )
    
    if is_eligibile:
        sequence_grade_data = {
            'earnest': [],
            'primary': [],
        }

        for timestep_row in result_timestep:
            timestep = {
                'id': timestep_row[0],
                'position': timestep_row[1],
                'kind': timestep_row[2],
                'time_begin': timestep_row[3],
                'time_end': timestep_row[4],
                'response_time_ms': timestep_row[5],
            }
            query = (
                "SELECT kind, time_begin, info FROM interaction "
                "WHERE timestep_id=%s"
            )
            vals = (timestep['id'],)
            cursor_psiz03.execute(query, vals)
            results_interaction = cursor_psiz03.fetchall()

            grade_data = grade.grade_timestep(
                cxn_psiz03, cursor_psiz03, design_factors, timestep,
                results_interaction
            )
            sequence_grade_data['earnest'].append(grade_data['earnest'])
            sequence_grade_data['primary'].append(grade_data['primary'])

        # Convert timestep grades to overall sequence grade.
        sequence_grade = distill_to_sequence_grade(
            sequence_id, design_factors, sequence_grade_data
        )
    else:
        sequence_grade = 0

    # Close connection
    cursor_psiz03.close()
    cxn_psiz03.close()

    return sequence_grade


def distill_to_sequence_grade(sequence_id, design_factors, sequence_grade_data):
    """Convert timesteps grade to overall sequence grade."""
    # Make sure NumPy arrays.
    sequence_grade_data['earnest'] = np.array(sequence_grade_data['earnest'])
    sequence_grade_data['primary'] = np.array(sequence_grade_data['primary'])

    bidx = np.not_equal(sequence_grade_data['primary'], -1)
    primary_grades = sequence_grade_data['primary'][bidx]

    if len(primary_grades) > 0:
        primary_grade = np.mean(primary_grades)
        msg = ''
    else:
        # Aggressive drop criteria.
        primary_grade = 0
        msg = '(no primary grade)'

    # Screen any sequences that do not meet earnest criteria.
    bidx = np.not_equal(sequence_grade_data['earnest'], -1)
    earnest_grades = sequence_grade_data['earnest'][bidx]
    if np.sum(np.less(earnest_grades, 100)) > 0:
        earnest_grade = 0
    else:
        earnest_grade = 100

    if earnest_grade < 100:
        sequence_grade = 0
    else:
        sequence_grade = primary_grade

    sequence_grade = int(np.round(sequence_grade))

    print(
        'sequence_id:{0} | {1} | {2} | grade {3} {4}'.format(
            sequence_id,
            design_factors['project'],
            design_factors['protocol'],
            sequence_grade,
            msg
        )
    )
    return sequence_grade