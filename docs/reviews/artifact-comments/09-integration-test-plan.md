# Review Comments: docs/vmodel/09-integration-test-plan.md

## qa_verification_agent - testability and evidence quality

Verdict: changes_required

### Comment 1

- Severity: major
- Blocking: yes
- Comment: The plan names test categories, but several tests lack exact commands, expected outputs, fixtures, and pass/fail thresholds.
- Required action: Add executable commands, expected evidence files, and pass/fail criteria for every planned test.

### Comment 2

- Severity: critical
- Blocking: yes
- Comment: The RTM references IT-004 through IT-014 but this plan defines only IT-001 through IT-003.
- Required action: Either define the missing integration tests or repair RTM mappings to use only existing evidence.

### Comment 3

- Severity: minor
- Blocking: no
- Comment: Review lens `testability and evidence quality` confirms this document must remain linked to requirements, code modules, tests, issues, and PR evidence.
- Required action: Keep links synchronized when tasks or code move.

Software Lead disposition:

Software Lead blocks full staged implementation/test entry for this artifact until required actions are resolved. A dev-mode exploratory PR may remain open, but release progression is blocked.

## development_lead_agent - developer execution and automation hooks

Verdict: changes_required

### Comment 1

- Severity: major
- Blocking: yes
- Comment: The plan names test categories, but several tests lack exact commands, expected outputs, fixtures, and pass/fail thresholds.
- Required action: Add executable commands, expected evidence files, and pass/fail criteria for every planned test.

### Comment 2

- Severity: critical
- Blocking: yes
- Comment: The RTM references IT-004 through IT-014 but this plan defines only IT-001 through IT-003.
- Required action: Either define the missing integration tests or repair RTM mappings to use only existing evidence.

### Comment 3

- Severity: minor
- Blocking: no
- Comment: Review lens `developer execution and automation hooks` confirms this document must remain linked to requirements, code modules, tests, issues, and PR evidence.
- Required action: Keep links synchronized when tasks or code move.

Software Lead disposition:

Software Lead blocks full staged implementation/test entry for this artifact until required actions are resolved. A dev-mode exploratory PR may remain open, but release progression is blocked.

## release_quality_agent - gate readiness and audit evidence

Verdict: changes_required

### Comment 1

- Severity: major
- Blocking: yes
- Comment: The plan names test categories, but several tests lack exact commands, expected outputs, fixtures, and pass/fail thresholds.
- Required action: Add executable commands, expected evidence files, and pass/fail criteria for every planned test.

### Comment 2

- Severity: critical
- Blocking: yes
- Comment: The RTM references IT-004 through IT-014 but this plan defines only IT-001 through IT-003.
- Required action: Either define the missing integration tests or repair RTM mappings to use only existing evidence.

### Comment 3

- Severity: minor
- Blocking: no
- Comment: Review lens `gate readiness and audit evidence` confirms this document must remain linked to requirements, code modules, tests, issues, and PR evidence.
- Required action: Keep links synchronized when tasks or code move.

Software Lead disposition:

Software Lead blocks full staged implementation/test entry for this artifact until required actions are resolved. A dev-mode exploratory PR may remain open, but release progression is blocked.
