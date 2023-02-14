import requests
import json 
import math 


def turbidity(calibration_cons:float , detector_current:float) -> float:
   """ It calculates the turbidity of water  
        using the data imported from the json file 

        calibration_con 
            is the calibration of the water 

        detector_current 
            is ninety degree detector current. 

   """
   turb = calibration_cons * detector_current
    
   return turb 
 
def threshold(current_turbidity:float) -> float :
    """Calculates minimum time for the threshold 
        
            Takes in the current turbidity as current_turbidity

    
    """

    ts = 1.0 #threshold for safe water 
    d = 0.02 #this is the decay facor for the safe watwer 
    b = 0 #indicates the hours elapsed 

    while (ts < current_turbidity*(1-d)**b):
        b = b+1

    return b 


def main():
    turbidity_data = requests.get(url='https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json') #gets the data from the web using the request get functiom
    turbidity_data.status_code
    t_data = turbidity_data.json() #stores the data into a json file        

    results_list = []
    i = len(t_data['turbidity_data'])
    a = 0
    for i in range (i-1,0,-1):

        calibration = t_data['turbidity_data'][i]['calibration_constant']
        detector = t_data['turbidity_data'][i]['detector_current']
        get_turb = turbidity(calibration,detector)
        results_list.append(get_turb)
        threshold(get_turb)
        a +=1 
        
        if a == 5:
            average = sum(results_list)/5 #gets the average turbidity of the 5 recent measuremts by getting the sum and dividing by 5 
            break
        
     
    print("Average turbidity based on most recent five measurements = " + str(average) + " NTU") 
    if average > 1 :    #checks the average is greater than the threshold
        print("Warning: Turbidity is above threshold for safe use")
        print("Minimum time required to return below a safe threshold " + str(threshold(average)) + " hours" )
    else: 
        print("Info: Turbidity is below threshold for safe use")
        print("Minimum time required to return below a safe threshold = 0 hours")
        


if __name__ == '__main__':
    main()
