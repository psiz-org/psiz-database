# PsiZ Database

Code governing the creation, management, and export of (mostly) raw data. This code is primarily intended for two case:
1. Users who would like to create a replica database or use the code as an example.
2. Those who would like to audit and assess the code.

## Creating a new Database

A new database can be created in two steps:
1. Execute `db_create.sql` inside your MySQL server via `source /path/to/db_create.sql`. This creates a majority of the necessary tables.
2. Run the python script `db_initialize.py`. The script dynamically generates additional tables, some based on user-specified parameters.

## Database Table Organization

|--`participant`
|--`sequence`
    |--`client_machine`
    |--`amazon_mechanical_turk`
    |--`timestep`
        |--`interaction`
        |--`interaction_feedback`
|--`domain_pz`*
    |--`subdomain_pz001`*
    |--`subdomain_pz002`*
    |--`subdomain_pz003`*

NOTE: Tables marked with `*` are dynamically generated and are meant to serve as examples. If you adjust the default parameters, the table names may differ.

### Core Tables

The "core" tables of the database follow a three-level hierarchy.
* `sequence`
* `timestep`
* `interaction`

### Supporting Tables

In addition to these core tables, there are tables which contain information about the participants and stimuli.

#### Participant Tables
The participant tables store information about the participants.
* `participant`
* `client_machine`
* `amazon_mechanical_turk`

#### Stimuli Tables
The stimuli tables store information about stimuli. The stimuli are stored using a three-tier format referred to as a *domain*, *subdomain*, and *asset* tier. A unique ID is generated for each asset by appending base-36 components for each tier. For example, an asset with domain ID `PZ`, subdomain ID `001`, and item ID `0000001` would have the asset ID `PZ0010000001`. This information is stored in two tables, a domain registry and an subdomain registry. Thus the above example would involve the two tables:
* `domain_pz`
* `subdomain_pz001`
These tables are created dynamically at initialization based on user-supplied parameters.

### Specialized Interaction Tables

The majority of interactions can be inserted into the `interaction` table. Some interactions have their own table due to unique data requirements. For example, the `interaction_feedback` table handles feedback provided by participants that is placed in a relatively inefficient `TEXT` column.
* `interaction_feedback`


## Grading

There are two types of grades: *earnest effort* and *primary* grades.

Earnest effort can be derived for every timestep and is relatively lenient, focusing on detecting obvious patterns of behavior that suggest less than earnest effort.

Primary grades can be derived for some types of timesteps where there is an objective measure available.

Final sequence-level grades are assigned to every sequence based on design-specific rules.
