# preparation
gcloud auth login
gcloud config set project PROJECT_ID

# Start testing with the gcloud CLI (firebase)
gcloud firebase test android models list
gcloud firebase test android models describe Nexus5
gcloud firebase test android versions list
gcloud firebase test android locales list

# Running tests
gcloud firebase test android run \
  --type robo \
  --app app-debug-unaligned.apk \
  --device model=Nexus6,version=21,locale=en,orientation=portrait  \
  --device model=Nexus7,version=19,locale=fr,orientation=landscape \
  --timeout 90s

# Running the Robo test
gcloud firebase test android run \
  --type instrumentation \
  --app app-debug-unaligned.apk \
  --test app-debug-test-unaligned.apk \
  --device model=Nexus6,version=21,locale=en,orientation=portrait  \
  --device model=Nexus7,version=19,locale=fr,orientation=landscape

# Running your instrumentation tests
gcloud firebase test android run \
  --type instrumentation \
  --app your-app.apk \
  --test your-app-test.apk \
  --device model=TestDevice,version=AndroidVersion  \
  --environment-variables coverage=true,coverageFile="/sdcard/coverage.ec" \
  --directories-to-pull /sdcard