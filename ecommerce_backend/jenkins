pipeline {
    agent none
    stages {
        stage('Build Docker Image') {
            agent {
                docker {
                    image 'docker:24-dind'
                    args '--privileged'
                }
            }
            steps {
                sh 'docker info'
                sh 'docker build -t ecommerce-backend ./ecommerce_backend'
            }
        }
        stage('Run Tests') {
            agent any
            steps {
                sh './run_tests.sh'
            }
        }
        stage('Deploy') {
            agent any
            steps {
                sh 'docker-compose up -d'
            }
        }
    }
}
