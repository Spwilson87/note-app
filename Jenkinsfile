pipeline {
    agent any
	environment {
		DOCKERHUB_CREDENTIALS=credentials('docker-hub')
        ID = "${env.BUILD_NUMBER}"
        BRANCH = "${env.GIT_BRANCH}"
	}
    stages {
        stage ('Git Branch') {
            steps{
                echo 'Building git branch = ${BRANCH}'
            }
        }

        stage ('Build Image') {
            steps{
                sh 'docker build -t spwilson87/note-app:latest -t spwilson87/note-app:0.${ID} .'
            }
        }

        stage ('Testing with pytest') {
            steps{
                echo "starting pytest"
                sh 'python3 -m pytest --junitxml pytest-results.xml'
            }
        }

		stage('dockerHub Login') {

			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}

        stage ('Push to Docker Hub') {
            steps{
                sh 'docker push spwilson87/note-app:latest'
                sh 'docker push spwilson87/note-app:0.${ID}'
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
            sh 'docker logout'
        }
    }  
}