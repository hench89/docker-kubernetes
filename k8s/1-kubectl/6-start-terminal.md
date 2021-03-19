# Start interactive terminal with pod


1. If doesnt exist, create a new deployment<br>
`kubectl create deployment mongo-depl --image=mongo`

2. Get the ID of the pod<br>
`kubectl get pods`

3. Run script to start bash application inside the container<br>
`kubectl exec -it <id> -- bin/bash`
