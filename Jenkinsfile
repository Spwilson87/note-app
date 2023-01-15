pipeline {
    agent any

    stages {
        stage ('Stop note app if running') {
            steps{
                sh 'docker compose down'

            }
        }
        stage ('Run note app') {
            steps{
                sh 'docker compose up -d'

            }
        }
        stage ('Testing with pytest') {
            steps{
                echo "starting pytest"
                sh 'python3 -m pytest --junitxml pytest-results.xml'
            }
        }





    }
    post {
        always {
            archiveArtifacts artifacts: 'pytest-results.xml', onlyIfSuccessful: true
        }
    }  
}