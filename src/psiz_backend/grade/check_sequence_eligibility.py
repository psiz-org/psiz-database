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


def check_sequence_eligibility(design_factors, result_timestep):
    """Check task-specific eligibility."""
    # Start by assuming eligible.
    is_eligible = True

    # Ineligible if sequences contains zero timesteps.
    if len(result_timestep) == 0:
        return False

    if (
        design_factors['project'] == 'rank:Birds2019' and
        len(result_timestep) < 10
    ):
        # NOTE: Different expected number of trials.
        is_eligible = False
    elif (
        design_factors['project'] == 'rank:ILSVRC2012-val' and
        len(result_timestep) < 10
    ):
        # NOTE: Different expected number of trials depending on protocol, so
        # allow anything greater than 10.
        is_eligible = False
    elif (
        design_factors['project'] == 'rank:RegionalBirds' and
        len(result_timestep) < 10
    ):
        # NOTE: Different expected number of trials depending on protocol, so
        # allow anything greater than five.
        is_eligible = False
    elif (
        design_factors['project'] == 'rank:Rocks2016' and
        len(result_timestep) < 25
    ):
        # Should be 30 trials.
        is_eligible = False
    elif (
        design_factors['project'] == 'rank:SkinLesions2018' and
        len(result_timestep) < 25
    ):
        # Should be 30 trials. One "guest" completed 206 trials.
        is_eligible = False

    if (
        design_factors['project'] == 'categorize:Birds2019:sequencing-0' and
        len(result_timestep) < 300
    ):
        # NOTE: Experiment consists of 320 trials: 224 practice trials
        # (approximately 40 minutes) and 96 assessment trials (approximately 
        # 15 minutes). Including feedback timestep, expect 321 timesteps.
        # Allow for 20 missing trials.
        is_eligible = False

    return is_eligible
