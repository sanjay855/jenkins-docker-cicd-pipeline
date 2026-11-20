pipeline {
    agent any
    environment {
        IMAGE_NAME = "devops-status-api"
        CONTAINER_NAME = "status-api-live"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:${BUILD_NUMBER} -t $IMAGE_NAME:latest .'
            }
        }
        stage('Run Automated Tests') {
            steps {
                sh 'docker run --rm $IMAGE_NAME:${BUILD_NUMBER} pytest -v'
            }
        }
        stage('Deploy & Health Check') {
            steps {
                sh '''
                docker stop $CONTAINER_NAME || true
                docker rm $CONTAINER_NAME || true
                docker run -d --name $CONTAINER_NAME -p 8085:5000 -e APP_VERSION="1.0.${BUILD_NUMBER}" $IMAGE_NAME:${BUILD_NUMBER}
                sleep 3
                curl -f http://host.docker.internal:8085/health || curl -f http://172.17.0.1:8085/health
                '''
            }
        }
    }
}
