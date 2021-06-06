# Execute this command in main-cloud-run folder
# Set Environment Variables
GOOGLE_CLOUD_PROJECT=sapaai

# Build Container of main-cloud-run API
gcloud builds submit --tag gcr.io/$GOOGLE_CLOUD_PROJECT/main-cloud-run

# Deploy cloud run main-cloud-run
gcloud beta run deploy main-cloud-run \
  --image gcr.io/$GOOGLE_CLOUD_PROJECT/main-cloud-run \
  --platform managed \
  --no-allow-unauthenticated