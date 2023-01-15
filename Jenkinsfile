pipeline {
    agent any
	environment {
		DOCKERHUB_CREDENTIALS=credentials('docker-hub')
	}
    stages {
        stage ('Build Image') {
            steps{
                sh 'docker build -t spwilson87/note-app:latest -t spwilson87/note-app:${env.BUILD_NUMBER} .'
            }
        }

        stage ('Testing with pytest') {
            steps{
                echo "starting pytest"
                sh 'python3 -m pytest --junitxml pytest-results.xml'
            }
        }
        stage ('Push to Docker Hub') {
            steps{
                sh 'docker push spwilson87/note-app:latest'
                sh 'docker push spwilson87/note-app:${env.BUILD_NUMBER}'
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