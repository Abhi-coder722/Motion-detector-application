# Motion-detector-application

This is an application which detects the motion in a live User Camera, i.e. the movement in the object/ person.



DOCUMENTATION:
**************
The above file contains basically two python files , a csv file and an HTML file(which is not required initially but it will be created after executing the plotting.py file in your directory ).



app2.py
*******

Overview:

The app contaions various modules in it like datetime,re,cv2,and pandas .

The motive of the this application is to create a frame which will detect motion if there is any from the starting frame and it will enclose it in an rectangular green box .
It will save the date and time of the motion which is done  that frame in a Times.csv file .


Description:

After importing the basic modules cv2,datetime,time and pandas we will create a first frame from which we will detect that if there is any change in the frame .
We will also create a times array to append the time and we will create a data frame with two columns 'Start' and 'End'.
And then we start capturing the video using the cv2.VideoCapture() method, and we will stop time for a second.


Then , We start a while loop with an exit condition as the 'q' button i.e. Whenever we will press it it will close all the frames .
 We convert our frame to gray and then we blur it and if the first frame is none assign gray as the first frame and then using continue start the loop again.

And then we store the absolute difference of the pixels in a delta_frame variable.
Then, we create an threshold image of the delta_frame and usig the dilate method of cv2 weapply morphological filters to it .
Then we find the contours of the thres_frame using cv2.findContours() method with some specific parameters.
