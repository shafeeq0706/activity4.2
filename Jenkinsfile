pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                git branch: 'main', url: 'https://github.com/shafeeq0706/activity4.2.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Store the built image reference in a variable
                    myImage = docker.build('flask_project')
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Use the image reference to run the container
                    myImage.run('-p 5000:5000')
                }
            }
        }
    }
}
