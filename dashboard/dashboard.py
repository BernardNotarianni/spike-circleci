from bottle import route, run, template
from kubernetes import client, config


tpl = ''
with open('dashboard.tpl.html', 'r') as file:
    tpl = file.read()

@route('/')
def index():
    config.load_kube_config()
    v1 = client.CoreV1Api()
    all_services = v1.list_service_for_all_namespaces(watch=False)
    app_services = [s for s in all_services.items if s.metadata.namespace not in ['default', 'kube-system'] ]

    items = []
    for s in app_services:
        ip = s.status.load_balancer.ingress[0].ip
        namespace = s.metadata.namespace
        url = 'http://{}:8000'.format(ip)
        if 'issue' in namespace:
            [z, issue] = namespace.split('-')
            issue_url = 'https://github.com/BernardNotarianni/spike-circleci/issues/{}'.format(issue)
        else:
            issue_url = None
        items.append({'name': namespace, 'issue_url': issue_url, 'url': url})

    return template(tpl, items=items)

run(host='0.0.0.0', port=8000)

