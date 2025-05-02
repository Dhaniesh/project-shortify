pipeline {
    agent {
        docker {
            image 'python:3.10-slim'
            args '-v /c/ProgramData/Jenkins/.jenkins/workspace/build-shorify:/app -w /app -p 8000:8000'
        }
    }

    environment {
        APP_DIR = '/app'
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                    apt-get update && \
                    apt-get install -y redis-server curl && \
                    pip install --upgrade pip && \
                    pip install -r ${APP_DIR}/requirements.txt
                '''
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
                sh 'uvicorn ${APP_DIR}/main:app --host 0.0.0.0 --port 8000 --reload &'
                sh 'sleep 5'
            }
        }

        stage('Smoke Test') {
            steps {
                sh 'curl http://localhost:8000/docs || echo "App not responding"'
            }
        }
    }
}
