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
"""Script to initialize MySQL database."""

import logging
from pathlib import Path

from psiz_database import db_psiz03
from psiz_database.sql.create_connection import create_connection


def db_initialize(fp_project, new_db_name, subdomain_list):
    """Handle initialization steps."""
    logging.basicConfig(level=logging.INFO)
    logging.info('Started')
    
    # Open MySQL connection to new database and create a cursor.
    cxn_psiz03 = create_connection(new_db_name)
    cursor_psiz03 = cxn_psiz03.cursor()

    # Initialize counter variables.
    db_psiz03.initialize_guest_counter(cxn_psiz03, cursor_psiz03)

    # Initialize subdomains.
    for subdomain_label in subdomain_list:
        db_psiz03.initialize_subdomain(
            fp_project, cxn_psiz03, cursor_psiz03, subdomain_label
        )

    cursor_psiz03.close()
    cxn_psiz03.close()
    logging.info('Finished')


if __name__ == "__main__":
    # Initialization settings (adjust these parameters based on your needs).
    fp_project = Path.home() / Path('packages', 'psiz-database')  # TODO change hypen to underscore
    new_db_name = "psiz03"
    subdomain_list = [
        'birds_2019',
        'skin_lesions_2018',
        'rocks_2016',
        'ilsvrc_2012_val',
        'regional_birds',
        'ilsvrc_2012_train',
        'ecoset_2021_train',
    ]

    db_initialize(fp_project, new_db_name, subdomain_list)
