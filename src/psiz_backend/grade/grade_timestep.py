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

import db_psiz03
import grade


def grade_timestep(
        cxn_psiz03, cursor_psiz03, design_factors, timestep,
        results_interaction):
    """Grade timestep.
    
    Args:
        design_factors:
        timestep:
        results_interaction:

    Returns:
        grade_data

    """
    grade_earnest = grade.derive_timestep_earnest_effort(
        design_factors, timestep, results_interaction
    )
    grade_primary = grade.derive_timestep_primary_grade(
        design_factors, timestep, results_interaction
    )

    # Update timestep table.
    db_psiz03.update_timestep_grade(
        cxn_psiz03, cursor_psiz03, timestep['id'], grade_earnest,
        grade_primary
    )

    return {
        'earnest': grade_earnest,
        'primary': grade_primary,
    }
