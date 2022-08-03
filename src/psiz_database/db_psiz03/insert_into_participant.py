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

import uuid


def insert_into_participant(
        cxn_psiz03, cursor_psiz03, personal_id, amt_hit_id):
    """Add to `participant` table.
    
    Args:
        personal_id: A string of (potentially) personally identifiable
            information. For example, an AWS worker ID.
        amt_hit_id: A string indicating a Mechanical Turk HIT ID.

    """
    # Intercept personal ID, to see if it needs to be modified.
    if personal_id == "undefined":
        # Get and increment guest_counter.
        query = (
            "SELECT counter_value FROM counter WHERE counter_name='guest'"
        )
        cursor_psiz03.execute(query)
        sql_result = cursor_psiz03.fetchall()
        guest_counter = sql_result[0][0]
        query = (
            "UPDATE counter SET counter_value=%s "
            "WHERE counter_name='guest'"
        )
        vals = (guest_counter + 1,)
        cursor_psiz03.execute(query, vals)
        cxn_psiz03.commit()
        
        personal_id = "guest_{}".format(guest_counter)

    # Infer if AMT worker.
    if (amt_hit_id == "undefined") or (amt_hit_id == ""):
        is_amt_worker_id = 0
    else:
        is_amt_worker_id = 1

    # Check if `personal_id` is already present in database.
    query = (
        "SELECT anonymous_id FROM participant WHERE personal_id=%s"
    )
    vals = (personal_id,)
    cursor_psiz03.execute(query, vals)
    sql_result = cursor_psiz03.fetchall()
        
    if len(sql_result) > 0:
        # Participant already exists.
        anonymous_id = sql_result[0][0]
    else:
        # Participant does not exist yet.
        anonymous_id = str(uuid.uuid4())

        query = (
            "INSERT INTO participant (personal_id, anonymous_id, "
            "is_amt_worker_id) VALUES (%s, %s, %s)"
        )
        vals = (personal_id, anonymous_id, is_amt_worker_id)
        cursor_psiz03.execute(query, vals)
        cxn_psiz03.commit()

    return anonymous_id, is_amt_worker_id
