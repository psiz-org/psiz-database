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


def  grade_response_time(design_factors, timestep):
    """Grade response time."""
    # Defaults based on timestep kind.
    if timestep['kind'] == 'rank:8choose2':
        # NOTE The CVPR 2021 criterion is 1000 ms.
        if timestep['response_time_ms'] < 1000:
            rt_grade = 0
        else:
            rt_grade = 100
    elif timestep['kind'] == 'rank:2choose1':
        if timestep['response_time_ms'] < 500:
            rt_grade = 0
        else:
            rt_grade = 100
    elif 'categorize:unconstrained' in timestep['kind']:
        if timestep['response_time_ms'] < 1000:
            rt_grade = 0
        else:
            rt_grade = 100
    elif timestep['kind'] == 'questionnaire:birding_experience':
        rt_grade = 100
    elif timestep['kind'] == 'questionnaire:feedback':
        rt_grade = 100

    # Override defaults.
    # Example:
    # if (
    #     design_factors['project'] == 'rank:Birds2019' and
    #     design_factors['stimulus_set'] == 'Birds2019'
    # ):
    #     if timestep['response_time_ms'] > 500:
    #         rt_grade = 100
    #     else:
    #         rt_grade = 0

    if rt_grade is None:
        print(
            'WARNING: no RT criterion for {}, giving perfect RT grade.'.format(
                timestep['kind']
            )
        )
        rt_grade = 100

    return rt_grade
