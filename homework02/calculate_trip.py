import json 
import random 
import math 

mars_radius = 3389.5    # km
def time_to_sample(the_composition):
    
    if (len(the_composition) == 5): #stony has a lenght of 5 if 5 then the time to samp would be 1
        time_samp = 1 
    
    elif (len(the_composition) == 4): #iron has a lenght of 4 if 4 then the time to samp would be 2
        time_samp = 2 

    else:                   #otherwise is stony iron then returns 3 
        time_samp = 3 
    
    return time_samp


def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:               #calculates the distance between two points between points
    lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2] )
    d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
    return ( mars_radius * d_sigma )


def time_traveled(distance_traveled):
    speed = 10 #km per hour 
    time = distance_traveled/speed  
    
    return time


def main():
    
    with open('sites_data.json', 'r') as f:
        ml_data = json.load(f)
   
    starting_latitude = 16.0
    starting_longitude = 82.0
    total_time = 0
    for i in range(len(ml_data['sites'])): 
        
        distance = calc_gcd(starting_latitude,starting_longitude, ml_data['sites'][i]['latitude'], ml_data['sites'][i]['longitude']) #gets the ditance using the function
        total_time = total_time + time_traveled(distance) + time_to_sample(ml_data['sites'][i]['composition'])
        print("leg = " + str(i+1) + ", "  + "time to travel = " + str(time_traveled(distance)) + " hr" + ", "  + "time to sample = " + str (time_to_sample(ml_data['sites'][i]['composition'])) + " hr" )
        starting_latitude = ml_data['sites'][i]['latitude']
        starting_longitude = ml_data['sites'][i]['longitude']
        
    print("==============================================")
    print("number legs = " + str(i+1) +  " , total time elapsed = " + str(total_time) + " hr")


if __name__ == '__main__':
    main()
