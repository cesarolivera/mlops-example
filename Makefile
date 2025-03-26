# AUTOR: CÉSAR OLIVERA COKAN- EMAIL: COliveraC@vitapro.com.pe

# VARIABLES AND CONSTANTS
NAME   		:= py-mlops-demo
TAG    		:= $$(git log -1 --format=%h) #TAG: SHORT GIT HASH COMMIT
IMG    		:= $(NAME):$(TAG)
LATEST 		:= $(NAME):latest
BASE_IMAGE  := python:3.11-slim

#us-east1-docker.pkg.dev/

# BUILD PYTHON PROJECT SOURCE CODE
build:
	kedro docker build \
	--base-image $(BASE_IMAGE) \
	--image $(CONT_REG)/$(LATEST)

# PUSH KEDRO PROJECT SOURCE CODE CONTAINER 
push:
	docker push $(CONT_REG)/$(LATEST)

# RUN KEDRO COMMAND
run:
	kedro docker cmd "$(COMMAND)"