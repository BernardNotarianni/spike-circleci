export TAG=$1
export NAMESPACE=$2

echo ${GCLOUD_SERVICE_KEY} > gcp-key.json
gcloud auth activate-service-account --key-file gcp-key.json
gcloud --quiet config set project ${GOOGLE_PROJECT_ID}
gcloud --quiet config set compute/zone ${GOOGLE_COMPUTE_ZONE}
gcloud --quiet container clusters get-credentials ${GOOGLE_CLUSTER_NAME}

envsubst < k8s_template.yml > patched_k8s.yml

kubectl apply -f patched_k8s.yml
kubectl rollout status deployment/my-webapp -n ${NAMESPACE}
