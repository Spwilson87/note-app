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
                sh 'python3 -m pytest --junitxml pytest-results.xml'
            }
        }

        stage ('Stop note app') {
            steps{
                sh 'docker compose down'

            }
        }

        stage ('Run note app') {
            steps{
                sh 'docker compose up -d'

            }
        }

    }
    post {
        always {
            archiveArtifacts artifacts: 'pytest-results.xml', onlyIfSuccessful: true
        }
    }  
}