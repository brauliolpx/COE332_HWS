from flask import Flask
import json
import requests
import xmltodict
import math

app = Flask(__name__)
response = requests.get(url="https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml")
data = xmltodict.parse(response.content)

@app.route('/', methods=['GET'])
def entire_dataset():
    """
    The function returns the all data collected collected by calling data dictionary ouside the function
   
    Args:
        No Args
    
    Return: 
        returns "data" which is a list of dictionary set outside the function

    """

    return data

@app.route('/epochs', methods=['GET'])
def get_epochs():
    """
        get_epochs function gets all the epochs from the data set and lits them for the user 

        Args:
            No Args

        Return:
            list_epochs - a list of dictionatires containing all epochs from the data set
    """

    list_epochs = []
    for i in range(len(data['ndm']['oem']['body']['segment']['data']['stateVector'])):   
  
        list_epochs.append(data['ndm']['oem']['body']['segment']['data']['stateVector'][i]['EPOCH'])
    
    return list_epochs
   
@app.route('/epochs/<epoch>',  methods=['GET'])
def epochs_state(epoch):
    """
        epochs_state function takes in a specific epoch given by the user and returns its coordinates usig the data set

        Args:
            epoch - a string of EPOCH value for a specific time in the data site 
        
        Return:
            a string showing the location of each site given the x , y and z coordinates     
    """

    for i in range(len(data['ndm']['oem']['body']['segment']['data']['stateVector'])):               #iterates through the whole data set
        if data['ndm']['oem']['body']['segment']['data']['stateVector'][i]['EPOCH'] == epoch:        #checks the current value to the one given by the user and if equal it stores them 
           x_value = data['ndm']['oem']['body']['segment']['data']['stateVector'][i]['X']['#text']  
           y_value = data['ndm']['oem']['body']['segment']['data']['stateVector'][i]['Y']['#text']
           z_value = data['ndm']['oem']['body']['segment']['data']['stateVector'][i]['Z']['#text']
           x_dot = data['ndm']['oem']['body']['segment']['data']['stateVector'][i]['X_DOT']['#text']
           y_dot = data['ndm']['oem']['body']['segment']['data']['stateVector'][i]['Y_DOT']['#text']
           z_dot = data['ndm']['oem']['body']['segment']['data']['stateVector'][i]['Z_DOT']['#text']
           break
    
    
    return 'X: {} km,\nY: {} km,\nZ: {} km,\nX_DOT: {} km/s,\nY_DOT: {} km/s,\nZ_DOT: {} km/s\n'.format(x_value,y_value,z_value,x_dot,y_dot,z_dot) 

@app.route('/epochs/<epoch>/speed',  methods=['GET'])
def Instantaneous_speed(epoch):
    """
        Instantaneous_speed function that gives the speed of an specific EPOCH from the data set

        Args:
            epoch - a string of EPOCH value for a specific time in the data site

        Return:
            a string giving the instantaneous speed by formating a float value by a string 
    """

    for i in range(len(data['ndm']['oem']['body']['segment']['data']['stateVector'])):                  #iterates through the whole data set
        if data['ndm']['oem']['body']['segment']['data']['stateVector'][i]['EPOCH'] == epoch:           #checks the current value to the one given by the user and if equal it stores them
           x_dot = float(data['ndm']['oem']['body']['segment']['data']['stateVector'][i]['X_DOT']['#text']) 
           y_dot = float (data['ndm']['oem']['body']['segment']['data']['stateVector'][i]['Y_DOT']['#text'])
           z_dot = float(data['ndm']['oem']['body']['segment']['data']['stateVector'][i]['Z_DOT']['#text'])
    
    instan_speed = math.sqrt(x_dot**2 + y_dot**2 + z_dot**2) #calculates the instantanoues speed by using math.sqrt buildin function

    return 'Instantaneous speed is: {} km/s \n'.format(instan_speed)

# the next statement should usually appear at the bottom of a flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
