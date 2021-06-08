import os
import googleapiclient.discovery
from google.api_core.client_options import ClientOptions

def predict_json(instances, version=None):
    """Send json data to a deployed model for prediction.

    Args:
        project (str): project where the Cloud ML Engine Model is deployed.
        region (str): regional endpoint to use; set to None for ml.googleapis.com
        model (str): model name.
        instances ([Mapping[str: Any]]): Keys should be the names of Tensors
            your deployed model expects as inputs. Values should be datatypes
            convertible to Tensors, or (potentially nested) lists of datatypes
            convertible to tensors.
        version: str, version of the model to target.
    Returns:
        Mapping[str: any]: dictionary of prediction results defined by the
            model.
    """

    # Set service account ml_predict_req key
    os.environ['GOOGLE_APPLICATION_CREDENTIALS']="key.json"

    # Create the ML Engine service object.
    api_endpoint = "https://asia-southeast1-ml.googleapis.com"
    client_options = ClientOptions(api_endpoint=api_endpoint)
    service = googleapiclient.discovery.build(
        'ml', 'v1', client_options=client_options)
    name = "projects/sapaai/models/multiclass"

    if version is not None:
        name += '/versions/{}'.format(version)


    response = service.projects().predict(
        name=name,
        body={'instances': instances}
    ).execute()

    if 'error' in response:
        raise RuntimeError(response['error'])

    for i in range(len(response['predictions'][0])):
        if response['predictions'][0][i] >= 0.15:
            response['predictions'][0][i] = True
        else:
            response['predictions'][0][i] = False

    return response['predictions']


# Test Object
# from ml import predict_json
# instances=["saya anak yang baik tetapi sering dipukuli paman saya karena selalu menolak ketika diajak bekerja di pasar"]
# version="v3"
# test = predict_json(instances, version)
# print(test)
