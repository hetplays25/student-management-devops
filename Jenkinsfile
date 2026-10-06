pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python --version'
                sh 'python -m pip install --break-system-packages -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python -m pytest -q'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t student-management:${BUILD_NUMBER} .'
                sh 'docker tag student-management:${BUILD_NUMBER} student-management:latest'
            }
        }

        stage('Deploy Container') {
            steps {
                sh 'docker rm -f student-management || true'
                sh 'docker run -d --name student-management -p 5001:5001 student-management:latest'
            }
        }
    }

    post {
        success {
            echo 'CI/CD pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check the stage logs.'
        }
    }
}