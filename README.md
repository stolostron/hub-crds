# MultiClusterHub CRDs

Central location for CRDs used by Multiclusterhub components. This repo provides CRDs for the [multiclusterhub-operator installer](https://github.com/open-cluster-management/multicloudhub-operator).

## CRD chart sources
Original locations of CRDs

https://github.com/open-cluster-management/rcm-chart
- 0000_00_addon.open-cluster-management.io_clustermanagementaddons.crd.yaml
- 0000_01_addon.open-cluster-management.io_managedclusteraddons.crd.yaml
- agent.open-cluster-management.io_klusterletaddonconfigs_crd.yaml

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

https://github.com/open-cluster-management/multicloudhub-operator (foundation/OCM)
- view.open-cluster-management.io_managedclusterviews_crd.yaml
- cluster.open-cluster-management.io_mirroredmanagedclusters.yaml
- internal.open-cluster-management.io_managedclusterinfos_crd.yaml
- inventory.open-cluster-management.io_baremetalassets_crd.yaml
- action.open-cluster-management.io_managedclusteractions_crd.yaml
