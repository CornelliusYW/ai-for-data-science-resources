# Time Series Foundation Models

Time series foundation models allow us to create a forecast without training a model from scratch. They give us a zero-shot result to compare. However, we still need time-based backtesting and a simple seasonal baseline to understand whether the model improves the forecast.

## Try this

Run a zero-shot forecast on one business series. Compare the result with a seasonal naive baseline using several rolling backtests.

## Resources

<!-- RESOURCE_LIST_START -->
| Resource | Type | Access | Practice | Level | Status |
|---|---|---|---|---|---|
| [TimesFM](https://github.com/google-research/timesfm) | Tool | Free | Hands-on | Advanced | Active |
| [Chronos Forecasting](https://github.com/amazon-science/chronos-forecasting) | Tool | Free | Hands-on | Advanced | Active |
| [Uni2TS and Moirai](https://github.com/SalesforceAIResearch/uni2ts) | Tool | Free | Hands-on | Advanced | Active |
| [Lag-Llama](https://github.com/time-series-foundation-models/lag-llama) | Tool | Free | Hands-on | Advanced | Check compatibility |
| [Production Forecasting with TimeGPT and Polars](https://www.nixtla.io/blog/production-ready-forecasting-pipeline-with-timegpt-and-polars) | Tutorial | Paid or account required | Hands-on | Beginner | Active |
| [MOMENT](https://github.com/moment-timeseries-foundation-model/moment) | Tool | Free | Hands-on | Advanced | Active |
| [Granite Time Series Foundation Models](https://github.com/ibm-granite/granite-tsfm) | Tool | Free | Hands-on | Advanced | Active |
<!-- RESOURCE_LIST_END -->

We should evaluate several forecast origins. A single train-test split might hide failures that only appear in another season or business period.

