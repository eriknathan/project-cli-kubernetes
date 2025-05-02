#!/usr/bin/env python3

from kubernetes import client, config
from kubernetes.client import V1Pod

config.load_kube_config()
v1 = client.CoreV1Api()

def get_pods_all_namespaces() -> list:
    return v1.list_pod_for_all_namespaces().items


def get_images_from_pod(pod: V1Pod) -> list:
    return [ container.image for container in pod.spec.containers ]


def main():
    for pod in get_pods_all_namespaces():
        print(f"name: {pod.metadata.name} | image: {get_images_from_pod(pod)}")


if __name__ == '__main__':
    main()
