pipeline {
    agent any

    stages {
        stage ('Build Image') {
            steps{
                sh 'docker build -t note-app .'
            }
        }

        stage ('Testing with pytest') {
            steps{
                echo "starting pytest"
                sh 'python3 -m pytest'

            }
        }

        stage ('Run note app') {
            steps{
                sh 'docker run -d -p 5000:5000 note-app'

            }
        }

    }
    
}