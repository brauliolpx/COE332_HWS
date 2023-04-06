from flask import Flask,request,jsonify
import json
import redis 
import requests

app = Flask(__name__)


def get_redis_client():
    """
        get_redis_client - function that constantly gest the redis running 
        Args:
            No Args
        
        Return:
            redis.Redis(host='127.0.0.1', port=6379, db=0, decode_responses=True)
    """

    return redis.Redis(host='127.0.0.1', port=6379, db=0, decode_responses=True)

rd = get_redis_client()


@app.route('/data', methods=['POST','GET', 'DELETE'])
def handle_data():
    """
    handle_data - function that has 3 methods 'POST','GET', 'DELETE' which gets the data, post the data and deletes the data from redis
    Args: 
        No Args
    Return: 
        if using GET request you should get output_list as the return value if using other method should receive a string
    """

    if request.method == 'GET': 
        output_list = []
        for item in rd.keys():
            output_list.append(rd.hgetall(item))
        return output_list 

    elif request.method == 'POST':
        response = requests.get(url='https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json')        
        data = response.json()['response']['docs']
        for item in data:
            rd.hset('hgnc_data',item['hgnc_id'],str(item))
        return 'Data loaded into Redis.\n'

            
    elif request.method == 'DELETE':

        rd.flushdb()

        return 'data deleted \n' 

    else:

        return 'The method you tried does not work \n'


@app.route('/genes', methods=['GET'])
def get_hgnc_id():
    """
        get_hgnc_id - function that gets all 'hgnc_id' and stores it into a dictionary 
        Args: 
            No args 
        Return:
            data - where all 'hgnc_id is stored 
    """
    data = handle_data()
    for item in rd.hkeys('hgnc_data'):
        data.append(item)
    return data

@app.route('/genes/<hgnc_id>', methods=['GET'])
def specificgene(hgnc_id):
    """
        specificgene - function that gets the hgnc_id data from the data set
        Args:
            hgnc_id
        Return: 
            output_dict - dicitonary with all the information about the specific gene
    """

    if rd.hexists('hgnc_data', hgnc_id):
        output_dict = rd.hgetall(hgnc_id)
        return jsonify(output_dict)
    else:
        return jsonify({'error': 'Invalid hgnc_id'}), 404



# the next statement should usually appear at the bottom of a flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
