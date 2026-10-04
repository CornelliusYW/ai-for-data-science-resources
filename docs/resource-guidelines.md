# Resource Guidelines

This collection starts with one question: **How can we learn and use AI throughout our data science workflow?**

There are many AI resources available. However, not every resource helps us with data science work. A resource belongs here when it explains the workflow, gives us something to try, and shows enough detail to check the result.

For example, a text-to-SQL tutorial should not only show us which button to click. It should explain how to inspect the generated SQL, check the metric, or handle a question the system cannot answer.

## What belongs

For me, a resource should meet all of these conditions:

1. It directly supports data analysis, data preparation, machine learning, evaluation, communication, or production work.
2. It teaches through documentation, code, notebooks, exercises, worked examples, or a guide we can follow.
3. Its claims and description can be verified from the resource itself.
4. Its link works, and its dependencies or platform are current enough to use.
5. It adds something that an existing resource does not already cover well.

We first look at official documentation, maintained open-source courses, university material, and engineering guides with code or examples. We also prefer free resources. However, we can include a paid resource when it teaches something the free alternatives do not. In this case, we label the access requirement clearly.

## What does not belong

- Generic AI or data science roadmaps
- SEO articles, shallow listicles, and link collections that only point to other collections
- Product pages without lessons, examples, or documentation we can follow
- Research papers without a clear connection to data work
- Resources included mainly because of popularity or star count
- Duplicate tutorials for the same workflow
- Abandoned examples that no longer run, unless they remain unusually valuable and are marked `needs-review`

## Review process

When we find a candidate, the review process is:

1. Open the direct learning material, not only a landing page.
2. Confirm what a reader can learn and where it fits in data science work.
3. Inspect examples, notebooks, exercises, or documentation structure.
4. Check recent maintenance, releases, issues, and dependency support when applicable.
5. Confirm access requirements and whether “free” is accurate.
6. Compare it with existing entries.
7. Write a concise, factual description and use case.
8. Run validation and regenerate the derived sections.

GitHub stars can provide context, but they do not decide whether a resource belongs here. Older material can also remain when the method still applies and the examples still work.

## Metadata conventions

- `status: active` means the resource is suitable for the current collection.
- `status: needs-review` means the content still fits the collection but has a compatibility, maintenance, or access question.
- `status: archived` keeps historical metadata but excludes the resource from generated lists.
- `free: true` means the learning material and core hands-on path can be used without payment. It does not promise that every external API or hosted service is free.
- `last_verified` records the last human review, not the latest upstream release.

The description explains what the resource is. `use_case` explains what we can learn or do with it. We keep both fields concise and avoid promotional claims.

