# Implementing the model
This repository includes the files necessary to reproduce the steps that were followed for the implementation of the LSTM model, from teleoperating the robot through the training scenarios and recording its LiDAR readings, position inside the Motion Capture system, target point and linear and angular velocities, to training, validating and testing the LSTM model.

## Relevant files
You can find videos of the model being tested, the presentation for the project, and relevant .csv files in [this](https://drive.google.com/drive/folders/1DtHG-nLFXtRnXHjDUmPfr6xOAHteYCBR?usp=drive_link) Drive folder. In there, you'll find a file named "Dataset for training the model.
csv", containing the data obtained from the 100 user-operated examples, which was used for training the LSTM neural network. The resulting model is in the file "trainingDA.h5"

## TurtleBot3 Waffle Pi assembly and configuration
The TurtleBot3 e-Manual by ROBOTIS containing all relevant information about the robot can be found [here](https://emanual.robotis.com/docs/en/platform/turtlebot3/features/). In this page, you can find a Quick Start Guide. This project was run using ROS Noetic on Ubuntu 20.04, which is why the "Noetic" option should be selected in every e-Manual section that is consulted, as is shown in the image below.
![Screenshot from 2024-06-07 20-00-58](https://github.com/esmemt/drone_arena/assets/153858248/aaf11b2b-a12f-4e85-8dbd-4dfe89055032)

The model used for the experiments is the TurtleBot3 Waffle Pi, which is the hardware assembly manual that will be needed. The manual can be found [here](https://www.robotis.com/service/download.php?no=750)

**Note**: the TurtleBot3 robots at Tecnológico de Monterrey, Campus Querétaro, are already assembled and the with the boards configured, which is why it is only necessary to follow sections **3.2.6. Configure the WiFi Network Setting** and **3.2.7. ROS Network Configuration** of the [**SBC setup**](https://emanual.robotis.com/docs/en/platform/turtlebot3/sbc_setup/#sbc-setup) section of the e-Manual, so the robots can connect to the computer that will control them and to the required WiFi network.

## OptiTrack Motion Capture System
Note: This section only applies to the Motion Capture System located at Tecnológico de Monterrey, Campus Querétaro, known as the Drone Arena.

To start up the motion capture system, first it is imṕortant to make sure that the cameras are plugged in to the multi-contact connectors and that the connectors are turned on, as shown in the images below. These connectors are located in two of the arena's corners, the one closest to the cabin door and the one diagonally across from the first one.

FOTOS MULTICONTACTOS

Once the cameras are powered on, it is necessary to go into the cabin and turn on the computer that is closest to the door, along with its two monitors. An image of the computer is shown below

FOTO COMPU

For starting up Motive 2.2, the motion capture software, you can follow [this]() tutorial, recorded at the Drone Arena.

Once the robots are set up, the rigid body is created and the data from Motive is being streamed, you can begin operating the robot through the different scenarios to record the required data.

## Training the robot
