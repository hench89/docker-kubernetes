# Delete a pod 

1. Find deployment to terminate<br>
`kubectl get deployment`

2. Delete specific deployment<br>
`kubectl delete deployment mongo-depl`

3. Check pod and replicaset to verify the change<br>
`kubectl get replicaset`<br>
`kubectl get pod`
