node{

    stage("ssh-agent"){

      script {

        sshagent (credentials: ['80ccbc4f-14b4-4c13-a9b3-b4b9958492f7']) {
                sh 'sshpass -p "Skyl0123" ssh -o StrictHostKeyChecking=no pi@10.49.0.2'
            }

          }
         }
     }

