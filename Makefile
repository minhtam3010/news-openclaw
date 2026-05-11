ifneq ("$(wildcard .env)","")
    include .env
    export
endif

run:
	uv run main.py

package:
	uv add -r requirements.txt

commit:
	git add .
	git commit

build:
	docker build -t news-bot -f docker/Dockerfile .
	docker tag news-bot:latest $(AWS_ACCOUNT_ID).dkr.ecr.$(AWS_REGION).amazonaws.com/$(ECR_REPO_NAME):latest
	
	aws ecr get-login-password --region $(AWS_REGION) | docker login --username AWS --password-stdin $(AWS_ACCOUNT_ID).dkr.ecr.$(AWS_REGION).amazonaws.com
	
	docker push $(AWS_ACCOUNT_ID).dkr.ecr.$(AWS_REGION).amazonaws.com/$(ECR_REPO_NAME):latest

.PHONY: run commit package