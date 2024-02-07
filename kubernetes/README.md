# Deploy on Kubernetes

Here, we use [`kind`](https://kind.sigs.k8s.io/) to deploy our K8s sandbox environment on Docker for Windows.

Run `cluster.ps1 create` to create the cluster of nodes.

Then, run `app.ps1 apply` to deploy the application within the cluster.

When everything is up, the Bisselium WebUI is accessible via <http://127.0.0.1:30000/>.

The Ludus endpoint is exposed on port `30001`. This allows you to manage gladiators and engage combats.

Have fun! :)
