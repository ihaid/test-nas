pipeline {
    agent { 
        docker { image 'themattrix/tox' } 
    }
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
}
    
