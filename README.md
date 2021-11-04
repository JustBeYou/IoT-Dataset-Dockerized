IoT-Dataset Docker network
===
This is the main repository of our dataset of IoT applications. It contains 5 mock smart home apps and a hub. 

![image](https://user-images.githubusercontent.com/10727813/140134084-657e0e02-774b-4fbe-8cf5-a9d9e5e856aa.png)

Run `docker-compose up -d` to start the network. Docker will pull the images for each application to your local machine.

If you want to interact with the applications, you can change the code of the [hub app](https://github.com/unibuc-cs/iot-dataset-hub-app), rebuild the image and restart the composer. If you want live updates, mount the directory of the hub app as a volume inside the docker container. (TODO add instructions for this)

## IoT applications
* https://github.com/unibuc-cs/iot-dataset-hub-app (the hub)
* https://github.com/unibuc-cs/FlowerPower
* https://github.com/unibuc-cs/smarteeth
* https://github.com/unibuc-cs/SmartKettle
* https://github.com/unibuc-cs/SmartTV-Alpha-X
* https://github.com/unibuc-cs/WindWow

## Notes
1. All applications start with a delay of 1 second
2. There is a single MQTT server runing on the network (hostname `mqtt_server`). All applications connect to it.
3. Check if everything started correctly by running `./test.sh`
