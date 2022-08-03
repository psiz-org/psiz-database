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


def check_timestep_primary_eligibility(
        design_factors, timestep, interactions_data):
    """Check task-specific eligabilty."""
    # Start by assuming all timesteps are eligible.
    is_eligible = True

    if timestep['kind'] == 'questionnaire:birding_experience':
        is_eligible = False
    if timestep['kind'] == 'questionnaire:feedback':
        is_eligible = False
    if design_factors['project'] == 'categorize:Birds2019:sequencing-0':
        # Derive grade from "assessment phase" trials (that do not include
        # feedback) at end of sequence. These trials correspond to timesteps
        # with position >= 224.
        if timestep['kind'] == 'categorize:unconstrained_with-feedback':
            is_eligible = False

    return is_eligible
