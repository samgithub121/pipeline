pipeline {
    agent none 
    stages {
        stage('Example Build') {
            agent { label 'Raspy1' } 
            steps {
                echo 'Hello, Maven'
                sh 'python --version'
                sh 'ls -la'
            }
        }
        stage('Example Test') {
            agent { label 'Raspy2' } 
            steps {
                echo 'Hello, JDK'
                sh 'python --version'
                sh 'ls -la'
            }
        }
    }
