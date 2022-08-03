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


def insert_into_designs(cxn_psiz03, cursor_psiz03, design_factors):
    """Add to `design` table.
    
    Args:
        cxn_psiz03:  MySQL connection to `psiz03` database.
        design_factors: List of strings that identify design factors.
    
    """
    # Check if relevant `design_id` is already present.
    query = (
        "SELECT id FROM design WHERE project=%s "
        "AND stimulus_set=%s "
        "AND protocol=%s "
        "AND factor_d=%s "
        "AND factor_e=%s"
    )
    vals = (
        design_factors[0], design_factors[1], design_factors[2],
        design_factors[3], design_factors[4]
    )
    cursor_psiz03.execute(query, vals)
    sql_result = cursor_psiz03.fetchall()

    if len(sql_result) > 0:
        # Design already exists.
        design_id = sql_result[0][0]
    else:
        query = (
            "INSERT INTO design (project, stimulus_set, protocol, factor_d, "
            "factor_e) VALUES (%s, %s, %s, %s, %s)"
        )
        vals = (
            design_factors[0], design_factors[1], design_factors[2],
            design_factors[3], design_factors[4]
        )
        cursor_psiz03.execute(query, vals)
        cxn_psiz03.commit()

        cursor_psiz03.execute("SELECT LAST_INSERT_ID()")
        sql_result = cursor_psiz03.fetchall()
        design_id = sql_result[0][0]

    return design_id
