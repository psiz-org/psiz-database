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


def derive_timestep_earnest_effort(
        design_factors, timestep, results_interaction):
    """Derive earnest effort grade for timestep.
    
    Args:
        design_factors:
        timestep:
        results_interactions:

    Returns:
        grade_earnest

    """
    grade_rt = grade.grade_response_time(design_factors, timestep)

    grade_earnest = grade_rt

    return grade_earnest
