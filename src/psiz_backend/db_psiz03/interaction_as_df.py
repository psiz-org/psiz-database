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


def interaction_as_df(sql_result):
    """Format SQL result as DataFrame.
    
    Args:
        sql_result: Appropriately formatted sql_result.

    Returns:
        DataFrame

    """
    id = []
    timestep_id = []
    time_begin = []
    kind = []
    info = []

    n_row = len(sql_result)
    for i_row in range(n_row):
        id.append(sql_result[i_row][0])
        timestep_id.append(sql_result[i_row][1])
        time_begin.append(sql_result[i_row][2])
        kind.append(sql_result[i_row][3])
        info.append(sql_result[i_row][4])

    d = {
        'id': id,
        'timestep_id': timestep_id,
        'time_begin': time_begin,
        'kind': kind,
        'info': info,
    }

    df = pd.DataFrame(d)
    return df
