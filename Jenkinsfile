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
                dir('flask_project') {
                    script {
                        docker.build('flask_project')
                    }
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    sh 'docker run -d -p 5000:5000 flask_project'
                }
            }
        }
    }

           stage('Check Docker Version') {
            steps {
                script {
                    sh 'docker --version'     
                }
            }
        }
    }
}
