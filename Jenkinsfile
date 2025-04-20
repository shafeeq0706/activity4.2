pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask_project"
        CONTAINER_PORT = "5000"
        HOST_PORT = "5003"  // Change this to an unused port
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t $IMAGE_NAME ./flask_project"
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    sh "docker run -d -p $HOST_PORT:$CONTAINER_PORT $IMAGE_NAME"
                }
            }
        }

        // You can add test, deploy, etc. stages here
    }
}
