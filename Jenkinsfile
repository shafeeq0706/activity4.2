pipeline {
    agent any
    stages {
        stage('Checkout SCM') {
            steps {
                git 'https://github.com/shafeeq0706/activity4.2.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    // Building Docker image as before
                    docker.build('flask_project', './flask_project')
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    // Running the Docker container inside the Jenkins pipeline
                    docker.image('flask_project').inside {
                        sh 'python app.py'  // Adjust this command based on what your app runs
                    }
                }
            }
        }
    }
}
