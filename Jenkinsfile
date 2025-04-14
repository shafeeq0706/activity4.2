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
                    docker.build('flask_project', './flask_project')
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    docker.run('flask_project')
                }
            }
        }
    }
}
