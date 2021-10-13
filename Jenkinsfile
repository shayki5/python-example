pipeline {
    agent none 
    stages {
        stage('Create file') { 
            agent { label 'master' }
            steps {
                sh 'python create_file.py' 
            }
        }
        stage('Get longets word') { 
            agent { label 'master' }
            steps {
                sh 'python count_words_chars.py' 
            }
        }
        stage('Run unit tests') { 
            agent { label 'master' }
            steps {
                sh 'python unit_test.py' 
            }
        }
    }
}
