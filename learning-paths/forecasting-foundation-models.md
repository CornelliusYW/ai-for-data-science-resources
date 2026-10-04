# Foundation Models for Forecasting

**Goal:** understand whether a pretrained time-series model improves our actual forecasting task.

## 1. Define the backtest

Before trying a foundation model, choose several forecast origins, the production horizon, the business metric, and a simple seasonal baseline.

## 2. Run two pretrained models

Choose two resources from [Time Series Foundation Models](../resources/time-series-foundation-models.md). Keep the input history and evaluation windows the same for both models.

## 3. Inspect failures

We can break down the result by horizon, series, intermittency, and business period. If the model provides prediction intervals, we should also check whether they are calibrated.

## 4. Plan the operating model

Use [MLOps and Production](../resources/mlops-and-production.md) to compare zero-shot inference, light adaptation, and an established local model. The most suitable choice depends on what our team can maintain.

**Capstone:** a rolling-backtest report with seasonal naive, one classical or tree-based method, and two foundation models.

