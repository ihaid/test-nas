pipeline {
    agent { docker { image 'themattrix/tox' } }
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