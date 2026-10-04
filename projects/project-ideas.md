# Project Ideas to Try

Reading a tutorial helps us understand the idea, but an actual project shows us what happens with the method. For example, we can find where the output is wrong, which step takes the most time, and what still needs a person to review it.

The projects below are small enough to finish while still showing us where AI helps and where it fails.

## 1. Analysis copilot with a metric contract

Give a read-only SQL agent a small warehouse schema and written definitions for five metrics. Then, build twenty questions that include ambiguous wording, invalid joins, and unsupported requests.

**What we review:** SQL correctness, source selection, handling of ambiguity, numerical accuracy, and trace quality.

## 2. Document-to-dataset pipeline

Extract the same fields from 50 invoices, reports, or forms into a typed schema. We should keep the source span for each value and send every validation failure to a review file.

**What we review:** field accuracy, missing-value handling, provenance, cost, and the time saved after manual correction.

## 3. AutoML versus a careful baseline

Use one medium-sized tabular dataset. We can compare a simple linear model, a tuned tree ensemble, and two AutoML systems under the same time budget.

**What we review:** validation design, leakage, score, runtime, calibration, interpretability, and reproducibility.

## 4. Tabular foundation model benchmark

Compare TabPFN or TabICL with CatBoost and AutoGluon on three small datasets. However, we should not tune any model on the final test set.

**What we review:** performance by dataset size, inference cost, memory, calibration, and failure modes.

## 5. Notebook refactoring with a coding agent

Choose a notebook with repeated preprocessing and plotting. Ask an agent to create reusable functions, configuration, tests, and one command that reproduces the result.

**What we review:** the code difference, test coverage, result parity, documentation, and whether the new structure is easier to change.

## 6. Bounded data science agent

Build an agent that profiles a dataset, proposes three questions, runs approved analyses, and writes a short report. We can require a human approval step between the plan and execution.

**What we review:** plan quality, tool selection, calculation accuracy, unsupported claims, and whether the final report answers the original question.

## 7. Evaluation set for analytical answers

Create 25 questions for one dataset we understand. Store the expected numbers where possible and write simple criteria for explanations, charts, and citations.

**What we review:** coverage of realistic tasks, evaluator consistency, regression detection, and the effort needed for review.

## 8. Zero-shot forecasting comparison

Run at least two time-series foundation models against a seasonal naive model and a local statistical model. Use rolling backtests so we can compare several forecast periods.

**What we review:** accuracy by horizon, runtime, interval coverage, operational complexity, and stability across the series.

