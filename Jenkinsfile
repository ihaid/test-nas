pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Pipeline started"'
                sh '''
                    echo "Installing tox"
                    pip install tox
                    echo "Running tox"
                    tox
                '''
            }
        }
    }
}