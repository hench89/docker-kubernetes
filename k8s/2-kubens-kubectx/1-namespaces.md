# Namespaces in k8s

In k8s, resources can be organised in namespaces. It works like a virtual cluster, inside a cluster. 

Namespaces ...
* ... are great for grouping of resources, e.g.: database/monitoring/networking, staging (test/preprod/prod)
* ... prevents naming conflicts for applications
* ... should not be used for small projects and less than 10 users
* ... can be used for green/blue deployment ("swapping" old services/servers with new one)

## Check Existing Namespaces

1. Check available namespaces<br>
`kubectl get namespaces`<br>

    by defalt there should be three system specific ones we dont really care about:

    * "kube-system": components for system processed<br>
    * "kube-public": public accessible data<br>
    * "kube-node-lease": node specific information
    <br>

    finally there is "default", which can be used for running personal resources. 

