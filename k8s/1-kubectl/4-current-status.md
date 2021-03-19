# Check what's going on with a pod 

1. Create a new deployment for mongodb<br>
`kubectl create deployment mongo-depl --image=mongo`

2. Check status of pods to get the id<br>
`kubectl get pods`

3. Describe pod to see all relevant information<br>
`kubectl describe pod <id>`
