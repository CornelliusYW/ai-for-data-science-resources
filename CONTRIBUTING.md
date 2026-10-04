# Contributing

Thank you for helping us keep this collection current. Maybe you have found a course, tutorial, notebook, or guide that improved your data work. We would like to learn about it.

However, a resource suggestion should do more than mention AI. It should help a data professional learn or apply AI in an actual data science workflow. The strongest resources also help us check the result and understand when the method is not suitable.

## Suggest a resource

Open a **Resource suggestion** issue and provide:

- Resource name and direct URL
- Suggested category and resource type
- What it teaches and where it fits in data science work
- Whether it is free or paid
- Whether it includes code, notebooks, exercises, or projects
- When it was last updated, if known
- Any affiliation you have with the resource

Affiliation disclosure is required. We review an affiliated resource with the same criteria as every independent suggestion.

## Submit a pull request

1. Read [Resource Guidelines](docs/resource-guidelines.md).
2. Add or update the entry in `data/resources.yaml`.
3. Use a stable direct URL and write a factual description.
4. Set `last_verified` to the date you actually reviewed the resource.
5. Run:

   ```bash
   python -m pip install -r requirements.txt
   python scripts/validate_resources.py
   python scripts/generate_readme.py
   python scripts/generate_readme.py --check
   python scripts/check_internal_links.py
   ```

6. Commit the generated README and category-page changes with the YAML change.
7. Complete the pull request template, including affiliation disclosure.

For a new category, explain why the existing taxonomy is not enough and provide several distinct resources that justify the split. The category size is not fixed. For me, the quality and usefulness matter more than matching another category's number.

## Style

Use simple and direct English. Explain what the resource is, what we can learn, and where it fits. Avoid promotional language and unsupported claims. The full voice guide is in [Writing Style](docs/writing-style.md).

Do not add a resource only because it is new, popular, or mentions AI. We should also never include API keys, private data, or copied course material.

