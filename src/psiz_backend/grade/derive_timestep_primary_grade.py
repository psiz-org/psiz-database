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

import grade


def derive_timestep_primary_grade(
        design_factors, timestep, results_interaction):
    """Derive primary grade for timestep.
    
    Args:
        design_factors:
        timestep:
        results_interactions:

    Returns:
        grade_primary

    """
    is_primary_eligible = grade.check_timestep_primary_eligibility(
        design_factors, timestep, results_interaction
    )
    if is_primary_eligible:
        if 'rank:' in timestep['kind']:
            grade_primary = grade.grade_rank_similarity(
                design_factors, timestep, results_interaction
            )
        elif 'categorize:' in timestep['kind']:
            grade_primary = grade.grade_categorize(
                design_factors, timestep, results_interaction
            )
        # elif 'rate:' in timestep['kind']:
        #     grade_primary = grade_rate(
        #         design_factors, timestep, results_interaction
        #     )
    else:
        # Not eligible for primary grading process.
        grade_primary = -1

    return grade_primary