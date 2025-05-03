pipeline {
    agent {
        docker {
            image 'python:3.10-slim'
            args '-p 8000:8000'
        }
    }

    environment {
        APP_DIR = 'app'
    }

    stages {
        stage('test run') {
            steps {
                sh 'python --version'
            }
        
        }
    }
}
