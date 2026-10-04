# Tabular Foundation Models

A tabular foundation model is a pretrained model we can use for classification or regression data. Instead of training everything from the beginning, we can use the existing model to create a result.

The method gives us another baseline, especially for a smaller dataset. However, we still need to compare it with gradient-boosted trees and our existing feature process.

## Try this

Let's use a tabular foundation model on one small classification dataset. Then, compare the result with CatBoost or XGBoost using the same split and metric.

## Resources

<!-- RESOURCE_LIST_START -->
| Resource | Type | Access | Practice | Level | Status |
|---|---|---|---|---|---|
| [TabPFN](https://github.com/PriorLabs/TabPFN) | Tool | Free | Hands-on | Intermediate | Active |
| [TabPFN Extensions](https://github.com/PriorLabs/tabpfn-extensions) | Notebook Collection | Free | Hands-on | Advanced | Active |
| [Prior Labs TabPFN Documentation](https://docs.priorlabs.ai/overview) | Official Documentation | Free | Hands-on | Beginner | Active |
| [TabICL](https://github.com/soda-inria/tabicl) | Tool | Free | Hands-on | Advanced | Active |
| [TICL](https://github.com/microsoft/ticl) | Tool | Free | Hands-on | Advanced | Check compatibility |
| [PyTabKit](https://github.com/dholzmueller/pytabkit) | Tool | Free | Hands-on | Advanced | Active |
<!-- RESOURCE_LIST_END -->

Accuracy is not the only result we need to check. We can also compare calibration, runtime, memory, and what is required to deploy the model. The best choice depends on what we need.

