# Enable Kubernetes

* Install docker-desktop from https://www.docker.com/get-started
* Open setting > Kubernetes > Enable Kubernetes
* Click Apply & Restart - wait a few minutes


## Troubleshooting

If Kubernetes in windows docker desktop will not start, try below tips based on https://github.com/docker/for-mac/issues/5027.

* check file type of C:\Windows\System32\drivers\etc\hosts. run `file -i hosts` and very that charset is ascii and not utf-8 or binary. it must be ascii based
* try to delete pki folder in AppData\Local\Docker\
