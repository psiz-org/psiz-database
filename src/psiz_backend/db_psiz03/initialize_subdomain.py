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

import logging
from pathlib import Path

import numpy as np

from psiz_database import utils


def initialize_subdomain(
        fp_project, cxn_psiz03, cursor_psiz03, subdomain_label,
        domain_prefix='PZ'):
    """Initialize subdomain.
    
    Create entry in "domain" table and create new "subdomain" table.

    Args:
        fp_project:
        cxn_psiz03:
        cursor_psiz03:
        subdomain_label:
        domain_prefix (optional):

    """
    # Hardcoded settings.
    subdomain_length = 3
    item_length = 7

    domain_table_name = generate_domain_table_name(domain_prefix)

    # Check if subdomain already exists in subdomain table.
    query = (
        "SELECT id, id36 FROM {0} WHERE label=%s"
    ).format(domain_table_name)
    vals = [subdomain_label]
    cursor_psiz03.execute(query, vals)
    sql_result = cursor_psiz03.fetchall()

    if len(sql_result) < 1:
        # Subdomain does not exist in domain table, so insert.
        query = (
            "SELECT MAX(id36) FROM {0}"
        ).format(domain_table_name)
        cursor_psiz03.execute(query)
        sql_result = cursor_psiz03.fetchall()

        if sql_result[0][0] is None:
            id10 = 1
            id36 = np.base_repr(id10, 36).zfill(subdomain_length)
            id36 = domain_prefix + id36
        else:
            id10 = int(sql_result[0][0], 36) + 1
            id36 = np.base_repr(id10, 36)

        query = (
            "INSERT INTO {0} (id36, label) VALUES (%s, %s)"
        ).format(domain_table_name)
        vals = [id36, subdomain_label]
        cursor_psiz03.execute(query, vals)
        cxn_psiz03.commit()
    else:
        id36 = sql_result[0][1]

    # Check if `subdomain_<x>` table exists.
    subdom_table_name = utils.generate_subdomain_table_name(id36)
    query = (
        "SHOW TABLES LIKE %s"
    )
    vals = [subdom_table_name]
    cursor_psiz03.execute(query, vals)
    sql_result = cursor_psiz03.fetchall()
    
    fp_assets = fp_project / Path('assets', subdomain_label, 'assets.txt')
    if len(sql_result) < 1:
        if fp_assets.is_file():
            # Create subdomain table.
            query = (
                "CREATE TABLE IF NOT EXISTS {0} ("
                "id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,"
                "id36 VARCHAR(16) NOT NULL,"
                "filepath VARCHAR(255) NOT NULL"
                ");"
            ).format(subdom_table_name)
            cursor_psiz03.execute(query)
            cxn_psiz03.commit()

            # Try to populate table.
            populate_subdomain_table(
                cxn_psiz03, cursor_psiz03, fp_assets, subdom_table_name, id36,
                item_length
            )

            # Update "domain" table with asset count.
            update_asset_count(cxn_psiz03, cursor_psiz03, domain_table_name, id36)
        else:
            logging.warning('File not found "{0}"'.format(fp_assets))


def populate_subdomain_table(
        cxn_psiz03, cursor_psiz03, fp_assets, subdom_table_name, id36,
        item_length):
    """Populate subdomain table.
    
    Args:
        cxn_psiz03:
        cursor_psiz03:
        fp_assets:
        subdom_table_name:
        id_36:
        item_length:

    """
    try:
        file_stimuli = open(fp_assets, 'r')
        lines = file_stimuli.readlines()

        counter = 1
        # Strips the newline character
        for line in lines:
            fp = line.strip()
            id36_item = id36 + np.base_repr(counter, 36).zfill(item_length)
            query = (
                "INSERT INTO {0} (id36, filepath) VALUES (%s, %s)"
            ).format(subdom_table_name)
            vals = [id36_item, fp]
            cursor_psiz03.execute(query, vals)
            cxn_psiz03.commit()
            
            counter += 1
        logging.info('Created subdomain table {0}'.format(subdom_table_name))
    except FileNotFoundError:
        logging.warning('File not found "{0}"'.format(fp_assets))


def update_asset_count(cxn_psiz03, cursor_psiz03, domain_table_name, id36):
    """Update asset count in corresponding domain table.
    
    Args:
        cxn_psiz03:
        cursor_psiz03:
        domain_table_name:
        id36:

    """
    subdom_table_name = utils.generate_subdomain_table_name(id36)

    query = (
        "SELECT COUNT(id36) FROM {0}"
    ).format(subdom_table_name)
    cursor_psiz03.execute(query)
    sql_result = cursor_psiz03.fetchall()
    asset_count = sql_result[0][0]

    query = (
        "UPDATE {0} SET asset_count = %s WHERE id36 = %s;"
    ).format(domain_table_name)
    vals = [asset_count, id36]
    cursor_psiz03.execute(query, vals)
    cxn_psiz03.commit()


def generate_domain_table_name(domain_prefix):
    """Generate "domain" table name.
    
    Args:
        domain prefix: A base-36 prefix.

    Returns:
        String of MySQL table name.

    """
    domain_table_name = 'domain_' + domain_prefix.lower()
    return domain_table_name
