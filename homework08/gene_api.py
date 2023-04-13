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
    redis_ip = os.environ.get('REDIS_IP')
    if not redis_ip:
        raise Exception()
    rd=redis.Redis(host=redis_ip, port=6379, db=0)
    return rd

def get_redis_image_db():
    redis_ip = os.environ.get('REDIS-IP')
    if not redis_ip:
        raise Exception()
    return redis.Redis(host=redis_ip, port=6379, db=1)

rd = get_redis_client()

rd_image = get_redis_image_db()



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



@app.route('/image', methods = ['POST', 'GET', 'DELETE'])
def get_image():
    """
        get_image function gets the image and uploads it into redis  run some matplotlib code to create a simple plot of that data
        
        Args:
            No Args

        Return: 
            The "DELETE" command will produce a string indicating the deletion of data.
            The "POST" method will return a string verifying the data provided.
            The "GET" command retrieves data from the Redis database in the form of a list of dictionaries.

    """
    if request.method == 'GET':
        plot_bytes = rd_image.get("Plot")


        buf = io.BytesIO(plot_bytes)
        buf.seek(0)

        return send_file(buf, mimetype='image/png')


    elif request.method == 'POST':
        daysSince2000List = []
        HGNClist = []
        for item in rd.keys():

            value = rd.get(item).decode('utf-8')
            value = json.loads(value)
            date_str = value["date_approved_reserved"]
            parsed_date = datetime.strptime(date_str, "%Y-%m-%d").date()

            reference_date = date(2000, 1, 1)
            delta = parsed_date - reference_date
            days_since_2000 = delta.days
            daysSince2000List.append(days_since_2000)
            HGNClist.append(int(value["hgnc_id"][5:]))

        fig, ax = plt.subplots()
        ax.scatter(daysSince2000List, HGNClist,s=5,alpha=0.5)
        ax.set_title('ID Number vs Date Approved')
        ax.set_xlabel('Day approved since 2000')
        ax.set_ylabel('HGNC ID number')

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)

        rd_image.set("plot", buf.getvalue())

        return 'Posted data\n'

    elif request.method == 'DELETE':
        rd_image.flushdb()
        return f'The Data has been deleted successfully. There are {len(rd.keys())} plots\n'

    else:
        return 'please try again, the method did not work\n'



# the next statement should usually appear at the bottom of a flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
