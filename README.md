# Insight Coding Challenge
# Nancy Zhang, Oct 29,2018
# Problem
This project creates metrics to analyze past years data of H1B program, specificially it calculates two metrics: Top 10 Occupations and Top 10 States for certified visa applications.

# I/O
input:

h1b_input.csv: statistics from the US Department of Labor and its Office of Foreign Labor Certification Performance Data

output:

top_10_occupations.txt: Top 10 occupations for certified visa applications

top_10_states.txt: Top 10 states for certified visa applications

# Approach
1.Read input and generate a list containing relevant information of all certified applications,

2.count frequency and store it in a dictionary,

3.convert dictionary to a list and sort the list by number of applications and alphabet.

4.output the top 10 items on the list.

# Run instructions
You can run the project with the following command from within the insightCoding folder:

./run.sh 

# Run tests
You can run the test with the following command from within the insight_testsuite folder:

insight_testsuite~$ ./run_tests.sh 

