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


def initialize_guest_counter(cxn_psiz03, cursor_psiz03):
    """Initialize guest_counter."""
    # Check if "guest" counter already present.
    query = (
        "SELECT counter_value FROM counter WHERE counter_name='guest'"
    )
    cursor_psiz03.execute(query)
    sql_result = cursor_psiz03.fetchall()

    if len(sql_result) < 1:
        # Does not exist, so create.
        query = (
            "INSERT INTO counter (counter_name, counter_value) "
            " VALUES ('guest', 0)"
        )
        cursor_psiz03.execute(query)
        cxn_psiz03.commit()
