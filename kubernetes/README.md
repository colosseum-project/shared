# Deploy on Kubernetes

- [Deploy on Kubernetes](#deploy-on-kubernetes)
  - [Create the K8s cluster](#create-the-k8s-cluster)
  - [Deploy the applicaton](#deploy-the-applicaton)
  - [Clean everything up](#clean-everything-up)

## Create the K8s cluster

Here, we use [`kind`](https://kind.sigs.k8s.io/) to deploy our K8s sandbox environment on Docker.

Use this command to create the cluster:

```sh
kind create cluster --config ./kind_config.yaml
```

## Deploy the applicaton

To deploy the application inside the cluster, run:

```sh
kubectl apply -f ./resources
```

After a short moment, the Bisselium WebUI interface can be accessed via <http://127.0.0.1:30000/>.

The Ludus endpoint is also accessible via <http://127.0.0.1:30001/>. _This allows you to manage gladiators and engage them in combats._

Add gladiators by running this Python script:

```sh
python ./api/add_random_gladiators/main.py 127.0.0.1 -p 30001
```

Engage random duels with this cURL command:

```sh
curl -X POST http://127.0.0.1:30001/duels/resolve/random
```

## Clean everything up

Once you are done, you can remove the cluster with this single command:

```sh
kind delete cluster colosseum-project
```

---

Have fun! :)
