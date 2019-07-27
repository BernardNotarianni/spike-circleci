BRANCH=$(git symbolic-ref --short HEAD)
TAG=$(echo $BRANCH| sed 's/\(dev-[0-9]*\).*/\1/')
NAMESPACE=$TAG

IP=$(kubectl get svc my-webapp -n$NAMESPACE -ojson | jq -r ".status.loadBalancer.ingress[0].ip")

URL="http://$IP:8000"

echo $URL
