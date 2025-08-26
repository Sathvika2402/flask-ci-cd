pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "flask-ci-cd:latest"
        DOCKER_CONTAINER = "flask-ci-cd"
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Cloning repository...'
                git branch: 'main', url: 'https://github.com/Sathvika2402/flask-ci-cd.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install --upgrade pip'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh "docker build -t ${DOCKER_IMAGE} ."
            }
        }

        stage('Run Docker Container') {
            steps {
                echo 'Stopping old container if exists...'
                sh "docker rm -f ${DOCKER_CONTAINER} || true"
                echo 'Running new container...'
                sh "docker run -d -p 5000:5000 --name ${DOCKER_CONTAINER} ${DOCKER_IMAGE}"
            }
        }

        stage('Test Application') {
            steps {
                echo 'Testing Flask app endpoints...'
                sh "curl -f http://localhost:5000/ || echo 'App not responding!'"
                sh "curl -f http://localhost:5000/users || echo 'Users endpoint failed!'"
            }
        }
    }

    post {
        success {
            echo '✅ Build and deployment succeeded!'
        }
        failure {
            echo '❌ Build or deployment failed!'
        }
    }
}
