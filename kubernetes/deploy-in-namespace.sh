NAMESPACE=dev-1

sed "s/___NAMESPACE___/$NAMESPACE/g" k8s_template.yml > k8s.yml

kubectl apply -f k8s.yml
