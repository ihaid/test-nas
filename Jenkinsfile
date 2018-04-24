pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Pipeline started"'
                sh '''
                    echo "Running tox"
                    tox
                '''
            }
        }
    }
}