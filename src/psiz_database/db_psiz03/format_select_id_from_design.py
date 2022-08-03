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


def format_select_id_from_design(
        project=None, stimulus_set=None, protocol=None,
        factor_d=None, factor_e=None):
    """Select design IDs for requested design parameters.

    Args:
        project:
        stimulus_set:
        protocol:
        factor_d:
        factor_e:

    Returns:
        query: A statement to be executed.
        vals: Values to use when executing the statement.

    """
    # Format conditional of query statement based on provided design info.
    conditional = []
    vals = []
    if project is not None:
        conditional.append('project=%s')
        vals.append(project)
    if stimulus_set is not None:
        conditional.append('stimulus_set=%s')
        vals.append(stimulus_set)
    if protocol is not None:
        conditional.append('protocol=%s')
        vals.append(protocol)
    if factor_d is not None:
        conditional.append('factor_d=%s')
        vals.append(factor_d)
    if factor_e is not None:
        conditional.append('factor_e=%s')
        vals.append(factor_e)

    if len(conditional) > 0:
        conditional = ' AND '.join(conditional)
        conditional = ' WHERE ' + conditional
    else:
        conditional = ''
    
    query = (
        'SELECT id FROM design' + conditional
    )

    return query, vals
