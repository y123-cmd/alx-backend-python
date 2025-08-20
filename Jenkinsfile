pipeline {
    agent any

    tools {
        python "Python3"   // Provided by ShiningPanda plugin
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-creds',
                    url: 'git@github.com:y123-cmd/alx-backend-python.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                pip install -r messaging_app/requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                source venv/bin/activate
                pytest messaging_app/tests --junitxml=test-results.xml
                '''
            }
        }

        stage('Archive Test Report') {
            steps {
                junit 'test-results.xml'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished!'
        }
    }
}

