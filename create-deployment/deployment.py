
from os import path
import yaml
from kubernetes import client, config

config.load_kube_config()

with open(path.join(path.dirname(__file__), "deploy_nginx.yaml")) as f:
    deploy = yaml.safe_load(f)

    k8s_v1 = client.AppsV1Api()

    resp = k8s_v1.create_namespaced_deployment(
        body=deploy,
        namespace="default"
    )

print("Your deployment was created. Status = '%s' " % resp.metadate.name)