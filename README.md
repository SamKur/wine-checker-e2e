# End to End Data Science Project

# Setup from your side

1. Clone the repository
2. Create a virtual environment (```python -m venv venv```) and activate it
3. Install the required packages (```pip install -r requirements.txt```)

### Workflows -- ML Pipeline

1. Data Ingestion
2. Data Validation
3. Data Transformation -- Feature Engineering, Data Preprocessing
4. Model Trainer
5. Model Evaluation -- MLflow, Dagshub

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py

# Repos

https://github.com/SamKur/wine-checker-e2e

https://dagshub.com/susamay.sk/wine-checker-e2e

https://dagshub.com/susamay.sk/wine-checker-e2e.mlflow

# Saving model & artifacts to AWS S3
Using AWS cli commands directly to sync files wrt S3 bucket
Requires AWS CLI installed and credentials configured (aws configure).
Uses aws s3 sync under the hood (good for big directories, handles diffs).

# AWS ECR (pushing docker image)
