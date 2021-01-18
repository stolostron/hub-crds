FROM registry.access.redhat.com/ubi8/ubi-minimal:latest

LABEL org.label-schema.vendor="Red Hat" \
      org.label-schema.name="multiclusterhub-crds" \
      org.label-schema.description="Repo storing CRDs used by Multiclusterhub charts" \
      org.label-schema.license="Red Hat Advanced Cluster Management for Kubernetes EULA"

WORKDIR /
COPY crds/ crds/
