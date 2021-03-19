# Creating a pod 

Container(s) in k8s are run inside a pod. Pod is just an abstraction layer. Pods are created through another abstraction called Deployments, and inbetween is a thing called replicatsets

Abstraction layers: Deployment -> Replicaset -> Pod -> Container

In summary: containers are not managed directly, instead focus is on "deployments". Lets create one!

1. Create a new deployment for nginx<br>
`kubectl create deployment nginx-depl --image=nginx`

2. Check status of deployment<br>
`kubectl get deployment`

3. Check status of related replicaset<br>
`kubectl get replicaset`

4. Finally check pod is running<br>
`kubectl get pod`
