# Edit a deployment 

Now we will make a change to a running deployment

1. Inspect the configuration of a deployment<br>
`kubectl edit deployment nginx-depl`

2. Edit configuration by changing the yaml file. Change container image from "image: nginx" to "image: nginx:1.16". Save the file.

3. Check that configuration change impacts the related replicaset(s)<br>
`kubectl get replicaset`

4. Check pod status to see that it is updated<br>
`kubectl get pod`
