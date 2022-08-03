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

from psiz_database import utils


def lookup_asset_id36(cursor_psiz03, fp_asset):
    """Lookup `id36` given asset filepath.
    
    Assumes `fp_asset` is correctly formated such that the first part
    of the filepath can be used to determine the correct subdomain.

    Args:
        cursor_psiz03:
        fp_asset: Asset filepath.

    Returns:
        id36: String of base-36 ID.

    """
    domain_table_name = 'domain_pz'  # TODO

    fp_parts = fp_asset.split('/')
    subdomain_label = fp_parts[1]

    query = (
        "SELECT id36 FROM {0} WHERE label = %s"
    ).format(domain_table_name)
    vals = [subdomain_label]
    cursor_psiz03.execute(query, vals)
    sql_result = cursor_psiz03.fetchall()
    id36_subdomain = sql_result[0][0]

    subdomain_table_name = utils.generate_subdomain_table_name(id36_subdomain)

    query = (
        "SELECT id36 FROM {0} WHERE filepath = %s"
    ).format(subdomain_table_name)
    vals = [fp_asset]
    cursor_psiz03.execute(query, vals)
    sql_result = cursor_psiz03.fetchall()
    id36_asset = sql_result[0][0]

    return id36_asset
