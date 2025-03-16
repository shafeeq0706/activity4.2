pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/shafeeq0706/activity4.2.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('my-docker-image')
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    docker.run('my-docker-image')
                }
            }
        }
    }
}
