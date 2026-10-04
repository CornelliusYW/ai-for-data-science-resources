# AI-Assisted Analysis and SQL

Data analysis often starts with a question. To answer it, we need to find the right data, write the query, check the number, and explain what it means.

We can use AI to help with these activities. For example, it can propose an analysis plan, write SQL, or create a chart. However, the generated result can still use the wrong table, join, filter, or metric definition.

## Try this

Let's start with a small dataset and one metric definition. Ask an assistant to create the analysis plan before writing any code. Then, check every query, number, and chart against the data.

## Resources

<!-- RESOURCE_LIST_START -->
| Resource | Type | Access | Practice | Level | Status |
|---|---|---|---|---|---|
| [Data Analysis with ChatGPT](https://help.openai.com/en/articles/8437071-data-analysis-with-chatgpt) | Official Documentation | Paid or account required | Hands-on | Beginner | Active |
| [PandasAI](https://github.com/sinaptik-ai/pandas-ai) | Tool | Free | Hands-on | Intermediate | Active |
| [Data Formulator](https://github.com/microsoft/data-formulator) | Tool | Free | Hands-on | Intermediate | Active |
| [LIDA](https://github.com/microsoft/lida) | GitHub Curriculum | Free | Hands-on | Advanced | Check compatibility |
| [BigQuery Data Canvas](https://docs.cloud.google.com/bigquery/docs/data-canvas) | Official Documentation | Paid or account required | Hands-on | Intermediate | Active |
| [Snowflake Cortex Analyst](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst) | Official Documentation | Paid or account required | Hands-on | Advanced | Active |
| [LangChain SQL Agent Tutorials](https://docs.langchain.com/oss/python/learn) | Tutorial | Free | Hands-on | Intermediate | Active |
| [LlamaIndex Text-to-SQL Guide](https://developers.llamaindex.ai/python/examples/index_structs/struct_indices/sqlindexdemo/) | Tutorial | Free | Hands-on | Intermediate | Active |
| [Just Enough SQL to Safely Use AI for Data Analysis](https://motherduck.com/blog/just-enough-sql-for-ai/) | Tutorial | Free | Hands-on | Beginner | Active |
| [AI in Hex](https://learn.hex.tech/docs/getting-started/ai-overview) | Official Documentation | Paid or account required | Hands-on | Beginner | Active |
<!-- RESOURCE_LIST_END -->

For me, text-to-SQL is easier to learn with a small read-only database. Write down the expected grain, joins, filters, and metric definitions first. This way, we have a known result to compare with the generated SQL.

