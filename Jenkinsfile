pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Pipeline started"'
                sh '''
                    export PATH=$PATH:~/.local/bin/
                    echo "Installing tox"
                    pip install tox
                    echo "Running tox"
                    tox
                '''
            }
        }
    }
}