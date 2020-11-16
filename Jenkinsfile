pipeline { 
    agent any 
    stages {
      stage('Raspy Simulators') {
        parallel{
            stage('RaspySimulator1') { 
                steps { 
                    echo "Simulate the BLE in raspy1" 
                    script {
                           sh 'sshpass -p "Skyl0123" ssh -o StrictHostKeyChecking=no pi@10.49.0.2'
                           sh 'ls -la'
                    }
                }
            }
            stage('RaspySimulator2'){
                steps {
                    echo "Simulate the BLE in raspy2" 
                    script {
                           sh 'sshpass -p "Skyl0123" ssh -o StrictHostKeyChecking=no pi@10.49.0.3'
                           sh 'ls -la'
                    }
                }
            }
            stage('RaspySimulator3') {
                steps {
                    echo "Simulate the BLE in raspy3" 
                    script {
                           sh 'sshpass -p "Skyl0123" ssh -o StrictHostKeyChecking=no pi@10.49.0.4'
                           sh 'pwd'
                    }
                }
            }
        }
      }
    stage('Validate Advertise') { 
        steps { 
            echo "Advertised messages will get validated here" 
            sleep(time: 10, unit: "SECONDS")
        }
    }
    }
}
