pipeline {
    agent none 
    stages {
       stage('Advertise & Validate') {
	       parallel{
		       stage('Raspy Simulators') {
			        parallel{
					        stage('Raspy Simulator 1') {
					            agent { label 'Raspy1' } 
					            steps {
					                echo 'Raspy1 BLE Advertise Simulated'
					                sh 'python3 /home/pi/workspace/pipeline_main/avdertise_message.py'
					            }
					        }
					        stage('Raspy Simulator 2') {
					            agent { label 'Raspy2' } 
					            steps {
					                echo 'Raspy2 BLE Advertise Simulated'
					                sh 'python3 /home/pi/workspace/pipeline_main/avdertise_message.py'
					            }
					        }
					        stage('Raspy Simulator 3') {
					            agent { label 'Raspy3' } 
					            steps {
					                echo 'Raspy3 BLE Advertise Simulated'
					                sh 'python3 /home/pi/workspace/pipeline_main/avdertise_message.py'
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
