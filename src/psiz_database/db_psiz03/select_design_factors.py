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


def select_design_factors(cursor_psiz03, design_id):
    """Select design factors for requested `design_id`.

    Args:
        cursor_psiz03:
        design_id

    Returns:
        design_factors: A dictionary of design factors.

    """
    query = (
        "SELECT project, stimulus_set, protocol, factor_d, "
        "factor_e FROM design WHERE id=%s"
    )
    vals = (design_id,)
    cursor_psiz03.execute(query, vals)
    results_design = cursor_psiz03.fetchall()
    if len(results_design) > 1:
        print('There should only be one row in select design result.')
    design_factors = {
        'project':  results_design[0][0],
        'stimulus_set':  results_design[0][1],
        'protocol':  results_design[0][2],
        'factor_d':  results_design[0][3],
        'factor_e':  results_design[0][4],
    }
    return design_factors
