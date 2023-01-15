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
    post {
        always {
            archiveArtifacts artifacts: 'pytest-results.xml', onlyIfSuccessful: true
        }
    }

        stage ('Run note app') {
            steps{
                sh 'docker run -d -p 5000:5000 note-app'

            }
        }

    }
    
}