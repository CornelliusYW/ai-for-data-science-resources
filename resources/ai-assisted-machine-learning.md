# AI-Assisted Machine Learning

Machine learning development contains many repeated activities. We prepare the data, train several models, compare the metrics, and record the experiment.

AI and AutoML can help us complete some of this work. However, they do not decide the correct validation design, leakage rule, fairness requirement, or cost for our problem.

## Try this

Let's run one AutoML baseline beside our current model. Compare the accuracy, runtime, leakage risk, and interpretability. A higher score is nice, but it does not always mean the model is better for our work.

## Resources

<!-- RESOURCE_LIST_START -->
| Resource | Type | Access | Practice | Level | Status |
|---|---|---|---|---|---|
| [AutoGluon Tabular Tutorials](https://auto.gluon.ai/stable/tutorials/tabular/index.html) | Tutorial | Free | Hands-on | Beginner | Active |
| [FLAML Task-Oriented AutoML](https://microsoft.github.io/FLAML/docs/Use-Cases/Task-Oriented-AutoML/) | Official Documentation | Free | Hands-on | Intermediate | Active |
| [H2O AutoML](https://docs.h2o.ai/h2o/latest-stable/h2o-docs/automl.html) | Official Documentation | Free | Hands-on | Intermediate | Active |
| [PyCaret Tutorials](https://pycaret.gitbook.io/docs/get-started/tutorials) | Tutorial | Free | Hands-on | Beginner | Active |
| [Azure Machine Learning Automated ML](https://learn.microsoft.com/en-us/azure/machine-learning/concept-automated-ml?view=azureml-api-2) | Official Documentation | Paid or account required | Hands-on | Intermediate | Active |
| [Google Cloud Tabular Workflows](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tabular-data/tabular-workflows/overview) | Official Documentation | Paid or account required | Hands-on | Intermediate | Active |
| [MLJAR AutoML Documentation](https://supervised.mljar.com/) | Official Documentation | Free | Hands-on | Beginner | Active |
<!-- RESOURCE_LIST_END -->

Use the same data split and metric for every model. Otherwise, we might get an impressive leaderboard without knowing whether the comparison is fair.

