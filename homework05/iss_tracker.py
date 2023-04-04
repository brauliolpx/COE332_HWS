from flask import Flask,request,jsonify
import json
import requests
import xmltodict
import math
import requests
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
    global data
    offset = request.args.get('offset', 0)
    limit = request.args.get('limit', len(data['ndm']['oem']['body']['segment']['data']['stateVector']))
    try:
        offset = int(offset)
    except ValueError:
        return "Invalid offset  parameter; offset  must be an integer."
    try:
        limit = int(limit)
    except ValueError:
        return "Invalid limit parameter; limit must be an integer."

    end_index = offset + limit
    
    list_epochs = []
    for i in range(len(data['ndm']['oem']['body']['segment']['data']['stateVector'])):
      if i >= offset and i < end_index:
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
    global data
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
    global data
    for i in range(len(data['ndm']['oem']['body']['segment']['data']['stateVector'])):                  #iterates through the whole data set
        if data['ndm']['oem']['body']['segment']['data']['stateVector'][i]['EPOCH'] == epoch:           #checks the current value to the one given by the user and if equal it stores them
           x_dot = float(data['ndm']['oem']['body']['segment']['data']['stateVector'][i]['X_DOT']['#text'])
           y_dot = float (data['ndm']['oem']['body']['segment']['data']['stateVector'][i]['Y_DOT']['#text'])
           z_dot = float(data['ndm']['oem']['body']['segment']['data']['stateVector'][i]['Z_DOT']['#text'])

    instan_speed = math.sqrt(x_dot**2 + y_dot**2 + z_dot**2) #calculates the instantanoues speed by using math.sqrt buildin function

    return 'Instantaneous speed is: {} km/s \n'.format(instan_speed)

@app.route('/help', methods=['GET'])
def get_help():
    """ 
        get_help function that returns a help text for the user giving brief descriptions of all available routes (plus their methods) of the API

        Args: 
            No Args 

        Return: 
            help_string - a string containing the help text for each route
    """
    help_string = "Usage: GET /route\n\n"
    help_string += "Available routes:\n\n"
    help_string += "   /     -   Returns entire data set.\n\n"
    help_string += "   /help -   Returns help text (as a string) that briefly describes each route.\n\n"
    help_string += "   /epochs - Returns a list of all epochs in the data set.\n\n"
    help_string += "   /epochs?limit=int&offset=int -  modified list of Epochs given query parameters:limit value in form of an integer and a offset.\n\n"
    help_string += "   /epochs/<epoch> -  Return a list of state vectors containing the position and velocity for a specific Epoch from the data set, given a target Epoch value as a parameter.  \n\n"
    help_string += "   /epochs/<epoch>/speed - Return instantaneous speed for a specific Epoch in the data set. \n\n"
    help_string += "   /delete-data - Delete all data from the dictionary object. \n\n"
    help_string += "  /post-data - Reload the dictionary object with data from the web. \n\n"
    return help_string

@app.route('/delete-data', methods=['DELETE'])
def delete_data():
    """
        delete_data function that deletes the data from the dictionary data

        Args:
            No Args 

        Return:
            a string that indiocates the data have been deleted
    """
    data.clear()

    return "All data deleted successfully"
@app.route('/post-data', methods=['POST'])
def reload():
    """
        reload function reloads the dictionary object with data from the web
        
        Args:
            No args 
        
        Return:
            data - dictionary containing the data from the web

    """
    global data 
    response = requests.get(url="https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml")
    if response.status_code == 200:
        data = xmltodict.parse(response.content)
        return jsonify({'message': 'Data restored successfully'})
    else:
        return jsonify({'message': 'Failed to restore data'})

# the next statement should usually appear at the bottom of a flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
