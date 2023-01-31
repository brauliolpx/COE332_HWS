INVESTIGATION OF FIVE METEORITE SITES IN SYRTIS MAJOR

This folder contains two python files,"generate_sites.py" and "calculate_trip.py". The purpose of these files is to generate random landing sites for a hypothetical space mission and calculate the time required to visit and take samples from these sites.


generate_sites.py
This file generates five random pairs of latitudes and longitudes within the range of 16.0 - 18.0 degrees North and 82.0 - 84.0 degrees East respectively.
For each landing site, a random meteorite composition is also chosen from the list ["stony", "iron", "stony-iron"]. All of this data is assembled into a dictionary and saved as a JSON file using the Python json library. This file would later be used on the calculate_trip.py file.
 
calculate_trip.py
This file reads the data generated from generate_sites.py and calculates the time 
required to visit and take samples from the five sites. It prints the descriptive information of each leg following by the time traveled
and time of the sample.

--------------------
Installation 

On terminal first you will need to generate the sites data to do that you will execute generate_sites.py 
using the following command.

terminal: python3 generate_sites.py 

once clicking enter you will find a new file on your folder called "sites_data.json" which stores the random data. 

Then type to run the other file type 

terminal: python3 calculate_trip.py 

If you are able to see on the terminal the output of the information that means that you did everything correct. 
the intended output shoul look as follows:

leg = 1, time to travel = 11.75 hr, time to sample = 1 hr
leg = 2, time to travel = 3.43 hr, time to sample = 2 hr
leg = 3, time to travel = 4.53 hr, time to sample = 1 hr
leg = 4, time to travel = 6.04 hr, time to sample = 2 hr
leg = 5, time to travel = 10.43 hr, time to sample = 3 hr

===============================
number of legs = 5, total time elapsed = 45.17 hr 

*Note that this is using random data once doing all the process again the output would be different each time*
*If you are able to see from the example the on each leg is from each travel and it shows the time traveled to each site and the time for the sample
at the end it will give the user the recap of the whole travel mission*

In summary, these two python files provide a solution for generating random landing sites and calculating the time required to visit and take samples from these sites. This information can be used to plan a hypothetical space mission.
