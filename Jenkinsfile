pipeline{
    agent any
    stages{
        stage('setup python venv'){
           steps{
            sh '''
            chmod +x envsetup.sh
            ./envsetup.sh
            '''
        }
        }
        stage('setup gunicorn setup'){
            steps{
                sh '''
                chmod +x gunicorn.sh
                ./gunicorn.sh
                '''
            }
            }
    

    }
}
