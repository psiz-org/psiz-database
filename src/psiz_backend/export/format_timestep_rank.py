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


def format_timestep_rank(
        agent_id, row_sequence, row_timestep, df_interaction):
    """Format a ranked similarity timestep."""
    # n_select = None  # TODO
    # stimulus_set = None  # TODO

    formatted_interactions = None  # TODO

    formatted_timestep = {
        "position": row_timestep.position,
        "kind": row_timestep.kind,
        "time_begin": row_timestep.time_begin,
        "time_end": row_timestep.time_end,
        "response_time_ms": row_timestep.response_time_ms,
        "interactions": formatted_interactions,
    }
    return formatted_timestep
