pipeline {
    agent {
        docker {
            image 'python:3.10-slim'
        }
    }

    stages {
        stage('Install Deps & Lint') {
            steps {
                sh '''
                    pip install -r requirements.txt
                '''
            }
        
        }
    }
}
