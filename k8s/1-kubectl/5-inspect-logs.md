# Inspect logs of a pod 

1. If doesnt exist, create a new deployment<br>
`kubectl create deployment mongo-depl --image=mongo`

2. Get the ID of the pod<br>
`kubectl get pods`

3. Run command to get the logs
`kubectl logs <id>`
