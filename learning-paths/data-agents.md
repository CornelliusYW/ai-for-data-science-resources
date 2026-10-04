# Build Data Agents

**Goal:** build an agent that completes a bounded data task while leaving a result we can inspect.

## 1. Learn repository-based agent work

We can begin with [Coding Agents and Context Engineering](../resources/coding-agents-and-context.md). Give an agent one small task, several constraints, and a clear verification step.

## 2. Build a narrow tool-using agent

Choose one framework from [Data Science Agents](../resources/data-science-agents.md). Give the agent read-only access to a small database or dataset. For the first project, two or three tools are enough.

## 3. Ground the task in business context

Write down the data grain, metric definitions, allowed data sources, and unresolved questions. Then, require the agent to show its plan before calling any tools.

## 4. Evaluate complete runs

Use [Evaluation and Reproducibility](../resources/evaluation-and-reproducibility.md). We should test the source selection, tool calls, calculations, and final claims, not only whether the final prose looks good.

**Capstone:** an analytical agent that answers ten known questions, records its traces, cites the data it uses, and asks for our review when a question is ambiguous.

