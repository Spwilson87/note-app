pipeline {
    agent {
  label 'Python VM'
}

    stages {
        stage ('Build Image') {
            steps{
                sh 'docker build -t note-app .'
            }
        }

        stage ('Testing with pytest') {
            steps{
                sh 'pip list'
                echo "starting pytest"
                sh 'python -m pytest'

            }
        }

        stage ('Run note app') {
            steps{
                sh 'docker run -d -p 5000:5000 note-app'

            }
        }

    }
    
}