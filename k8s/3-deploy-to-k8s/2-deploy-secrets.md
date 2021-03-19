
# Deploy a Secret to Kubernetes and Pull and Image

Before kubernetes can pull an image and create/orchestrate a container, it nees to have access credentials. The below steps will help to set this up using the "dockerconfigjson" approach.

This approach is not very good engineering practice, because password is not encrypted. However, for beginner tutorial this is fine.

1. Log into container registry service and identify

    * login server
    * login username
    * login password

2. Create base64 encoded docker authentification config file (method from [github](https://github.com/docker/for-mac/issues/4100#issuecomment-562294425))

    * identify base64 encoded login string:<br>
    `echo -n 'USERNAME:PASSWORD' | base64`
    * insert registry + encoded string into config-template.json. 
    * make another base64 encoding of the updated file<br>
    `cat config.json | base64`

3. Create a dockerconfigjson Secret

    * using attached yaml template, insert secret name + base64 encoded json file into the yaml template

4. Create secret into kubernetes using command<br>
    `kubectl apply -f SECRETYAMLFILE`

5. Verify that secret has successfully been submitted to k8s<br>
`kubectl get secrets`
