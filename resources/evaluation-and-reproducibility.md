# Evaluation and Reproducibility

An AI workflow might work well for one example and fail on the next one. That is why we need evaluation. We can use representative examples, deterministic checks where possible, and human review when the result needs judgment.

## Try this

Save ten representative analysis questions and write down what we expect from each answer. Rerun them whenever we change the prompt, model, or tools.

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

We should evaluate the complete task, not only whether the final answer sounds good. For data work, this means checking the selected source, generated code, numerical result, citation, and explanation.

