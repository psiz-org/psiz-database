# Organization

## Modules
`db_psiz03`: Python code for inserting and updating the MySQL database.
`sql`: Helpful wrapper functions for making MySQL connections.
`utils`: Helpful utility functions.

## Design Factors
Roughly, the different design factors correspond to:
* `project_name`: (factor_0) experiment/project name (e.g., "rank", "categorize")
* `stimulus_set_name`: (factor_1) stimulus set name
* `protocol_name`: (factor_2) protocol
* `factor_3`: condition
* `factor_4`: unassigned

However, the factor designations are intentionally left vague using numbers to allow flexibility in identifying unique designs

## Timestep Types
* "rank:ssss"
* "rate:ssss"
* "categorize:ssss"
* "questionnaire:ssss"
* "optional_feedback:ssss"

Note: The timestep type is *not* redundant with `designs.factor_0` since the task name may be something that denotes the multiple tasks performed in the sequence. For simple sequences they may be the same, but in general they are different.

### Example Subtypes
* rank:8choose2
* rank:4choose1
* rank:2choose1
* categorize:unconstrained
* categorize:unconstrained_with-feedback
* categorize:4afc-label_with-feedback
* categorize:4afc-label-image_with-feedback
* rate:5point
* questionnaire:birding_experience
* questionnaire:final_comments_and_feedback

## Interaction Types
At the highest level, distinguish between content shown to participant (stimulus), participant behavior (behavior), and system information (info)

Follows format:
* "stimulus:ssss"
* "behavior:ssss"
* "info:ssss"

### Example Subtypes
* "stimulus:query"
* "stimulus:reference_0"
* "stimulus:reference_1"
* "stimulus:warning"
* "stimulus:graded_feedback"
* "behavior:rank_0"
* "behavior:rank_1"
* "behavior:submit_response"
* "info:visibility"
* "info:window_resize"
* "info:finish_trial"  MAYBE stimulus type?

## Grades
Database uses a grade strategy. This allows downstream processing to decide what's accepted/rejected. For example, grade information allows web applications to dynamically decide if a protocol has sufficient participants. Grade strategy dodges issue of defining what counts as expired versus dropped.
* spec:
    * `-1` to indicate ungraded item
    * [`0`, `100`] to indicate graded item and corresponding grade.

## Exporting MySQL data as JSON-formatted files.