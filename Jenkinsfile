pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Pipeline started"'
                sh '''
                    apt-get install python3-setuptools & easy_install3 pip
                    echo "Installing tox"
                    pip install tox
                    echo "Running tox"
                    tox
                '''
            }
        }
    }
}