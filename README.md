# Python Microservice CI/CD Pipeline with Jenkins and Docker

A hands-on DevOps project that automates the build, testing, deployment, and health verification of a Python Flask microservice using Jenkins and Docker in a WSL Ubuntu environment.

## Project Overview

This project demonstrates a CI/CD pipeline for a containerized Python API. Jenkins retrieves the project from GitHub, builds a Docker image, runs automated tests inside a container, deploys the application, and verifies that the deployed service is healthy.

The pipeline uses a versioned Docker image (`devops-status-api:1`) and also tags the image as `latest`.

## Architecture

```text
Developer
   |
   v
GitHub Repository
   |
   v
Jenkins Pipeline
   |
   +--> Checkout source
   |
   +--> Build Docker image
   |
   +--> Run automated tests (pytest)
   |
   +--> Deploy container
   |
   +--> Health check
          |
          v
   Running Flask API container
```

## Pipeline Workflow

The Jenkins pipeline contains the following stages:

| Stage | Description |
|---|---|
| **Checkout** | Retrieves the source code from the GitHub repository. |
| **Build Docker Image** | Builds the application image and tags it as `devops-status-api:1` and `devops-status-api:latest`. |
| **Run Automated Tests** | Runs the test suite inside a disposable container using `pytest`. |
| **Deploy & Health Check** | Replaces the running application container, starts the new container, and checks the health endpoint. |

### Automated Tests

The pipeline runs the following tests:

- `test_health_endpoint`
- `test_status_endpoint`

Both tests passed during the recorded pipeline run.

### Deployment and Health Verification

The deployed container is named `status-api-live`.

The container is published on host port `8085`, mapped to application port `5000`, and receives the environment variable:

```text
APP_VERSION=1.0.1
```

The pipeline verifies the service by requesting its health endpoint. The recorded response was:

```json
{
  "status": "healthy",
  "version": "1.0.1"
}
```

## Technology Stack

- **Python 3.11** — application runtime
- **Flask 3.0.3** — API framework
- **pytest 8.3.2** — automated testing
- **Docker** — image building and container runtime
- **Jenkins** — CI/CD pipeline automation
- **Git & GitHub** — source control and repository hosting
- **Ubuntu on WSL** — Linux environment used for the project

## Repository

GitHub: [jenkins-docker-cicd-pipeline](https://github.com/sanjay855/jenkins-docker-cicd-pipeline)

## Project Files

```text
.
├── app.py             # Flask microservice
├── test_app.py        # Automated tests
├── requirements.txt     # Python dependencies
├── Dockerfile         # Docker image build instructions
└── Jenkinsfile        # Jenkins pipeline
```

## Running Locally

### Prerequisites

- Python 3.11
- Git
- Docker
- Jenkins configured to use Docker
- WSL with Ubuntu (used in this project)

### Clone the repository

```bash
git clone https://github.com/sanjay855/jenkins-docker-cicd-pipeline.git
cd jenkins-docker-cicd-pipeline
```

### Install dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Run the test suite

```bash
pytest -v
```

## Build and Run with Docker

### Build the image

```bash
docker build -t devops-status-api:1 -t devops-status-api:latest .
```

### Run the container

```bash
docker run -d --name status-api-live -p 8085:5000 -e APP_VERSION=1.0.1 devops-status-api:1
```

### Verify the health endpoint

```bash
curl http://localhost:8085/health
```

The project pipeline used the WSL Docker gateway address during its health-check stage. When testing from your own environment, use the address that is reachable from the shell where the command is executed.

## Jenkins

Jenkins runs in a Docker container in the WSL Ubuntu environment. The pipeline is defined in the `Jenkinsfile` and uses Docker to build the application image, run the tests, deploy the container, and perform a health check.

The project repository is configured as the pipeline source in Jenkins.

## Screenshots

Screenshots documenting the setup and pipeline execution are stored in the repository's `screenshots/` folder.

Suggested screenshots to include:

- Jenkins setup and dashboard
- Jenkinsfile pipeline definition
- Docker image build output
- Automated test results
- Running Docker containers

<!-- Example:
![Jenkins pipeline](screenshots/jenkins-pipeline.png)
![Automated tests](screenshots/pytest-results.png)
![Deployment health check](screenshots/health-check.png)
-->

## Key Learning Outcomes

- Building a Jenkins declarative pipeline
- Integrating a GitHub repository with Jenkins
- Creating Docker images for a Python application
- Running automated tests as part of a CI/CD workflow
- Deploying and replacing containers through pipeline automation
- Validating a deployment with an HTTP health check
- Working with Docker and Linux in a WSL Ubuntu environment

## Future Improvements

- Trigger pipeline runs automatically using GitHub webhooks
- Add code-quality checks and security scanning
- Publish images to a container registry
- Add image tagging based on Git commit or build number
- Improve deployment rollback and failure recovery
- Add notifications for pipeline success or failure

---
