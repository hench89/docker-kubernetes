# Edit a deployment 

Inspect the configuration of a deployment 
Edit configuration 
Check that pod is automatically restarted 
Check that replicaset is automatically updated 

Commands

* kubectl edit deployment nginx-depl
* <inside yaml file change container image from "nginx" to "nginx:1.16">
* kubectl get replicaset
* kubectl get pod
