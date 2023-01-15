pipeline {
    agent {
  label 'Python VM'
}

    stages {
        stage ('testing jenkins webhook') {
            steps{
                sh 'docker run hello-world'
                sh 'docker images'
                sh 'docker rmi -f $(docker images -aq)'
                sh 'docker images'
            }
        }


    }
}