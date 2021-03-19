# Working inside a Namespace

Create a new deployment inside default namespace

1. Create a new deployment for nginx<br>
`kubectl create deployment nginx-default-depl --image=nginx`

2. Finally check pod is running<br>
`kubectl get pod`

Create a new namespace

3. Create new namespace<br>
`kubectl create namespace my-ns`
4. Verify that it was created <br>
`kubectl get namespaces`


Change namespace using kubens

5. Install [kubectx](https://github.com/ahmetb/kubectx) which incudes kubens+kubectx command. In linux run<br>
`sudo apt install kubectx`

6. Change namespace to the newly created one<br>
`kubens my-ns`

7. Check that new deployed pod is no available in new namespace<br>
`kubectl get pod`

8. Change back to default namespace<br>
`kubens default`
