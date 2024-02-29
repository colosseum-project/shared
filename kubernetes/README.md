# Deploy on Kubernetes

Here, we use [`kind`](https://kind.sigs.k8s.io/) to deploy our K8s sandbox environment on Docker.

Use this command to create the `kind` cluster:

```sh
kind create cluster --config ./kind_config.yaml
```

To deploy the application inside the cluster, run:

```sh
kubectl apply -f ./resources
```

After a short moment, the Bisselium WebUI interface can be accessed via <http://127.0.0.1:30000/>.

The Ludus endpoint is also accessible via <http://127.0.0.1:30001/>. This allows you to manage gladiators and engage combats.

Once you are done, you can remove the cluster with this single command:

```sh
kind delete cluster colosseum-project
```

Have fun! :)
