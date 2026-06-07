
# Curated links

Instead of restating docs, storing any links with useful documentation. 

## Dev workflows

- [Databricks extension for VS Code](https://docs.databricks.com/dev-tools/vscode-ext/index.html) — local editing, run-on-cluster, debugging.
- [Databricks Connect](https://docs.databricks.com/dev-tools/databricks-connect/index.html) — run Spark code locally against a remote cluster.
- [Authentication (OAuth / profiles)](https://docs.databricks.com/dev-tools/auth/index.html) — how the CLI/extension authenticate; profiles vs OAuth.

## MLOps architecture

- [Big Book of MLOps](https://www.databricks.com/resources/ebook/the-big-book-of-mlops) — Databricks' reference framing; the source of deploy-code vs deploy-model.
- [MLOps on Databricks (recommended architecture)](https://docs.databricks.com/machine-learning/mlops/mlops-workflow.html) — the canonical reference workflow.

## Asset Bundles (notebook 02)

- [Databricks Asset Bundles](https://docs.databricks.com/dev-tools/bundles/index.html) — what bundles are and the project layout.
- [Bundle configuration reference](https://docs.databricks.com/dev-tools/bundles/settings.html) — every `databricks.yml` key; the schema CI validates against.
- [Bundle deployment modes](https://docs.databricks.com/dev-tools/bundles/deployment-modes.html) — development vs production mode behavior.

## Config & secrets

- [OmegaConf docs](https://omegaconf.readthedocs.io/) — interpolation, merging, structured configs.
- [Databricks widgets](https://docs.databricks.com/notebooks/widgets.html) — UI/job parameters for notebooks.
- [Secret management](https://docs.databricks.com/security/secrets/index.html) — secret scopes; never hardcode credentials.

## Unity Catalog & MLflow

- [Unity Catalog](https://docs.databricks.com/data-governance/unity-catalog/index.html) — the three-level namespace and governance model.
- [Models in Unity Catalog](https://docs.databricks.com/machine-learning/manage-model-lifecycle/index.html) — registry, versions, aliases.
- [MLflow Tracking](https://mlflow.org/docs/latest/tracking.html) — runs, params, metrics, artifacts.
- [MLflow model signatures](https://mlflow.org/docs/latest/model/signatures.html) — why signatures + input examples matter for serving.

## Monitoring
- [Lakehouse Monitoring](https://docs.databricks.com/lakehouse-monitoring/index.html) — drift/quality monitors on tables and inference logs.
- [Inference tables](https://docs.databricks.com/machine-learning/model-serving/inference-tables.html) — auto-logging serving requests/responses for monitoring.

## Agents & Vector Search
- [Genie](https://docs.databricks.com/genie/index.html) - Agent connected directly to your data. Primarily SQL based. 
- [AI agents / Mosaic Agent Framework](https://docs.databricks.com/generative-ai/agent-framework/build-genai-apps.html) — building and deploying custom agents.
- [Vector Search](https://docs.databricks.com/generative-ai/vector-search.html) - delta-sync vs direct-access indexes for retrieval/RAG.
- [Model Serving](https://docs.databricks.com/machine-learning/model-serving/index.html) - how agents and models are deployed behind endpoints.
- [LangChain Databricks Integration](https://docs.langchain.com/oss/python/integrations/providers/databricks) - using LangChain/Langgraph in Databricks
- [LangGraph Tracing](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/langgraph) - Insights into LangGraph execution