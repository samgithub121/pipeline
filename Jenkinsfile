pipeline {
    agent none 
    stages {
       stage('Raspy Simulators') {
	        parallel{
			        stage('Raspy Simulator 1') {
			            agent { label 'raspy_broadcaster1' } 
			            steps {
			                echo 'Raspy1 BLE Advertise Simulated'
			                //sh 'python3 /home/pi/workspace/pipeline_main/avdertise_message.py'
					sh 'cd /home/pi/sensor_test_auto/'
					sh 'python3 -m  pytest test_suite/stability/test_001_broadcast_ble_messages.py  --html=reports/results.html'
			            }
			        }
			        stage('Raspy Simulator 2') {
			            agent { label 'raspy_broadcaster2' } 
			            steps {
			                echo 'Raspy2 BLE Advertise Simulated'
			                //sh 'python3 /home/pi/workspace/pipeline_main/avdertise_message.py'
					sh 'cd /home/pi/sensor_test_auto/'
					sh 'python3 -m  pytest test_suite/stability/test_001_broadcast_ble_messages.py  --html=reports/results.html'
			            }
			        }
			        stage('Raspy Simulator 3') {
			            agent { label 'raspy_broadcaster3' } 
			            steps {
			                echo 'Raspy3 BLE Advertise Simulated'
			                //sh 'python3 /home/pi/workspace/pipeline_main/avdertise_message.py'
					sh 'cd /home/pi/sensor_test_auto/'
					sh 'python3 -m  pytest test_suite/stability/test_001_broadcast_ble_messages.py  --html=reports/results.html'
			            }
			        }
			       stage('Validate Broadcast') { 
			            agent { label 'raspy_validator' } 
			            steps { 
			                 echo "Advertised messages will get validated here" 
		                         //sh 'python3 /root/flasktest/process_killer.py'
					 //sleep(time: 10, unit: "SECONDS")
			                 //sh 'python3 /root/flasktest/serial_log.py start'
					 sh 'cd /home/pi/workspace/pipeline_main/sensor_test_auto/'
					 sh 'python3 -m  pytest test_suite/stability/test_002_ble_broadcast_validator.py  --html=reports/results.html'
			            }
                               }
		    }
		}
		stage('Result uploader') { 
	        steps { 
	            echo "A Stage to upload the result to GCP" 
	        }
        }
    }
}
