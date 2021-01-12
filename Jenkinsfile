pipeline {
    agent none 
    stages {
	   stage('Upgrade Hub Firmware') { 
		agent { label 'raspy_validator' } 
	        steps { 
	            echo "Pipeline will ugrade the hub firmware here" 
	            sh "python3 /root/flasktest/upgrade_firmware.py  -jfrog_path='https://skyloeng.jfrog.io/artifactory/production_releases/BEAGLE-v1.5.11.1/SOB.bin'"
	   }
       stage('Raspy Simulators') {
	        parallel{
			        stage('Raspy Simulator 1') {
			            agent { label 'raspy_BLE_broadcaster1' } 
			            steps {
					echo 'Raspy1 BLE Advertise Simulated'
			                //sh 'python3 /home/pi/workspace/pipeline_main/avdertise_message.py'
					sh 'cp -r /home/pi/sensor_test_auto/  /home/pi/workspace/pipeline_main/'
					sh 'cd /home/pi/workspace/pipeline_main/sensor_test_auto/'
					//sh 'pip3 install -r /home/pi/workspace/pipeline_main/sensor_test_auto/requirements.txt'
					//sh 'sudo apt-get install -y postgresql'
					//sh 'sudo apt-get install -y libpq-dev'
					//sh 'pip3 install psycopg2'
					sh 'sudo chmod 777 /home/pi/workspace/'
					sh 'python3 -m  pytest -s /home/pi/workspace/pipeline_main/sensor_test_auto/test_suite/stability/test_001_broadcast_ble_messages.py  --html=/home/pi/workspace/pipeline_main/sensor_test_auto/reports/results.html'
			            }
			        }
			        stage('Raspy Simulator 2') {
			            agent { label 'raspy_BLE_broadcaster2' } 
			            steps {
			                echo 'Raspy2 BLE Advertise Simulated'
			                //sh 'python3 /home/pi/workspace/pipeline_main/avdertise_message.py'
					sh 'cp -r /home/pi/sensor_test_auto/  /home/pi/workspace/pipeline_main/'
					sh 'cd /home/pi/workspace/pipeline_main/sensor_test_auto/'
					//sh 'pip3 install -r /home/pi/workspace/pipeline_main/sensor_test_auto/requirements.txt'
					//sh 'sudo apt-get install -y postgresql'
					//sh 'sudo apt-get install -y libpq-dev'
					//sh 'pip3 install psycopg2'
					sh 'sudo chmod 777 /home/pi/workspace/'
					sh 'python3 -m  pytest -s /home/pi/workspace/pipeline_main/sensor_test_auto/test_suite/stability/test_001_broadcast_ble_messages.py --html=/home/pi/workspace/pipeline_main/sensor_test_auto/reports/results.html'
			            }
			        }
			        stage('Raspy Simulator 3') {
			            agent { label 'raspy_BLE_broadcaster3' } 
			            steps {
			                echo 'Raspy3 BLE Advertise Simulated'
			                //sh 'python3 /home/pi/workspace/pipeline_main/avdertise_message.py'
					sh 'cp -r /home/pi/sensor_test_auto/  /home/pi/workspace/pipeline_main/'
					sh 'cd /home/pi/workspace/pipeline_main/sensor_test_auto/'
					//sh 'pip3 install -r /home/pi/workspace/pipeline_main/sensor_test_auto/requirements.txt'
					//sh 'sudo apt-get install -y postgresql'
					//sh 'sudo apt-get install -y libpq-dev'
					//sh 'pip3 install psycopg2'
					sh 'sudo chmod 777 /home/pi/workspace/'
					sh 'python3 -m  pytest -s /home/pi/workspace/pipeline_main/sensor_test_auto/test_suite/stability/test_001_broadcast_ble_messages.py  --html=/home/pi/workspace/pipeline_main/sensor_test_auto/reports/results.html'
			            }
			        }
			        stage('Raspy Simulator 4') {
			            agent { label 'raspy_BLE_broadcaster4' } 
			            steps {
			                echo 'Raspy4 BLE Advertise Simulated'
			                //sh 'python3 /home/pi/workspace/pipeline_main/avdertise_message.py'
					sh 'cp -r /home/pi/sensor_test_auto/  /home/pi/workspace/pipeline_main/'
					sh 'cd /home/pi/workspace/pipeline_main/sensor_test_auto/'
					//sh 'pip3 install -r /home/pi/workspace/pipeline_main/sensor_test_auto/requirements.txt'
					//sh 'sudo apt-get install -y postgresql'
					//sh 'sudo apt-get install -y libpq-dev'
					//sh 'pip3 install psycopg2'
					sh 'sudo chmod 777 /home/pi/workspace/'
					sh 'python3 -m  pytest -s /home/pi/workspace/pipeline_main/sensor_test_auto/test_suite/stability/test_001_broadcast_ble_messages.py  --html=/home/pi/workspace/pipeline_main/sensor_test_auto/reports/results.html'
			            }
			        }
			       stage('Raspy Simulator 5') {
			            agent { label 'raspy_BLE_broadcaster5' } 
			            steps {
			                echo 'Raspy5 BLE Advertise Simulated'
			                //sh 'python3 /home/pi/workspace/pipeline_main/avdertise_message.py'
					sh 'cp -r /home/pi/sensor_test_auto/  /home/pi/workspace/pipeline_main/'
					sh 'cd /home/pi/workspace/pipeline_main/sensor_test_auto/'
					//sh 'pip3 install -r /home/pi/workspace/pipeline_main/sensor_test_auto/requirements.txt'
					//sh 'sudo apt-get install -y postgresql'
					//sh 'sudo apt-get install -y libpq-dev'
					//sh 'pip3 install psycopg2'
					sh 'sudo chmod 777 /home/pi/workspace/'
					sh 'python3 -m  pytest -s /home/pi/workspace/pipeline_main/sensor_test_auto/test_suite/stability/test_001_broadcast_ble_messages.py  --html=/home/pi/workspace/pipeline_main/sensor_test_auto/reports/results.html'
			            }
			        }
			        stage('Raspy WIFI Simulator 1') {
			            agent { label 'raspy_WIFI_broadcaster1' } 
			            steps {
			                echo 'Raspy1 WIFI Advertise Simulated'
			                //sh 'python3 /home/pi/workspace/pipeline_main/avdertise_message.py'
					sh 'cp -r /home/pi/sensor_test_auto/  /home/pi/workspace/pipeline_main/'
					sh 'cd /home/pi/workspace/pipeline_main/sensor_test_auto/'
					//sh 'pip3 install -r /home/pi/workspace/pipeline_main/sensor_test_auto/requirements.txt'
					//sh 'sudo apt-get install -y postgresql'
					//sh 'sudo apt-get install -y libpq-dev'
					//sh 'pip3 install psycopg2'
					sh 'sudo chmod 777 /home/pi/workspace/'
					sh 'sudo chmod 777 /home/pi/sensor_test_auto/'
					sh 'python3 -m  pytest -s /home/pi/workspace/pipeline_main/sensor_test_auto/test_suite/stability/test_002_broadcast_wifi_messages.py  --html=/home/pi/workspace/pipeline_main/sensor_test_auto/reports/results.html'
			            }
			        }
			          stage('Raspy WIFI Simulator 2') {
			            agent { label 'raspy_WIFI_broadcaster2' } 
			            steps {
			                echo 'Raspy2 WIFI Advertise Simulated'
			                //sh 'python3 /home/pi/workspace/pipeline_main/avdertise_message.py'
					sh 'cp -r /home/pi/sensor_test_auto/  /home/pi/workspace/pipeline_main/'
					sh 'cd /home/pi/workspace/pipeline_main/sensor_test_auto/'
					//sh 'pip3 install -r /home/pi/workspace/pipeline_main/sensor_test_auto/requirements.txt'
					//sh 'sudo apt-get install -y postgresql'
					//sh 'sudo apt-get install -y libpq-dev'
					//sh 'pip3 install psycopg2'
					sh 'sudo chmod 777 /home/pi/workspace/'
					sh 'sudo chmod 777 /home/pi/sensor_test_auto/'
					sh 'python3 -m  pytest -s /home/pi/workspace/pipeline_main/sensor_test_auto/test_suite/stability/test_002_broadcast_wifi_messages.py  --html=/home/pi/workspace/pipeline_main/sensor_test_auto/reports/results.html'
			            }
			        }
			        stage('Raspy WIFI Simulator 3') {
			            agent { label 'raspy_WIFI_broadcaster3' } 
			            steps {
			                echo 'Raspy3 WIFI Advertise Simulated'
			                //sh 'python3 /home/pi/workspace/pipeline_main/avdertise_message.py'
					sh 'cp -r /home/pi/sensor_test_auto/  /home/pi/workspace/pipeline_main/'
					sh 'cd /home/pi/workspace/pipeline_main/sensor_test_auto/'
					//sh 'pip3 install -r /home/pi/workspace/pipeline_main/sensor_test_auto/requirements.txt'
					//sh 'sudo apt-get install -y postgresql'
					//sh 'sudo apt-get install -y libpq-dev'
					//sh 'pip3 install psycopg2'
					sh 'sudo chmod 777 /home/pi/workspace/'
					sh 'sudo chmod 777 /home/pi/sensor_test_auto/'
					sh 'python3 -m  pytest -s /home/pi/workspace/pipeline_main/sensor_test_auto/test_suite/stability/test_002_broadcast_wifi_messages.py  --html=/home/pi/workspace/pipeline_main/sensor_test_auto/reports/results.html'
			            }
			        }
			        stage('Raspy WIFI Simulator 4') {
			            agent { label 'raspy_WIFI_broadcaster4' } 
			            steps {
			                echo 'Raspy4 BLE Advertise Simulated'
			                //sh 'python3 /home/pi/workspace/pipeline_main/avdertise_message.py'
					sh 'cp -r /home/pi/sensor_test_auto/  /home/pi/workspace/pipeline_main/'
					sh 'cd /home/pi/workspace/pipeline_main/sensor_test_auto/'
					//sh 'pip3 install -r /home/pi/workspace/pipeline_main/sensor_test_auto/requirements.txt'
					//sh 'sudo apt-get install -y postgresql'
					//sh 'sudo apt-get install -y libpq-dev'
					//sh 'pip3 install psycopg2'
					sh 'sudo chmod 777 /home/pi/workspace/'
					sh 'sudo chmod 777 /home/pi/sensor_test_auto/'
					sh 'python3 -m  pytest -s /home/pi/workspace/pipeline_main/sensor_test_auto/test_suite/stability/test_002_broadcast_wifi_messages.py  --html=/home/pi/workspace/pipeline_main/sensor_test_auto/reports/results.html'
			            }
			        }
			        stage('Raspy WIFI Simulator 5') {
			            agent { label 'raspy_WIFI_broadcaster5' } 
			            steps {
			                echo 'Raspy4 BLE Advertise Simulated'
			                //sh 'python3 /home/pi/workspace/pipeline_main/avdertise_message.py'
					sh 'cp -r /home/pi/sensor_test_auto/  /home/pi/workspace/pipeline_main/'
					sh 'cd /home/pi/workspace/pipeline_main/sensor_test_auto/'
					//sh 'pip3 install -r /home/pi/workspace/pipeline_main/sensor_test_auto/requirements.txt'
					//sh 'sudo apt-get install -y postgresql'
					//sh 'sudo apt-get install -y libpq-dev'
					//sh 'pip3 install psycopg2'
					sh 'sudo chmod 777 /home/pi/workspace/'
					sh 'sudo chmod 777 /home/pi/sensor_test_auto/'
					sh 'python3 -m  pytest -s /home/pi/workspace/pipeline_main/sensor_test_auto/test_suite/stability/test_002_broadcast_wifi_messages.py  --html=/home/pi/workspace/pipeline_main/sensor_test_auto/reports/results.html'
			            }
			        }
			        stage('Validate Broadcast') { 
				    agent { label 'raspy_validator' } 
				    steps { 
					 echo "Advertised messages will get validated here" 
					 //sh 'python3 /root/flasktest/process_killer.py'
					 //sleep(time: 10, unit: "SECONDS")
					 //sh 'python3 /root/flasktest/serial_log.py start'
					 sh 'cp -r /home/pi/sensor_test_auto/  /home/pi/workspace/pipeline_main/'
					 sh 'cd /home/pi/workspace/pipeline_main/sensor_test_auto/'
					 //sh 'pip3 install -r /home/pi/workspace/pipeline_main/sensor_test_auto/requirements.txt'
					 //sh 'sudo apt-get install -y postgresql'
					 //sh 'sudo apt-get install -y libpq-dev'
					 //sh 'pip3 install psycopg2'
					 sh 'sudo chmod 777 /home/pi/workspace/'
					 sh 'sudo chmod 777 /home/pi/sensor_test_auto/'
					 sh 'python3 -m  pytest -s /home/pi/workspace/pipeline_main/sensor_test_auto/test_suite/stability/test_log_validate_message.py  --html=/home/pi/workspace/pipeline_main/sensor_test_auto/reports/results.html'
				    }
		               }
		    }
		}
		stage('Result uploader') { 
	        steps { 
	            echo "A Stage to upload the result to GCP" 
	            slackSend color: '#BADA55', message: 'Hello User,Your test execution got over.Please check ur result here - https://netq.skylo.tech'
	        }
        }
    }
}
