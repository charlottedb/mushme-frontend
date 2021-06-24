# Deployment

```bash
docker build . -t eu.gcr.io/wagon-bootcmap/mush-me
docker push eu.gcr.io/wagon-bootcmap/mush-me
gcloud run deploy mush-me --image=eu.gcr.io/wagon-bootcmap/mush-me

```