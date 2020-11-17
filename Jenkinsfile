pipeline {
    agent none 
    stages {
       stage('Raspy Simulators') {
	        parallel{
			        stage('Raspy Simulator 1') {
			            agent { label 'raspy_broadcaster1' } 
			            steps {
			                echo 'Raspy1 BLE Advertise Simulated'
			                sh 'python3 /home/pi/workspace/pipeline_main/avdertise_message.py'
			            }
			        }
			        stage('Raspy Simulator 2') {
			            agent { label 'raspy_broadcaster2' } 
			            steps {
			                echo 'Raspy2 BLE Advertise Simulated'
			                sh 'python3 /home/pi/workspace/pipeline_main/avdertise_message.py'
			            }
			        }
			        stage('Raspy Simulator 3') {
			            agent { label 'raspy_broadcaster3' } 
			            steps {
			                echo 'Raspy3 BLE Advertise Simulated'
			                sh 'python3 /home/pi/workspace/pipeline_main/avdertise_message.py'
			            }
			        }
		    }
		}
	        stage('Validate Broadcast') { 
			agent { label 'raspy_validator' } 
			steps { 
			    echo "Advertised messages will get validated here" 
			    sh 'python3 /root/flasktest/serial_log.py start'
			}
                }
		stage('Result uploader') { 
	        steps { 
	            echo "A Stage to upload the result to GCP" 
	        }
        }
    }
}
