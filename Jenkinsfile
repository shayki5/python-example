pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent { label 'master' }
            steps {
                sh 'python script.py' 
            }
        }
    }
}
