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


def insert_into_sequence(
        cxn_psiz03, cursor_psiz03, anonymous_id, design_id, sequence_begin,
        sequence_end):
    """Add to `sequence` table."""
    n_timestep = -1  # Will be updated later.
    grade = -1  # Will be graded later.
    query = (
        "INSERT INTO sequence (anonymous_id, design_id, "
        "time_begin, time_end, n_timestep, grade) VALUES "
        "(%s, %s, %s, %s, %s, %s)"
    )
    vals = (
        str(anonymous_id), design_id, sequence_begin, sequence_end, n_timestep,
        grade
    )
    cursor_psiz03.execute(query, vals)
    cxn_psiz03.commit()

    cursor_psiz03.execute("SELECT LAST_INSERT_ID()")
    sql_result = cursor_psiz03.fetchall()
    sequence_id = sql_result[0][0]

    return sequence_id
