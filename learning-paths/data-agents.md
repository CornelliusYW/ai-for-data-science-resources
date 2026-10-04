# Build Data Agents

A data agent can complete several activities with Python, SQL, and other tools. The goal of this path is to build one for a small data task while keeping the result easy to inspect.

## 1. Learn repository-based agent work

Let's begin with [Coding Agents and Context Engineering](../resources/coding-agents-and-context.md). Give an agent one small task, several constraints, and a clear verification step.

## 2. Build a narrow tool-using agent

Choose one framework from [Data Science Agents](../resources/data-science-agents.md). Give the agent read-only access to a small database or dataset. For the first project, two or three tools are enough. We can add more tools after the basic workflow works.

## 3. Ground the task in business context

Write down the data grain, metric definitions, allowed data sources, and unresolved questions. Then, ask the agent to show its plan before calling any tools.

## 4. Evaluate complete runs

Use [Evaluation and Reproducibility](../resources/evaluation-and-reproducibility.md). The final prose might look good even when an earlier step is wrong. That is why we should test the source selection, tool calls, calculations, and final claims.

**Capstone:** an analytical agent that answers ten known questions, records its traces, cites the data it uses, and asks for our review when a question is ambiguous.

