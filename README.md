# service-desk-knowledge-base

Sample service desk knowledge base articles written the way a Service Desk Wiki should read: one problem per article, with symptom, cause, numbered resolution steps, a way to verify, and a clear escalation path. Includes a template and a linter that keeps every article consistent.

**Roles this supports:** Information Systems Technician, Service Desk Analyst, Help Desk Specialist, Desktop Support Technician, IT Support Specialist, Technical Support Specialist.

## Contents

- `articles/`: nine sample articles (see [articles/README.md](articles/README.md))
- `templates/kb-article-template.md`: the structure to copy
- `tools/lint_articles.py`: checks for required sections and fields, at least three resolution steps, and accidental passwords
- `tests/test_lint.py`: unit tests

## Usage

```bash
python3 tools/lint_articles.py .
python3 -m unittest discover -s tests -v
```

## Writing guidelines

1. Title the article with the words a user would search for.
2. Say what the article applies to (system, version, audience) and when it was last reviewed.
3. Put the exact error text under Symptom.
4. Use short numbered steps that begin with a verb, and warn before anything that deletes data or needs approval.
5. Always include How to verify and an escalation path with the evidence to attach.
6. Never include passwords, personal data or internal-only details.

## Notes

The articles are generic examples written for learning. Check them against your own environment, tools and policies before publishing them to a team wiki.

## License

MIT. See [LICENSE](LICENSE).
