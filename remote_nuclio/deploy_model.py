import os
from mlrun import set_environment, code_to_function, mount_v3io
import v3io.dataplane
import pandas as pd
import requests
import json
from dotenv import load_dotenv


def push_to_v3io(v3io_client, local_file, remote_file):
    print(f"Pushing '{local_file}' to '{remote_file}'")
    with open(local_file, "rb") as f:
        v3io_client.object.put(container="users", path=remote_file, body=f.read())


def test_inference(addr):
    print("Testing inference")
    X_test = pd.read_csv("assets/X_test.csv").set_index("patient_id")
    payload = json.dumps({"inputs": X_test[0:5].values.tolist()})
    response = requests.post(addr, json=payload)
    predictions = response.json()
    print(predictions)


def main():
    # Load environment variables
    load_dotenv()

    # Setup project
    project_name, artifact_path = set_environment(
        project="remote-model-deployment",
        artifact_path=os.getenv("MLRUN_ARTIFACT_PATH"),
        api_path=os.getenv("MLRUN_DBPATH"),
        access_key=os.getenv("V3IO_ACCESS_KEY"),
    )
    print(f"Creating project '{project_name}'")

    # Push assets to V3IO
    v3io_client = v3io.dataplane.Client()
    push_to_v3io(v3io_client, "assets/model.pkl", "nick/tmp/model.pkl")

    # Create MLRun function
    serving_fn = code_to_function(
        name="serving",
        kind="serving",
        image="mlrun/mlrun",
        filename="assets/model_server.py",
    ).apply(mount_v3io())
    print(f"Creating function '{serving_fn.metadata.name}'")

    # Configure MLRun function
    serving_fn.spec.default_class = "ClassifierModel"
    serving_fn.add_model("my_model", model_path="/User/tmp/model.pkl")

    # Deploy
    addr = serving_fn.deploy()

    # Test model inference
    test_inference(addr)


if __name__ == "__main__":
    main()