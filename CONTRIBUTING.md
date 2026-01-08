Contributing (Internal Only)

Status: This repository is maintained by Novel Signature Homes engineering. External
contributions are not accepted. The guidance below is intended for organization
members and authorized contributors only.

If you are not a Novel Signature Homes employee or authorized contractor, please do
not open pull requests, issues, or attempt to reuse repository assets.

Process for internal contributors

1. Branching
   - Create a branch from `main` using an org-based branch name: `team/feature-short-desc` or `user/bugfix-short-desc`.

2. Development
   - Keep changes scoped to a single logical change.
   - For changes that add or modify image/asset content, ensure assets are optimized and do not include private customer data.

3. Tests & Validation
   - Run the static preview locally (see README) and verify tour loads and tiles/images render correctly.

4. Pull Requests
   - Open a PR to `main` in this repository (not from forks if possible).
   - Include a clear description of the change, impacted tours, and screenshots if applicable.
   - Assign relevant reviewers and label the PR appropriately.

5. Reviews & Merging
   - PRs require at least one code review approval from the team and any automated checks must pass.
   - Squash or rebase as appropriate; use descriptive commit messages.

6. CI / Deployment
   - Merging to `main` will update the content served by GitHub Pages. Coordinate deployments with the platform/ops team.

Security and sensitive data

- Do not commit API keys, secrets, or private customer data. If you accidentally commit sensitive data, notify the security team immediately and follow the internal incident response process.

External pull requests and forks

- External forks and PRs will be closed and not merged. This repository's public visibility is only to support GitHub Pages hosting and not to invite outside contributions.

Contact

- For contribution access, repository permissions, or deployment coordination, contact the Novel Signature Homes engineering/repo owners via internal channels.
