pipeline {
    agent {
        docker {
            image 'python:3.10-slim'
        }
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/Dhaniesh/project-shortify.git'
            }
        }

        stage('Install Deps & Lint') {
            steps {
                sh '''
                    pip install -r requirements.txt
                '''
            }
        
        }
    }
}
