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


def update_response_time_stat(
        cxn_psiz03, cursor_psiz03, timestep_variety, stimulus_set_name, new_rt_ms):
    """Update response time statistics."""
    # Check if statistic has been started.
    query = (
        "SELECT id, rt_ms_sum, n_timestep FROM response_time_statistic "
        " WHERE timestep_variety=%s AND stimulus_set=%s"
    )
    vals = (timestep_variety, stimulus_set_name)
    cursor_psiz03.execute(query, vals)
    sql_result = cursor_psiz03.fetchall()

    if len(sql_result) < 1:
        # Statistic does not exist, so create new row.
        query = (
            "INSERT INTO response_time_statistic (timestep_variety, "
            "stimulus_set, rt_ms_sum, n_timestep, rt_ms_avg)"
            " VALUES (%s, %s, %s, 1, %s)"
        )
        vals = (
            timestep_variety, stimulus_set_name, new_rt_ms, new_rt_ms
        )
        cursor_psiz03.execute(query, vals)
        cxn_psiz03.commit()
    else:
        # Statistic exists, update the existing statistic.
        statistic_id = sql_result[0][0]
        old_rt_ms_sum = sql_result[0][1]
        old_n_timestep = sql_result[0][2]
        # Compute new values.
        new_rt_ms_sum = old_rt_ms_sum + new_rt_ms
        new_n_timestep = old_n_timestep + 1
        new_rt_ms_avg = int(new_rt_ms_sum / new_n_timestep)
        # Apply update.
        query = (
            "UPDATE response_time_statistic "
            "SET rt_ms_sum=%s,  n_timestep=%s, rt_ms_avg=%s "
            "WHERE id=%s"
        )
        vals = (new_rt_ms_sum, new_n_timestep, new_rt_ms_avg, statistic_id)
        cursor_psiz03.execute(query, vals)
        cxn_psiz03.commit()
