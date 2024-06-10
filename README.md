# Implementing the model
This repository includes the files necessary to reproduce the steps that were followed for the implementation of the LSTM model, from teleoperating the robot through the training scenarios and recording its LiDAR readings, position inside the Motion Capture system, target point and linear and angular velocities, to training, validating and testing the LSTM model.

## Relevant files
You can find videos of the model being tested, the presentation for the project, and relevant files in [this](https://drive.google.com/drive/folders/1DtHG-nLFXtRnXHjDUmPfr6xOAHteYCBR?usp=drive_link) Drive folder. In there, you'll find a file named ["trainingDA.csv"](https://drive.google.com/file/d/1z7ErxGBDruRpT1ESTPZZuoDeUqw-MjMl/view?usp=drive_link), containing the data obtained from the 100 user-operated examples, which was used for training the LSTM neural network. The resulting model is in the file ["trainingDA.h5".](https://drive.google.com/file/d/1LnEibYuDtMk0rY3E8viuKqBrEvWyWOf0/view?usp=drive_link)

## TurtleBot3 Waffle Pi assembly and configuration
The TurtleBot3 e-Manual by ROBOTIS containing all relevant information about the robot can be found [here](https://emanual.robotis.com/docs/en/platform/turtlebot3/features/). On this page, you can find a Quick Start Guide. This project was run using ROS Noetic on Ubuntu 20.04, which is why the "Noetic" option should be selected in every e-Manual section that is consulted, as shown in the image below.
![Screenshot from 2024-06-07 20-00-58](https://github.com/esmemt/drone_arena/assets/153858248/aaf11b2b-a12f-4e85-8dbd-4dfe89055032)

The model used for the experiments is the TurtleBot3 Waffle Pi, which is the hardware assembly manual that will be needed. The manual can be found [here](https://www.robotis.com/service/download.php?no=750)

**Note**: the TurtleBot3 robots at Tecnológico de Monterrey, Campus Querétaro, are already assembled and with the boards configured, which is why it is only necessary to follow sections **3.2.6. Configure the WiFi Network Setting** and **3.2.7. ROS Network Configuration** of the [**SBC setup**](https://emanual.robotis.com/docs/en/platform/turtlebot3/sbc_setup/#sbc-setup) section of the e-Manual, so the robots can connect to the computer that will control them and to the required WiFi network.

## OptiTrack Motion Capture System
Note: This section only applies to the Motion Capture System located at Tecnológico de Monterrey, Campus Querétaro, known as the Drone Arena.

To start up the motion capture system, first, it is important to make sure that the power cables for the cameras are plugged into the multi-contact connectors and that the connectors are turned on, as shown in the images below. These connectors are located in two of the arena's corners, the one closest to the cabin door and the one diagonally across from the first one.

![IMG_8976 de tamaño pequeño](https://github.com/esmemt/drone_arena/assets/153858248/33be4a4d-0aed-4d6d-a829-032606114344)     ![IMG_8977 de tamaño pequeño](https://github.com/esmemt/drone_arena/assets/153858248/7cd64c4a-7d93-4b10-ad75-b5ef8d709c0f)

Once the cameras are powered on, it is necessary to go into the cabin and turn on the computer that is closest to the door, along with its two monitors. An image of the computer is shown below

![IMG_8978 de tamaño pequeño](https://github.com/esmemt/drone_arena/assets/153858248/40025439-a91f-476e-a464-f7ea44228009)

For starting up Motive 2.2, the motion capture software, you can follow [this](https://drive.google.com/file/d/1ap2mmEBQ_HVClJv4Cm4d9SW4KihixuoZ/view?usp=drive_link) tutorial, recorded at the Drone Arena.

Once the obstacles for the mobile robot are in place, the robots are set up, the rigid body is created and the data from Motive is being streamed, you can begin operating the robot through the different scenarios to record the required data.

## Training the robot
To train the model, it is first necessary to operate the robot through the different scenarios and record the data from these examples. To do so, the file "get_values.py" needs to be launched. The TP_x and TP_y values in this script will need to be changed according to the target point for each training scenario. It is also important to note that, since the LiDAR readings from the mobile robot are filtered, the script "laser_publisher.py" must be run first. [This](https://drive.google.com/file/d/1VZY8DLrLVaV9Du0GkixIPyyfkSfRQfWU/view?usp=drive_link) video shows every command that must be run on the Ubuntu terminal to record the data from each user-operated example, from connecting to the robots, starting the trajectory of the dynamic obstacle, teleoperating the mobile robot and recording the data.
Scenarios 2 and 3 use the "obstacle.py" script for the trajectory of the dynamic obstacle, Scenario 4 uses "obstacleL.py", and Scenario 5 uses "obstacleS.py".

## Training and validating the model
Once the robot has been operated by the user through the five different scenarios, twenty times per scenario, and the data has been recorded to the same .csv file, it is necessary to train the LSTM model. This is done by running the "model_training_arena.py" script, which creates a .h5 file with the final model. Once the model is ready, it can be validated by running the "model_validating_arena.py" script. This code provides the validation accuracy for the model by comparing it to the original dataset and obtains two comparative plots: one for the human-driver linear velocity vs the LSTM predicted linear velocity and one for the human-driver vs LSTM predicted angular velocities.

## Testing the model
Once the model has been trained and validated, it can be tested in the different training scenarios. This is done by running the "model_testing_arena.py", script that also needs modifying of the TP_x and TP_y values according to the goal point of the navigation scenario that is being tested. [This](https://drive.google.com/file/d/1YZVJ_7W6lQmDM3hiBaFwlxJlHttn8MrY/view?usp=drive_link) video shows the commands that need to be run on the terminal for testing the model. The mobile obstacle trajectory code to be run will depend on the scenario being tested, as listed in the **Training the robot** section.

## Extras
The documentation for the "natnet_ros.launch" file can be found in [this](https://github.com/L2S-lab/natnet_ros_cpp) repository, containing instructions on downloading and running the package. This is the driver that migrates the data regarding the mobile robot's position from the Motive 2.2 software.

The script "laser_scan_subscriber.py" can be used to test if the "laser_publisher.py" script is functioning correctly.
