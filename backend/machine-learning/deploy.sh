# Set environment
PROJECT_ID=$(gcloud config list project --format "value(core.project)")
REGION=asia-southeast1
MODEL_BUCKET=gs://sapaai-bucket/backend/multi-class-model-3

# Test local predict
gcloud ai-platform local predict --model-dir gs://sapaai-bucket/backend/multi-class-model-3 \
  --json-instances gs://sapaai-bucket/backend/test/test.json \
  --framework tensorflow

# Deploy machine learning model
MODEL_DIR="gs://sapaai-bucket/backend/multi-class-model-3"
VERSION_NAME="v3"
MODEL_NAME="multiclass"
FRAMEWORK="tensorflow"
gcloud ai-platform versions create $VERSION_NAME \
  --model=$MODEL_NAME \
  --origin=$MODEL_DIR \
  --runtime-version=2.4 \
  --framework=$FRAMEWORK \
  --python-version=3.7 \
  --region=REGION \
  --machine-type="n1-standard-4"
