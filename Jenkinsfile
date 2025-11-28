pipeline {
    agent any
    stages {
        stage('Build Docker Image') {
            steps {
                // Show Docker info
                sh 'docker info'

                // Build the Docker image
                sh 'docker build -t ecommerce-backend ./ecommerce_backend'
            }
        }

        stage('Run Tests') {
            steps {
                // Run your tests script
                sh './run_tests.sh'
            }
        }

        stage('Deploy') {
            steps {
                // Start containers with docker-compose
                sh 'docker-compose up -d'
            }
        }
    }
}
