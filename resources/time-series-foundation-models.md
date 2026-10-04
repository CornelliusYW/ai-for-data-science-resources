# Time Series Foundation Models

A time series foundation model is a pretrained model we can use to create a forecast without training it from scratch. This gives us a zero-shot result that we can compare with our current method.

However, one forecast is not enough to show that the model is better. We still need time-based backtesting and a simple seasonal baseline.

## Try this

Let's run a zero-shot forecast on one business series. Compare the result with a seasonal naive baseline using several rolling backtests.

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

Evaluate several forecast origins. A single train-test split might hide a failure that only appears in another season or business period.

