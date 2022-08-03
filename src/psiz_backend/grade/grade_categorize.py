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


def grade_categorize(design_factors, timestep, interactions_data):
    """Grade categorize trial."""
    query = ""
    for interaction in interactions_data:
        interaction_variety = interaction[0]
        # interaction_datetime = interaction[1]
        details = interaction[2]
        if interaction_variety == "stimulus:query":
            query = details
        if interaction_variety == "behavior:submit_response":
            response = details
    
    # Derive correct answer from file name.
    parts = query.split("_")
    keep_list = []
    for part in parts:
        if not part[0].isnumeric():
            keep_list.append(part)
    correct_answer = " "
    correct_answer = correct_answer.join(keep_list).lower()
    
    # Check if response matches correct answer.
    response = response.lower()
    edist = levenshtein(correct_answer, response)
    if edist < 3:
        grade_primary = 100
    else:
        grade_primary = 0

    return grade_primary


def memoize(func):
    mem = {}
    def memoizer(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in mem:
            mem[key] = func(*args, **kwargs)
        return mem[key]
    return memoizer


@memoize    
def levenshtein(s, t):
    """Levenshtein distance.
    
    see:  https://python-course.eu/applications-python/levenshtein-distance.php

    """
    if s == "":
        return len(t)
    if t == "":
        return len(s)
    if s[-1] == t[-1]:
        cost = 0
    else:
        cost = 1
    
    res = min([levenshtein(s[:-1], t)+1,
               levenshtein(s, t[:-1])+1, 
               levenshtein(s[:-1], t[:-1]) + cost])

    return res