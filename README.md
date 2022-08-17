[comment]: # ( Copyright Contributors to the Open Cluster Management project )

# WORK IN PROGRESS

We are in the process of enabling this repo for community contribution. See wiki [here](https://open-cluster-management.io/concepts/architecture/).

# MultiClusterHub CRDs

Central location for CRDs used by Multiclusterhub components. This repo provides CRDs for the [multiclusterhub-operator installer](https://github.com/stolostron/multiclusterhub-operator). Updating CRDs in this repo will trigger an update in the installer repo to point to the latest version.

## CRD chart sources
Original locations of CRDs

https://github.com/stolostron/cluster-lifecycle-chart
- agent.open-cluster-management.io_klusterletaddonconfigs_crd.yaml

https://github.com/stolostron/grc-chart
- policy.open-cluster-management.io_placementbindings_crd.yaml
- policy.open-cluster-management.io_policies_crd.yaml

https://github.com/stolostron/search-chart
- search.open-cluster-management.io_searchcustomizations.yaml
- search.open-cluster-management.io_searchoperators.yaml

https://github.com/stolostron/console-chart
- user-preference-crd.yaml
