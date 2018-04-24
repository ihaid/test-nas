pipeline {
    agent { docker 'themattrix/tox' } 
    stages {
        stage('Build') {
            steps {
                sh '''
                    echo "Running tox"
                    tox
                '''
        }
    }
}
