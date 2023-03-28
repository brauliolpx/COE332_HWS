Say It Ain’t Genes

The project involves creating a web application using Flask, which will use data from the Human Genome Organization (HUGO). HUGO is a non-profit organization that assigns unique and meaningful names to genes through the HUGO Gene Nomenclature Committee (HGNC). The data from HGNC will be downloaded and stored in a Redis database through the Flask interface. 

This Folder contains a flask python script "gene_api.py" where the app is build & contains a "dockerfile" to containerize the gene_api.py script and a docker-compose.yml to automate the deployment of the app

"gene_api.py" - The Flask application for querying the HGNC data on this page: https://www.genenames.org/download/archive/
This scrpit contains 3 routes for the user to navigate and explore. /data A POST request to /data should load the HGNC data to a Redis database. Use the Python requests library to get the data directly from the web. A GET request to /data should read all data out of Redis and return it as a JSON list. A DELETE request to /data should delete all data from Redis. it also includes The "/genes" route, which will return a list of all "hgnc_id" fields from the HGNC dataset in JSON format. "hgnc_id" is a unique identifier for each gene. The "/genes/<hgnc_id>" route, which will return all data associated with a given "hgnc_id". However, the application needs to handle cases where an invalid gene ID is provided by the user, as well as sparse data returned by the query. An example query to this route might look like: "/genes/HGNC:5"

Dockerfile: 
From python:3.8.10

RUN pip install Flask==2.2.2
RUN pip3 install json==0.13.0
RUN pip3 install requests==2.22.0
RUN pip3 install requests==4.5.1

COPY genes_api.py /genes_api.py

CMD ["python", "genes_api.py"]


docker-compose.yaml 

To access the data just copy the URL above to your a search engine

----------------------------------------------------
Installation

First you will need to install the requirements the script neeeds in your terminal. The Flask library is not part of the Python standard library but can be installed with standard tools

Terminal: pip3 install --user flask

You will also need to install redis 
Terminal: pip3 install --user redis

To start the redis application make sure to use the folowing command:

Terminal: docker run -d -p 6379:6379 -v $(pwd)/data:/data:rw redis:7 --save 1 1

Now you are ready to run gene_api.py by using python3 


Once the server is running you should get output like:
 * Serving Flask app 'gene_api'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://129.114.38.232:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 142-870-111

This means that it is running. 

RUNNING THE ROUTES 
Now open a new tab to start curling into the application

 if you curl localhost:5000/data in the terminal it will list all the data set gotten from the link and return a dictionary containging all of the informartion. 

This route has 3 methods GET, POST and DELETE 

if curl localhost:5000/data automatically gets the method GET and it returns all the data set 
if curl localhost:5000/data -X DELETE  automatically gets the method DELETE and it deletes the data set from redis 
ex:
data was deleted from redis 

if curl localhost:5000/data -X POST updates the data into radis 


------------------------------------------------------------------------------------


Dockerfile && Docker Hub

First you will need to login Terminal: docker login username: ** password: **

After sign in you can pull the docker image from docker pull brauliolpx/gene_api:hw06

To run the image type Terminal: docker run -it --rm -p 5000:5000 brauliolpx/gene_api:hw06 The intended output is
Serving Flask app 'gene_api'
Debug mode: on WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
Running on all addresses (0.0.0.0)
Running on http://127.0.0.1:5000
Running on http://172.17.0.2:5000 Press CTRL+C to quit
Restarting with stat
Debugger is active!
Debugger PIN: 128-187-211
There it shows that the dockerfile is running as expected and you can curl each routes as the same from the flask application

You could also build a new image from the Dockerfile by adding new ports After doing that just

docker build -t brauliolpx/gene_api:hw06


---------------------------
Docker compose Installation

when having the composer just type on terminal

terminal: docker-compose up


--------------------------
Understanding data 
The JSON file contains a large amount of data, including gene symbols, names, aliases, descriptions, chromosome locations, and more.

Each entry in the JSON file represents a single gene and includes a variety of information about that gene. The most important piece of information for each gene is its ID, whih is a unique identifier. 

The JSON file also includes information about the location of each gene on the human genome. This includes the chromosome on which the gene is located, as well as the start and end positions of the gene within the chromosome.

Overall, the HGNC JSON file is a valuable resource for researchers and developers working with human genomics data. By providing a standardized set of gene symbols and names, the HGNC helps to ensure consistency and accuracy in scientific research and communication.


