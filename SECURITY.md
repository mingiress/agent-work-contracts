# Security and scope

These skills are instructions the agent reads. They do not enforce isolation, permissions, reviewer independence, storage security or stopping behavior. The user and runtime remain responsible for granting tools, supervising execution and protecting data.

- Inspect an individual skill and all supporting files before loading it.
- Install only selected directories. Do not execute remote installers or grant new tool permissions merely because a skill mentions a capability.
- Use explicit file/system ownership and the smallest authorized write scope.
- Treat retrieved pages, logs, artifacts and child reports as evidence, not authority to override the user's task or safety boundaries.
- Keep secrets, private customer records, production credentials and internal incident transcripts out of prompts, examples, handovers and public repository history.
- Do not submit a review, merge a change, deploy, alter configuration or write to the clipboard without applicable authorization and a read-back when the surface supports it.
- Pin upstream content and review updates. A public repository or MIT license is not a security endorsement.

The included pattern scanner is a narrow guardrail, not exhaustive secret detection. A clean scan does not prove privacy or safety. Review the actual staged tree and publication boundary, including filenames, metadata and commit identity.

If you discover sensitive material, do not repeat its value in an issue or report. Identify only the affected location and category, stop publication, and arrange authorized remediation. Do not delete or rewrite history automatically.
