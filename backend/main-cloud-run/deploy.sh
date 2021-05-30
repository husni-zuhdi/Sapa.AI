# Build Container of front-panick API
gcloud builds submit \
  --tag gcr.io/$GOOGLE_CLOUD_PROJECT/front-panick

# Deploy cloud run front-panick
gcloud beta run deploy front-panick \
  --image gcr.io/$GOOGLE_CLOUD_PROJECT/front-panick \
  --platform managed \
  --region asia-southeast-1 \
  --no-allow-unauthenticated