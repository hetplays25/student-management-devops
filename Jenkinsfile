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
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest -q'
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
                sh 'docker run -d --name student-management -p 5000:5000 student-management:latest'
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
