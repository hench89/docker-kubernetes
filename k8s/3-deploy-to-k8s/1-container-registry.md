# Container Registry

Kubernetes needs to pull container images from different container registries. Setting up a container registry can be done easily at different cloud providers, including Amazon AWS, Google Cloud and Microsoft Azure.


Finding a registry in Microsoft Azure Portal

1. Go to [azure portal](portal.azure.com)
2. Search for the azure service [Container Registries](https://portal.azure.com/#blade/HubsExtension/BrowseResource/resourceType/Microsoft.ContainerRegistry%2Fregistries)
3. If one is available to you it will be shown in the list. Alternatively you will need to create a new one.


Push an image to an Azure Container Registry

4. Use Azure CLI to log into Azure Portal using below command <br>
`az acr login --name REGISTRY_NAME --subscription SUBSCRIPTION`

5. Use below docker commands to push image to Azure Container Registry<br>
`docker tag IMAGE_NAME_AND_TAG REMOTE_IMAGE_NAME_AND_TAG`<br>
`docker push REMOTE_IMAGE_NAME_AND_TAG`
