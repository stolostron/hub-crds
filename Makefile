# Copyright Contributors to the Open Cluster Management project

set-copyright:
	@bash ./scripts/set-copyright.sh

.PHONY: lint
lint:
	@bash ./scripts/lint.sh
