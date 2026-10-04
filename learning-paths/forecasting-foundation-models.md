# Foundation Models for Forecasting

A pretrained time-series model can create a forecast without training from scratch. The goal of this path is to check whether that forecast improves our actual task.

## 1. Define the backtest

Before trying the foundation model, choose several forecast origins, the production horizon, the business metric, and a simple seasonal baseline. We need these first so the comparison has a clear meaning.

## 2. Run two pretrained models

Let's choose two resources from [Time Series Foundation Models](../resources/time-series-foundation-models.md). Keep the input history and evaluation windows the same for both models.

## 3. Inspect failures

Look at the result by horizon, series, intermittency, and business period. For example, a model might work well for a short horizon but fail when we forecast further ahead. If the model provides prediction intervals, we should also check their calibration.

## 4. Plan the operating model

Lastly, use [MLOps and Production](../resources/mlops-and-production.md) to compare zero-shot inference, light adaptation, and an established local model. The most suitable choice depends on what our team can maintain.

**Capstone:** a rolling-backtest report with seasonal naive, one classical or tree-based method, and two foundation models.

