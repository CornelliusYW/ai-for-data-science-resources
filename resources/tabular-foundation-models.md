# Tabular Foundation Models

Tabular foundation models allow us to use a pretrained model for classification or regression. They give us another baseline, especially for smaller datasets. However, we should still compare them with gradient-boosted trees and our existing feature process.

## Try this

Use a tabular foundation model as the first baseline for one small classification dataset. Then, compare the result with CatBoost or XGBoost using the same split and metric.

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

The comparison should not stop at predictive performance. We can also compare calibration, runtime, memory, and deployment requirements. It depends on what we need from the model.

