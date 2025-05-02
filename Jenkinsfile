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
        stage('Install Redis') {
            steps {
                sh '''
                    apt-get update
                    apt-get install -y redis-server curl
                '''
            }
        }

        stage('Install Python Dependencies') {
            steps {
                dir("${APP_DIR}") {
                    sh 'pip install --upgrade pip'
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Start Redis') {
            steps {
                sh '''
                    redis-server --daemonize yes
                    sleep 3
                    redis-cli ping
                '''
            }
        }

        stage('Run FastAPI') {
            steps {
                dir("${APP_DIR}") {
                    sh 'uvicorn main:app --host 0.0.0.0 --port 8000 --reload &'
                    sh 'sleep 5'
                }
            }
        }

        stage('Smoke Test') {
            steps {
                sh 'curl http://localhost:8000/docs || echo "App not responding"'
            }
        }
    }
}
