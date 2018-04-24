pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Pipeline started"'
                sh '''
                    sudo apt-get install python3-setuptools & sudo easy_install3 pip
                    echo "Installing tox"
                    pip install tox
                    echo "Running tox"
                    tox
                '''
            }
        }
    }
}