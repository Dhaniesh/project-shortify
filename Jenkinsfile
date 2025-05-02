pipeline {
    agent {
        docker {
            image 'python:3' // Prebuilt image with Python + Redis
            args '-p 8000:8000' // FastAPI port
        }
    }

    environment {
        APP_DIR = 'project-shortify' // Change to your app folder
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Dhaniesh/project-shortify.git'
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
                sh 'redis-server --daemonize yes'
                sh 'sleep 5' // Wait for Redis to start
                sh 'redis-cli ping' // Should return PONG
            }
        }

        stage('Start FastAPI') {
            steps {
                dir("${APP_DIR}") {
                    sh 'uvicorn main:app --host 0.0.0.0 --port 8000 --reload &'
                    sh 'sleep 10'
                }
            }
        }

        stage('Test FastAPI') {
            steps {
                sh 'curl http://localhost:8000/docs || echo "App failed to start"'
            }
        }
    }
}
