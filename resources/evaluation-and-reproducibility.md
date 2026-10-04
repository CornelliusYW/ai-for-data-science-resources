# Evaluation and Reproducibility

An AI workflow can answer one example correctly and fail on the next one. Looking at one successful result is not enough to know whether the workflow is working.

That is why we need evaluation. We can prepare examples that represent our work, check exact results when possible, and use human review when the answer needs judgment.

## Try this

Let's save ten analysis questions and write down what we expect from each answer. Run them again whenever we change the prompt, model, or tools.

## Resources

<!-- RESOURCE_LIST_START -->
| Resource | Type | Access | Practice | Level | Status |
|---|---|---|---|---|---|
| [MLflow GenAI Evaluation and Monitoring](https://mlflow.org/docs/latest/genai/eval-monitor/) | Official Documentation | Free | Hands-on | Intermediate | Active |
| [OpenAI Evals](https://github.com/openai/evals) | Tool | Free | Hands-on | Advanced | Active |
| [LangSmith Evaluation](https://docs.langchain.com/langsmith/evaluation) | Official Documentation | Paid or account required | Hands-on | Intermediate | Active |
| [DeepEval](https://deepeval.com/docs/getting-started) | Official Documentation | Free | Hands-on | Intermediate | Active |
| [Ragas](https://docs.ragas.io/en/stable/) | Official Documentation | Free | Hands-on | Intermediate | Active |
| [Promptfoo](https://www.promptfoo.dev/docs/intro/) | Official Documentation | Free | Hands-on | Intermediate | Active |
| [Evidently](https://docs.evidentlyai.com/introduction) | Official Documentation | Free | Hands-on | Intermediate | Active |
| [Arize Phoenix](https://arize.com/docs/phoenix/) | Official Documentation | Free | Hands-on | Intermediate | Active |
| [Giskard LLM Scan](https://legacy-docs.giskard.ai/en/stable/open_source/scan/scan_llm/index.html) | Tutorial | Free | Hands-on | Intermediate | Check compatibility |
| [Pydantic Evals](https://pydantic.dev/docs/ai/evals/evals/) | Official Documentation | Free | Hands-on | Intermediate | Active |
<!-- RESOURCE_LIST_END -->

The final answer might sound good even when the calculation is wrong. We should check the complete task, including the selected source, generated code, numerical result, citation, and explanation.

