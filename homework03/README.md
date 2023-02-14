The World Has Turned and Left Me Turbid

This project simmulates the aftermath of collecting data from mars using the previous project
This folder contains twp python files "analyze_water.py" and "test_analyze_water.py" 
The purpose of this project is to check and analyze the latest water quality data. 

analyze_water.py: This file scans the water quality data set and displays three important pieces of information on the screen: (1) the current water turbidity (as determined by the average of the last five data points), (2) whether that turbidity is below a safe threshold, and (3) the minimum time needed for turbidity to drop underneath the safe threshold (if it is already below the safe threshold, the script would report "0 hours" 

test_analyze_water.py: File that takes in the functions written on the first part and writes a unit test to check
that the code is working as expected.

---------------------------
Installation 

first you will need to install the requirements the script neeeds in your terminal.
therefore on terminal you need to install the requests library as that ios where we get our data

terminal: pip3 install --user requests

Once installed you are set to run the first part of the project wich analyses the data
On the terminal type

Terminal: python3 analyze_water.py

The expected outputs gives information of the water collected you should expected one of those two outcomes as eachour the data collected gets  analysed and it should look as follows:

======================
Average turbidity based on most recent five measurements = 1.1992 NTU
Warning: Turbidity is above threshold for safe use
Minimum time required to return below a safe threshold = 8.99 hours

or 

Average turbidity based on most recent five measurements = 0.9852 NTU
Info: Turbidity is below threshold for safe use
Minimum time required to return below a safe threshold = 0 hours


If we get that the aveage turbidity of water is greater than 1 that means that the wateer sampled is above the safe threshold. The output should state wheather it is safe use or no.
It also depicts the minimum time to retun below a safe threshold.

---------
Tester 

performs simple sanity checks that the math is correct, or could perform more complicated checking including that types returned and exceptions thrown match what are expected.

just open the test_analyze_data and execute it using the same syntax youll need to perform sanity checks to check that the code is working as expected. 

