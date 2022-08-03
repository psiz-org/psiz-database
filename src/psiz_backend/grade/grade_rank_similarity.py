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

import numpy as np

import grade


def grade_rank_similarity(design_factors, timestep, results_interaction):
    """Grade rank similarity trial.
    
    Check for catch trials.

    Args:
        design_factors:
        timestep:
        results_interaction:

    Returns:
        grade_primary:

    """
    query = ""
    reference_list = []
    choice_list = []
    rank_order_list = []
    for interaction in results_interaction:
        interaction_variety = interaction[0]
        # interaction_datetime = interaction[1]
        details = interaction[2]
        if interaction_variety == "stimulus:query":
            query = details
        if "stimulus:reference" in interaction_variety:
            reference_list.append(details)
        if "behavior:rank" in interaction_variety:
            choice_list.append(details)
            rank_order_list.append(
                int(interaction_variety.split('behavior:rank_')[1])
            )

    # Make sure that `choice_list` is in the same order that participants
    # indicated.
    choice_list = np.array(choice_list)
    rank_order_list = np.array(rank_order_list)
    idx_sorted = np.argsort(np.array(rank_order_list))
    choice_list = choice_list[idx_sorted]

    if query in reference_list:
        # A catch trial.
        grade_primary = 0
        if choice_list[0] == query:
            grade_primary = 100
        elif len(choice_list)>1:
            if choice_list[1] == query:
                grade_primary = 50
    else:
        grade_primary = -1

    return grade_primary
