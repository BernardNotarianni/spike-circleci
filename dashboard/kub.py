from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

v1 = client.CoreV1Api()
print("Listing services with their IPs:")
services = v1.list_service_for_all_namespaces(watch=False)

app_services = [s for s in services.items if s.metadata.namespace not in ['default', 'kube-system'] ]
for s in app_services:
    ip = s.status.load_balancer.ingress[0].ip
    namespace = s.metadata.namespace
    print("%s\thttp://%s:8000" % (namespace, ip))
