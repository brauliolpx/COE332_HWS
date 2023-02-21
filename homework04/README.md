BUDDY FLASK - POSITIONAL AND VELOCITY DATA 

This project builds a flask application using an abundance of interesting positional and velocity data for the International Space Station (ISS). The goal is to create a Flask application that queries and returns useful information from the ISS data collection.
This folder contains a flask python script "iss_tracker.py" where the app is build 

iss_tracker.py: The Flask application for querying the velocity and position of the International Space Station. The program should load the data from the URL below and provide it to the user using properly constructed routes. 
URL: https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml
The first route '/' returns the entire data set
'/epochs' returns a list of all Epochs in the data set
'/epochs/<epoch>' returns the state vectors for a specific Epoch from the data set
'/epochs/<epoch>/speed' Instantaneous speed for a specific Epoch in the data set

To access the data just copy the URL above to your a search engine 

--------------------
Installation 

First you will need to install the requirements the script neeeds in your terminal.
The Flask library is not part of the Python standard library but can be installed with standard tools

Terminal: pip3 install --user flask

You should get a 'Successfully installed flask-2.x.x' message

Once you installed flask you need to open a new terminal tab because you need to see that the flass application is running.
On the terminal type:

Terminal: flask --app iss_tracker --debug run
The expected output should be 
* Serving Flask app 'app'
* Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
* Running on http://127.0.0.1:5000
Press CTRL+C to quit
* Restarting with stat
* Debugger is active!
* Debugger PIN: 268-620-354

now on the second tab you can curl each route to see the outcomes 
if you curl localhost:5000/ in the terminal it will list all the data set gotten from the link and return a dictionary containging all of the informartion.
By curl localhost:5000/epochs it will list all epochs from the data set. For example...
...
"2023-063T11:55:00.000Z",
"2023-063T11:59:00.000Z",
"2023-063T12:00:00.000Z"

each epoch is a dictionary containing its state vectors 

If you want to access an specific epoch get the time you want the route is /epochs/<epoch> for this case I will show the last one.
By curl localhost:5000/epochs/2023-063T12:00:00.000Z that will return the X,Y,Z coordinates and its dot velocities. For example:
X: 2820.04422055639 km,
Y: -5957.89709645725 km,
Z: 1652.0698653803699 km,
X_DOT: 5.0375825820999403 km/s,
Y_DOT: 0.78494316057540003 km/s,
Z_DOT: -5.7191913150960803 km/s

By choosing an specific time it will return each state Vectors from the data set 

Lastly the route curl localhost:5000/epochs/<epoch>/speed gets the speed for that specific epoch value for example the last epoch data set
curl localhost:5000/epochs/2023-063T12:00:00.000Z/speed 
returns: 
Instantaneous speed is: 7.661757196327827 km/s

That shows the instantaneous speed for the specific epoch value. 
