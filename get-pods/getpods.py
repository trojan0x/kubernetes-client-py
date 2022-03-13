from kubernetes import client, config

config.load_kube_config()

v1 = client.CoreV1Api()

all_pod = v1.list_pod_for_all_namespaces(watch=False)

for i in all_pod.items:
    print( "%s\t%s\t%s" %(i.status.pod_ip, i.metadata.namespace i.metadata.name))
