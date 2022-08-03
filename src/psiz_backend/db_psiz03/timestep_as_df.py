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

import pandas as pd


def timestep_as_df(sql_result):
    """Format SQL result as DataFrame.
    
    Args:
        sql_result: Appropriately formatted sql_result.

    Returns:
        DataFrame

    """
    id = []
    sequence_id = []
    position = []
    kind = []
    time_begin = []
    time_end = []
    response_time_ms = []

    n_row = len(sql_result)
    for i_row in range(n_row):
        id.append(sql_result[i_row][0])
        sequence_id.append(sql_result[i_row][1])
        position.append(sql_result[i_row][2])
        kind.append(sql_result[i_row][3])
        time_begin.append(sql_result[i_row][4])
        time_end.append(sql_result[i_row][5])
        response_time_ms.append(sql_result[i_row][6])

    d = {
        'id': id,
        'sequence_id': sequence_id,
        'position': position,
        'kind': kind,
        'time_begin': time_begin,
        'time_end': time_end,
        'response_time_ms': response_time_ms,
    }

    df = pd.DataFrame(d)
    return df
