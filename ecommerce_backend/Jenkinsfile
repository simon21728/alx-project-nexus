pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                checkout scm
            }
        }

        stage('Backend - Build Docker Image') {
            steps {
                sh 'docker build -t ecommerce-backend ./ecommerce_backend'
            }
        }

        stage('Backend - Run Tests') {
            steps {
                sh 'docker run --rm ecommerce-backend python manage.py test'
            }
        }

        stage('Deploy using docker-compose') {
            steps {
                sh 'docker compose -f docker-compose.yml up -d --build'
            }
        }
    }
}
