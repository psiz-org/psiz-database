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


def update_n_timestep(cxn_psiz03, cursor_psiz03, sequence_id, n_timestep):
    """Update `n_timestep` in `sequence` table."""
    query = (
        "UPDATE sequence SET n_timestep=%s WHERE id=%s"
    )
    vals = (n_timestep, sequence_id)
    cursor_psiz03.execute(query, vals)
    cxn_psiz03.commit()
