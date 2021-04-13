# Motion-Control-Game

#### A few months ago I saw something similar to this on Linkedin that inspired me to work on the project. This project can be used to play any game in your PC or conrol any application the way you like by selecting the tracking object and then moving it around the boxes on the screen

## Getting Started

#### In order to start with the Motion Control Game just clone this repository. Open the main file in your Python IDE, create a virtual environment with Python version 3.6 and replace the names of each directory with your pc directories respectively .

#### Now install the packages provided in the requirements.txt by running pip install -r requirements.txt to install them all.

## How does it work?

#### Open the game with the link provided in the .txt file. Run the code in your IDE. A picture will be clicked. Keep an object you wish to track in the frame. Now select an area of the object. Start the game now you are ready to go.  

## Working Principal

#### Basically the idea is based on tracking down movements in real time and implementing a keypress as an output. The project is made using opencv and pyautogui as the main modules.Just after running the python script a picture will be clicked from the webcam.Then we mark down or select the portion of the object or the person in the frame that we wish to track.After clicking enter,a screen appears that is divide into different parts or lines and a blue circle pointing on the object that was selected for tracking the object where the middle portion resembles the nuetral or null. Now, whenever our tracking object moves towards any direction  the key of that direction is pressed using PYAUTOGUI.

## Contribution

#### Different laptops provide different fps and have different image quality as well. There are different trackers provided in the main code as well. Use them and experiment and see which one works better for you. Please feel free to contribute to the project and Pull Requests are open for everyone willing to improve upon the project.
