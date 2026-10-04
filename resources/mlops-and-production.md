# MLOps and Production

A notebook that works on our machine is a good start, but it is not yet a production workflow. Another person should be able to run it, test it, and understand what happens when something fails.

We still need packaging, tests, data checks, deployment, traces, and monitoring. This does not change even when an agent helps us write the first version.

## Try this

Let's take one notebook that we want to reuse and turn it into a package. Add one command to run it, several tests, a container, and a small deployment target.

## Resources

<!-- RESOURCE_LIST_START -->
| Resource | Type | Access | Practice | Level | Status |
|---|---|---|---|---|---|
| [MLOps Zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) | GitHub Curriculum | Free | Hands-on | Intermediate | Active |
| [Made With ML](https://madewithml.com/) | Course | Free | Hands-on | Intermediate | Active |
| [Full Stack Deep Learning](https://fullstackdeeplearning.com/) | Course | Free | Hands-on | Intermediate | Active |
| [MLflow for GenAI](https://mlflow.org/docs/latest/genai/) | Official Documentation | Free | Hands-on | Intermediate | Active |
| [BentoML LLM Guides](https://docs.bentoml.com/en/latest/examples/overview.html) | Official Documentation | Free | Hands-on | Advanced | Active |
| [Ray Serve LLM](https://docs.ray.io/en/latest/serve/llm/index.html) | Official Documentation | Free | Hands-on | Advanced | Active |
| [Docker Model Runner](https://docs.docker.com/ai/model-runner/) | Guide | Free | Hands-on | Beginner | Active |
| [Modal Guide](https://modal.com/docs/guide) | Official Documentation | Paid or account required | Hands-on | Intermediate | Active |
<!-- RESOURCE_LIST_END -->

For me, the best production path is often the smallest one that solves the problem. For example, a scheduled batch job might be enough. We do not always need an agent service that keeps running.

