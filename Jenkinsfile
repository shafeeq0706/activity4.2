pipeline {
    agent any
    stages {
        stage('Checkout SCM') {
            steps {
                git 'https://github.com/shafeeq0706/activity4.2.git'
            }
        }
        stage('Echo') {
            steps {
                echo "Repository checkout successful!"
            }
        }
    }
}
