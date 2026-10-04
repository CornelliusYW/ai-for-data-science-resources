# Notebook to Production

A notebook can work well for exploration but become difficult to reuse. The goal of this path is to turn one notebook into a small system that another data professional can run and maintain.

## 1. Define the contract

First, write the input schema, output schema, data assumptions, metric, latency target, and failure behavior. We can use this information to explain the project to both people and coding agents.

## 2. Refactor the notebook

Next, use [Coding Agents and Context Engineering](../resources/coding-agents-and-context.md) to move repeated work into functions, configuration, and a small package. We can keep the notebook as an example or report, but it should not be the only way to run the project.

## 3. Add tests and evaluation data

Use [Evaluation and Reproducibility](../resources/evaluation-and-reproducibility.md). Test the fixed transformations directly and save representative examples for any behavior that depends on a model.

## 4. Package and deploy

Lastly, use [MLOps and Production](../resources/mlops-and-production.md) to add a command-line entry point or API, a container, CI, and basic monitoring. The final setup depends on how people need to use the project.

**Capstone:** a repository another person can clone, test, run, and review without executing notebook cells in a particular order.

