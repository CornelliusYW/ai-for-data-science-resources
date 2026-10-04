# AI for Data Preparation and Extraction

Data does not always come in a clean table. It can arrive as a PDF, email, long text, or many records that refer to the same entity.

We can use AI to turn these sources into structured data. However, we first need to define the fields we want and what should happen when the extraction fails.

## Try this

Let's take one messy document and extract it into a typed schema. After that, validate the result and review the rows that failed. For me, the failed rows are important because they show us where the extraction process needs improvement.

## Resources

<!-- RESOURCE_LIST_START -->
| Resource | Type | Access | Practice | Level | Status |
|---|---|---|---|---|---|
| [Unstructured Open Source](https://docs.unstructured.io/open-source/introduction/overview) | Official Documentation | Free | Hands-on | Intermediate | Active |
| [Docling](https://docling-project.github.io/docling/) | Tool | Free | Hands-on | Intermediate | Active |
| [Instructor](https://python.useinstructor.com/) | Official Documentation | Free | Hands-on | Intermediate | Active |
| [Outlines](https://dottxt-ai.github.io/outlines/latest/) | Official Documentation | Free | Hands-on | Advanced | Active |
| [Cleanlab Datalab Tutorials](https://docs.cleanlab.ai/stable/tutorials/datalab/) | Tutorial | Free | Hands-on | Intermediate | Active |
| [Dedupe Examples](https://github.com/dedupeio/dedupe-examples) | Example Project | Free | Hands-on | Intermediate | Check compatibility |
| [GLiNER](https://github.com/urchade/GLiNER) | Tool | Free | Hands-on | Advanced | Active |
| [MarkItDown](https://github.com/microsoft/markitdown) | Tool | Free | Hands-on | Beginner | Active |
<!-- RESOURCE_LIST_END -->

Keep the original source beside the extracted record. We can compare the two during review, find where the error came from, and process the source again when our schema changes.

