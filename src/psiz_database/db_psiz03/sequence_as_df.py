# -*- coding: utf-8 -*-
# Copyright 2022 The PsiZ Database Authors. All Rights Reserved.
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


import pandas as pd


def sequence_as_df(sql_result):
    """Format SQL result as DataFrame.
    
    Args:
        sql_result: Appropriately formatted sql_result.

    Returns:
        DataFrame

    """
    id = []
    anonymous_id = []
    design_id = []
    time_begin = []
    time_end = []
    n_timestep = []
    grade = []
    is_exported = []

    n_row = len(sql_result)
    for i_row in range(n_row):
        id.append(sql_result[i_row][0])
        anonymous_id.append(sql_result[i_row][1])
        design_id.append(sql_result[i_row][2])
        time_begin.append(sql_result[i_row][3])
        time_end.append(sql_result[i_row][4])
        n_timestep.append(sql_result[i_row][5])
        grade.append(sql_result[i_row][6])
        is_exported.append(sql_result[i_row][7])

    d = {
        'id': id,
        'anonymous_id': anonymous_id,
        'design_id': design_id,
        'time_begin': time_begin,
        'time_end': time_end,
        'n_timestep': n_timestep,
        'grade': grade,
        'is_exported': is_exported,
    }

    df = pd.DataFrame(d)
    return df
