[comment]: # ( Copyright Contributors to the Open Cluster Management project )

# WORK IN PROGRESS

We are in the process of enabling this repo for community contribution. See wiki [here](https://open-cluster-management.io/concepts/architecture/).

# MultiClusterHub CRDs

Central location for CRDs used by Multiclusterhub components. This repo provides CRDs for the [multiclusterhub-operator installer](https://github.com/open-cluster-management/multiclusterhub-operator). Updating CRDs in this repo will trigger an update in the installer repo to point to the latest version.

## CRD chart sources
Original locations of CRDs

https://github.com/open-cluster-management/rcm-chart
- agent.open-cluster-management.io_klusterletaddonconfigs_crd.yaml

https://github.com/open-cluster-management/cluster-lifecycle-chart
- cluster.open-cluster-management.io_clustercurators.yaml

https://github.com/open-cluster-management/cert-manager-chart
- certificate-crd.yaml
- certificate-resource-crd.yaml
- challenge-crd.yaml
- clusterissuer-crd.yaml
- issuer-crd.yaml
- order-crd.yaml

https://github.com/open-cluster-management/grc-chart
- policy.open-cluster-management.io_placementbindings_crd.yaml
- policy.open-cluster-management.io_policies_crd.yaml

https://github.com/open-cluster-management/search-chart
- search.open-cluster-management.io_searchcustomizations.yaml
- search.open-cluster-management.io_searchoperators.yaml

https://github.com/open-cluster-management/console-chart
- user-preference-crd.yaml

https://github.com/open-cluster-management/multiclusterhub-operator (foundation/OCM)
- view.open-cluster-management.io_managedclusterviews_crd.yaml
- internal.open-cluster-management.io_managedclusterinfos_crd.yaml
- inventory.open-cluster-management.io_baremetalassets_crd.yaml
- action.open-cluster-management.io_managedclusteractions_crd.yaml
