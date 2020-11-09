pipeline {
    node{
    stage("ssh-agent"){
      script {

        sshagent (credentials: ['b0543eb0-0242-41e7-8e34-044591cf6a33']) {
              cat 'Hello Sam'
            }

          }
         }
     }
}