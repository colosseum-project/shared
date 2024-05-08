# Deploy on Kubernetes

- [Deploy on Kubernetes](#deploy-on-kubernetes)
  - [Create the K8s cluster](#create-the-k8s-cluster)
  - [Deploy the application](#deploy-the-application)
    - [Host application database](#host-application-database)
    - [Deploy application stack](#deploy-application-stack)
  - [Clean everything up](#clean-everything-up)

## Create the K8s cluster

Here, we use [kind](https://kind.sigs.k8s.io/) to deploy our K8s sandbox environment in Docker.

Use this command to create the cluster:

```sh
kind create cluster --config ./kind_config.yaml
```

Follow this documentation to set Contour as ingress controller: <https://kind.sigs.k8s.io/docs/user/ingress/#contour>

## Deploy the application

### Host application database

Before, ensure you already have a database instance to host the application database.

Although the application supports several DBMS, we will use a MariaDB database server for this example.

### Deploy application stack

To deploy the Colosseum application stack inside the cluster, we use [kustomize](https://kustomize.io/), which is integrated to `kubectl`.

Create your `kustomization.yaml`, which defines your kustomize configuration:

```sh
mkdir -p .env
cat <<EOF >./.env/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
- ../manifests/production
secretGenerator:
- name: ludus-config
  behavior: merge
  envs:
  - ludus.env
EOF
```

Create a `ludus.env` file, which defines the ludus application configuration:

_Replace with your own configuration values._

```sh
cat <<EOF >./.env/ludus.env
DB_URL=jdbc:mariadb://host.docker.internal:3306/ludus
DB_USERNAME=ludus
DB_PASSWORD=ludus
EOF
```

Finally, run these commands to deploy the application stack:

```sh
kubectl create namespace colosseum
kubectl apply -k ./.env
```

After a short moment, the Bisselium WebUI interface can be accessed via <http://127.0.0.1:30000/>.

The Ludus endpoint is also accessible via <http://127.0.0.1:30001/>. _This allows you to manage gladiators and engage them in combats._

Add gladiators by running this Python script:

```sh
python ../api/add_random_gladiators/main.py 127.0.0.1 -p 30001
```

Engage random duels with this cURL command:

```sh
curl -X POST http://127.0.0.1:30001/duels/resolve/random
```

## Clean everything up

Once you are done, you can remove the cluster with this single command:

```sh
kind delete clusters colosseum-project
```

---

Have fun! :)
