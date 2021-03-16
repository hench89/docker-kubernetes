# Inspect logs of a pod 

Create a new deployment 
Check pods to find pod id 
Use pod id to inspect logs 

Commands

* kubectl create deployment mongo-depl --image=mongo
* kubectl get pods
* kubectl logs mongo-depl-5fd6b7d4b4-txf7z
