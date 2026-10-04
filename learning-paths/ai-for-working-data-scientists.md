# AI for Working Data Scientists

AI can help with our current data work without requiring us to rebuild the whole workflow. The goal of this path is to try it one activity at a time and check the result at every step.

## 1. Start with one analysis task

Let's start with a dataset that we already understand and work through [AI-Assisted Analysis and SQL](../resources/ai-assisted-analysis-and-sql.md). Ask for an analysis plan before any code. Then, compare the result with an analysis we already trust.

**Output:** one reviewed notebook that contains the prompts, generated code, our corrections, and the final conclusion.

## 2. Add repository context

Next, we can try [Coding Agents and Context Engineering](../resources/coding-agents-and-context.md). Record the project commands, data boundaries, metric definitions, and expected checks inside the repository.

**Output:** `AGENTS.md` plus a short prediction or analysis contract.

## 3. Compare an ML baseline

Use [AI-Assisted Machine Learning](../resources/ai-assisted-machine-learning.md) to create one automated baseline. However, keep the split, metric, and leakage rules the same as the current model. This way, we can see whether the new method actually improves the result.

**Output:** a comparison table with accuracy, runtime, interpretability, and operational cost.

## 4. Save a regression set

Lastly, use [Evaluation and Reproducibility](../resources/evaluation-and-reproducibility.md) to save representative questions and what we expect from each answer.

**Output:** ten examples that can be rerun after changing the model, prompt, or tools.

