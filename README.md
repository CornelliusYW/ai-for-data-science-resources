<p align="center">
  <a href="https://www.nb-data.com/"><img src="assets/non-brand-data-logo.png" alt="Non-Brand Data" width="420"></a>
</p>

# AI for Data Science Resources

Resources for learning how to use AI in data analysis, SQL, machine learning, coding, evaluation, and production.

Curated by [Non-Brand Data](https://www.nb-data.com/), an independent publication by [Cornellius Yudha Wijaya](https://www.linkedin.com/in/cornellius-yudha-wijaya/).

<!-- STATUS_START -->
**Last reviewed:** 2026-10-04  
**Resources:** 85  
**Categories:** 11
<!-- STATUS_END -->

## Where should I start?

- **Use AI in my current data science work:** [analysis and SQL](resources/ai-assisted-analysis-and-sql.md) -> [coding agents and context](resources/coding-agents-and-context.md) -> [AI-assisted ML](resources/ai-assisted-machine-learning.md)
- **Build data agents:** [coding agents and context](resources/coding-agents-and-context.md) -> [data science agents](resources/data-science-agents.md) -> [evaluation](resources/evaluation-and-reproducibility.md)
- **Improve ML workflows:** [AI-assisted ML](resources/ai-assisted-machine-learning.md) -> [tabular foundation models](resources/tabular-foundation-models.md) -> [MLOps](resources/mlops-and-production.md)
- **Move from notebook to production:** [coding agents and context](resources/coding-agents-and-context.md) -> [evaluation](resources/evaluation-and-reproducibility.md) -> [MLOps](resources/mlops-and-production.md)
- **Try foundation models for forecasting:** [time series foundation models](resources/time-series-foundation-models.md) -> [evaluation](resources/evaluation-and-reproducibility.md) -> [MLOps](resources/mlops-and-production.md)

The detailed steps and expected outputs are available in [`learning-paths/`](learning-paths/).

## Browse by data science workflow

<!-- CATEGORY_TABLE_START -->
| Workflow area | What it covers | Resources |
|---|---|---:|
| [AI-Assisted Analysis and SQL](resources/ai-assisted-analysis-and-sql.md) | Use AI to explore datasets, write and inspect SQL, and move from a question to a reproducible analysis. | 10 |
| [AI for Data Preparation and Extraction](resources/data-preparation-and-extraction.md) | Turn documents and messy inputs into structured, validated data that can enter an analysis workflow. | 8 |
| [AI-Assisted Machine Learning](resources/ai-assisted-machine-learning.md) | Build strong baselines, compare models, and automate repetitive parts of supervised machine learning. | 7 |
| [Tabular Foundation Models](resources/tabular-foundation-models.md) | Try pretrained models designed for tabular prediction and compare them with established tree-based baselines. | 6 |
| [Coding Agents and Context Engineering](resources/coding-agents-and-context.md) | Use coding agents safely in notebooks and repositories, with durable project instructions and business context. | 9 |
| [Data Science Agents](resources/data-science-agents.md) | Build agents that plan analyses, call tools, inspect data, and complete multi-step data tasks. | 8 |
| [Evaluation and Reproducibility](resources/evaluation-and-reproducibility.md) | Test AI-generated analysis and agent behavior with datasets, traces, assertions, and repeatable evaluations. | 10 |
| [MLOps and Production](resources/mlops-and-production.md) | Move AI-assisted data work from a notebook into tested, observable, deployable systems. | 8 |
| [Visualization and Communication](resources/visualization-and-communication.md) | Use AI to prototype visual explanations, analytical apps, dashboards, and reports without giving up review. | 5 |
| [Time Series Foundation Models](resources/time-series-foundation-models.md) | Apply pretrained forecasting models and compare zero-shot forecasts with domain-specific baselines. | 7 |
| [End-to-End Courses](resources/end-to-end-courses.md) | Follow structured courses with code, exercises, and projects that connect several parts of the workflow. | 7 |
<!-- CATEGORY_TABLE_END -->

## Featured learning resources

- [Data Analysis with ChatGPT](https://help.openai.com/en/articles/8437071-data-analysis-with-chatgpt) shows the basic loop of uploading data, asking questions, and inspecting generated analysis.
- [Data Formulator](https://github.com/microsoft/data-formulator) is a concrete example of AI-assisted data transformation and visualization.
- [Cleanlab Datalab Tutorials](https://docs.cleanlab.ai/stable/tutorials/datalab/) apply model-based signals to label errors, duplicates, and other data quality problems.
- [AutoGluon Tabular Tutorials](https://auto.gluon.ai/stable/tutorials/tabular/index.html) provide a strong automated baseline for tabular prediction.
- [TabPFN](https://github.com/PriorLabs/TabPFN) lets us test a tabular foundation model on real datasets.
- [AGENTS.md](https://agents.md/) offers a small, durable way to give coding agents project instructions.
- [Microsoft AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners) teaches agent concepts through written lessons and code.
- [MLflow GenAI Evaluation and Monitoring](https://mlflow.org/docs/latest/genai/eval-monitor/) connects datasets, experiments, traces, and monitoring.
- [MLOps Zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) covers the engineering work between an experiment and a maintained system.
- [TimesFM](https://github.com/google-research/timesfm) is one way to begin testing zero-shot time-series forecasting.

## New this month

- **[Granite Time Series Foundation Models](https://github.com/ibm-granite/granite-tsfm):** compact pretrained models and examples for forecasting.
- **[Google Agent Development Kit](https://adk.dev/):** code-first agent development with evaluation and deployment material.
- **[Pydantic Evals](https://pydantic.dev/docs/ai/evals/evals/):** typed evaluation datasets and evaluators that fit naturally into Python projects.

## Projects we can try

- Turn an existing notebook into a tested package with help from a coding agent.
- Build a text-to-SQL assistant against a small database and a written metric layer.
- Compare TabPFN, AutoGluon, and a tree-based baseline on one tabular problem.
- Extract structured records from a set of messy documents and review validation failures.
- Build a data agent that writes an analysis plan before it calls any tools.
- Compare a zero-shot time-series foundation model with seasonal naive and statistical baselines.

See [Project Ideas to Try](projects/project-ideas.md) for scopes and review criteria.

## How this repository is maintained

The `data/resources.yaml` file is the source of truth. Links and new resources are reviewed monthly. A larger curation review runs quarterly.

The workflow is:

**discover -> verify -> propose -> human review -> merge**

Automation proposes changes but does not add or remove resources. See [Maintenance](docs/maintenance.md) and [Resource Guidelines](docs/resource-guidelines.md).

## Contributing

Recommend a course, notebook, or guide through the resource suggestion form. See [CONTRIBUTING.md](CONTRIBUTING.md).

## About Non-Brand Data

[Non-Brand Data](https://www.nb-data.com/) is an independent publication by [Cornellius Yudha Wijaya](https://www.linkedin.com/in/cornellius-yudha-wijaya/) about data, machine learning, GenAI, and analytics.

You can learn more from the [Non-Brand Data About page](https://www.nb-data.com/about), browse the [publication archive](https://www.nb-data.com/archive), or connect with me on [LinkedIn](https://www.linkedin.com/in/cornellius-yudha-wijaya/).

## License

Repository text and code are available under the [MIT License](LICENSE). Linked resources keep their own licenses and terms.

