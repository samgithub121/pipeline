pipeline { 
    agent any 
    stages {
        parallel{
            stage('RaspySimulator1') { 
                steps { 
                    echo "Simulate the BLE in raspy1" 
                    sleep(time: 5, unit: "SECONDS")
                }
            }
            stage('RaspySimulator2'){
                steps {
                    echo "Simulate the BLE in raspy2" 
                    sleep(time: 5, unit: "SECONDS")
                }
            }
            stage('RaspySimulator3') {
                steps {
                    echo "Simulate the BLE in raspy3" 
                    sleep(time: 5, unit: "SECONDS")
                }
            }
        }
    }
    parallel{
            stage('MonitorMessages') { 
                steps { 
                    echo "Start monitering the advertised messages in raspy" 
                }
            }
        }
}

