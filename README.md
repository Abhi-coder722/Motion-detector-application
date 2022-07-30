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
Then we find the contours (and store it in cnts variable ) of the thres_frame using cv2.findContours() method with some specific parameters.

We start a for loop for contour in cnts and if the contour is less than 5000 it will contiue to the loop block again, and if there is any motion detected it will change the status from zero to 1 .
If in the loop contour is greater than 5000 then it will pack it in an rectange . So, for finding the coordinates of rectangle we can use cv2.boundingRect() function using this we will get the dimensions of the diagonal of the rectangle and we will pack it.

We append the status i.e. either 0 or 1 to status_list list and then we slice it to the last two as the last two are only required to see either status moed from 1to 0 or 0 to 1 or it is same using that we will append the date time as of the current time at that moment using the datetime function..

Then, we'll show all the four frames . Then, we will keep our exiting condition .


Outside the loop we will display the times and we will append the times to the data frame .
We will pass the data frame to the csv file and then we release the video and destroy all the windows..

Now, we are oing to use this file in our plotting.py file..



plotting.py
***********


This file is used to plot the returned date and time by the app2.py in a graph using the bokeh module .

Here we import the dataframe variable df from the app2.py application.

We'll read the start and end string and we will display it and then we map the data columnwise using the ColumnDataSource.
Using the figure method of bokeh module ,
    we'll set the width, title and etc.. of our graph.
Using the hover tool we will add our start , end time to our graph variable and we pack it in a quadrilateral..
our output file will be an html file . It will create an html file in your directory with the same name we can open it and see the graph .







Motive of the application Motion detector :
********************************************


