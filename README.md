# Isaac-Sim-NoMaD

### Driving the robot to collect imgs
Inside the visualnav-transformer/deployment/src/ directory:
```
sh my_record_bag.sh
```


### Record as a Rosbag
```
cd ../topomaps/bags

rosbag record /rgb /odom -O warehouse_turtlebot 
```

When have finsihed kill the ros bag recording immediately with ctrl+c.

### Create topological map
Inside the visualnav-transformer/deployment/src/ directory:

```
sh my_create_topomap.sh <topomap_name> <bag_filename> <rosbag_playback_rate>

sh my_create_topomap.sh warehouse_turtlebot warehouse_turtlebot 1.5
```

### Navigate with pre-trained model
Inside the visualnav-transformer/deployment/src/ directory:
```
sh my_navigate.sh
```
