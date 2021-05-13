# Iguazio Onboarding Basic Demo

### Examples
1. `mlrun_example.ipynb` - Runs `mlrun_fn.py` on K8s cluster with input parameters and logs value for experiment tracking
2. `mlrun_mount_example.ipynb` - Runs `mlrun_mount_fn` on K8s cluster with input parameters and custom Python module mounted within container
3. `nuclio_example.ipynb` - Deploys `nuclio_fn` on K8s cluster as a serverless function for real-time "inference"

### Documentation
- Iguazio: https://www.iguazio.com/docs/latest-release/
    - Platform docs regarding Iguazio itself and V3IO data layer
- MLRun: https://docs.mlrun.org/en/latest/
    - MLRun open source / platform docs
- Nuclio: https://nuclio.io/
    - Nuclio open source / platform docs
- V3IO-py: https://github.com/v3io/v3io-py
    - Python SDK for V3IO data layer

### End-to-End Example
- MNIST Demo:  https://github.com/igz-us-sales/igz-mnist-demo
    - Demo we will be covering today regarding converting a Python script into an operational pipeline
- MLRun Demos: https://github.com/mlrun/demos
    - Includes end-to-end demos for real-time, pipelines, distributed training, and more