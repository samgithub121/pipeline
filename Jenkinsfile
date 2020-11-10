pipeline { 
    agent any 
    stages {
      stage('Raspy Simulators') {
        parallel{
            stage('RaspySimulator1') { 
                steps { 
                    echo "Simulate the BLE in raspy1" 
                    sleep(time: 10, unit: "SECONDS")
                }
            }
            stage('RaspySimulator2'){
                steps {
                    echo "Simulate the BLE in raspy2" 
                    sleep(time: 10, unit: "SECONDS")
                }
            }
            stage('RaspySimulator3') {
                steps {
                    echo "Simulate the BLE in raspy3" 
                    sleep(time: 10, unit: "SECONDS")
                }
            }
        }
      }
    stage('RaspySimulator1') { 
        steps { 
            echo "Simulate the BLE in raspy1" 
            sleep(time: 10, unit: "SECONDS")
        }
    }
    }
}

