# Set environment
gcloud config set project sapaai
PROJECT_ID=$(gcloud config list project --format "value(core.project)")

#when launching wordpress from the marketplace, the vm instance will automatically have the following syntax.
gcloud beta compute ssh --zone "asia-southeast1-a" "sapaai-dashboard-1-vm"  --project "sapaai"

# Change mysql password for wordpress
# click SSH button and type
mysqladmin -u root -p <your-password>

# and then login wp-admin 