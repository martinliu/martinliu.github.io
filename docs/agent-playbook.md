# Agent Playbook

This playbook standardizes how coding agents should execute tasks in this repository.

## 1) Task Classification

Determine task type first:

- Content update: markdown/front matter only.
- Presentation update: `layouts/`, `assets/`, CSS/JS partials.
- Build/config update: `config/`, Hugo behavior, workflow-adjacent changes.
- Script/tooling update: `scripts/` and related docs.

## 2) Execution Workflow

1. Read only the files required for the task.
2. Confirm constraints from `AGENTS.md`.
3. Make minimal edits.
4. Run the smallest applicable validation set.
5. Report exact files changed and validation results.

## 3) Validation Matrix

- Content update: run `hugo --minify --gc --enableGitInfo --cleanDestinationDir --logLevel info`.
- Presentation update: run the same build command and spot-check related templates/partials for broken references.
- Build/config update: run the same build command and verify config keys/paths remain valid.
- Script/tooling update: run changed script in safe/preview mode when supported; build if output can affect rendering.

## 4) Change Safety Rules

- Do not mass-edit `public/` unless explicitly requested.
- Avoid broad binary/image rewrites without a clear requirement.
- Do not alter deployment intent in `.github/workflows/` for unrelated tasks.
- Keep backward compatibility for existing content paths and links.

## 5) Response Template (Agent Output)

Use this structure in completion messages:

1. Summary of what changed.
2. Files changed.
3. Validation run and outcomes.
4. Risks or follow-up items (if any).

## 6) Common Pitfalls

- Breaking front matter structure in multilingual posts.
- Accidentally changing generated output in `public/`.
- Updating docs with commands that do not match real repo scripts.
- Introducing heavy dependency requirements for simple content tasks.
