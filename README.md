IoT-Dataset Docker network
===

![iot_dataset_docker](https://user-images.githubusercontent.com/10727813/123518139-3746b880-d6ad-11eb-9996-cbfb4de186e4.png)

1. Clone the repository using the `--recursive` option to also clone the project submodules:
```
$ git clone --recursive https://github.com/unibuc-cs/IoT-Dataset-Dockerized.git
```

2. Build the project images:
```
$ docker-compose build --parallel
```

3. Run `docker-compose up -d` to start the network

In case you've alreay cloned this repo and want to pull the latest changes,
run the following commands:
```
git pull
git submodule update --init --recursive
```

## Notes
1. All applications start with a delay of 1 second
2. There is a single MQTT server runing on the network (hostname `mqtt_server`). All applications connect to it.
3. Check if everything started correctly by running `./test.sh`
4. `smarteeth` is not working right now and it wasn't added to `docker-compose.yml`

## TODOs

 - [ ] fix `smarteeth`
