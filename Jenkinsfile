pipeline {
    agent none
    stages{
        stage('build') {
            agent none
            steps{
                echo "test"
            }  
        }
       stage ('Deploy') {
           steps{
                 script{
                       sshagent(credentials : ['b0543eb0-0242-41e7-8e34-044591cf6a33']) {
                       sh 'python --version'
                       }
                  }
           }
       }
    }
}
