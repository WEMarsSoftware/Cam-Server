# Camera Server

 A dedicated camera server for use on the WEMars rover, to stream video data

### Requirements
* Python 2
* Intel RealSense Camera
* Flask


### Installation

#### Part 1 - Intel RealSense installation

Mac OSX installation:

```
$ brew install cmake pkg-config libusb glfw
$ git clone https://github.com/IntelRealSense/librealsense.git
$ cd librealsense
$ git checkout legacy
$ mkdir build && cd build

$ cmake ../
$ make && make install
```

#### Part 2 - Server dependencies
```
$ pip install -r requirments.txt
```

### Running 

```
$ python server.py
```

### Usage

Example url:

```
localhost:5000/fps
```

| Endpoint    | Method |Params          |
|-------------|--------|----------------|
| /fps        | POST   | "fps":"30"		|
| /motionJpeg | GET    |                |
| /           |        | Test Page      |


