pipeline {
    agent {
        docker {
            image 'python:3.10-slim'
            args '-u root' // run as root user
        }
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        
        }

        stage('Linter') {
            steps {
                sh '''
                    flake8 application
                '''
            }
        
        }
    }
}
