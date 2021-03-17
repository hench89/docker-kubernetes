# Using Deployment Configuration files

## Create new Deployment

1. Create a deployment configuration file. Sample available from [kubernetes.io](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)

2. Run apply command<br>
`kubectl apply -f 8-nginx-deployment.yaml`

3. Verify that pod is created<br>
`kubectl get pods`

## Update Deployment

4. Open deployment file and change replicas from 1 to 2. Save file
5. Apply the file again<br>
`kubectl apply -f 8-nginx-deployment.yaml`
6. Verify that k8s "configured" the deployment instead of creating a new one.
7. Check updated number of pods<br>
`kubectl get pods`
