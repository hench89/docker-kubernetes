# Create Deployment

We will now create a deployment of the docker image and access it, running on the kubernetes cluster.

1. Specify a new job or deployment to run the container, using attached yaml file. Pay special attention to these fields:
    * "continers image": tell k8s where to fetch image (login server url)
    * "imagePullSecrets": reference to name of a secret in namespace

2. Run command to apply new job<br>
`kubectl apply -f YAMLFILE`

3. Verify that job is created and running<br>
`watch -n1 "kubectl get all"`

4. Access your pod, using [port-forwarding](https://phoenixnap.com/kb/kubectl-port-forward)<br>
    * Set up port forwarding<br>
    `kubectl port-forward pod/PODNAME LOCALPORT:REMOTEPORT`
    * Access http://localhost:REMOTEPORT
