pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent { label 'linux' }
            steps {
                sh 'python script.py' 
            }
        }
    }
}
