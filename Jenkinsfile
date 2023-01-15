pipeline {
    agent {
  label 'Python VM'
}

    stages {
        stage ('Build Image') {
            steps{
                sh 'docker build -t note-app .'
                sh 'pwd'
                sh 'whoami'
                sh 'ls'
            }
        }
    }
    agent {
  label 'Python VM'
}
    stages {
        stage ('Testing with pytest') {
            steps{
                sh 'pwd'
                sh 'whoami'
                sh 'ls'
                echo "starting pytest"
                sh 'python -m pytest'

            }
        }
    }
    agent {
  label 'Python VM'
}
    stages {
        stage ('Run note app') {
            steps{
                sh 'docker run -d -p 5000:5000 note-app'

            }
        }

    }
}