pipeline { 
    agent any 
    stages {
      stage('Advertise & Validate'){
          parallel{
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
    stage('Validate Advertise') { 
        steps { 
            echo "Advertised messages will get validated here" 
            sleep(time: 10, unit: "SECONDS")
        }
    }
          }
      }
    }
}

