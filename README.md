# Election_Analysis

## Project overview 
A Colorado Board of Elections requested a script to run the results of an elections. In particular asking for a scrio that delievers the following information: 

1) Total number of votes cast
2) A complete list of candidates who received votes
3) Total number of votes each candidate received
4) Percentage of votes each candidate won
5) The winner of the election based on popular vote

## Resources
- Data Source: election_results.csv
- Software: Pythong 3.6.7, Visual Studio Code, 

## Summary
The analysis of the elections results show tha:
- There were Total Votes: 369,711, in the election
- The Candiated were:
  -  Charles Casper Stockham
  -  Diana DeGette
  -  Raymon Anthony Doan
  
- The results were: 
  - Charles Casper Stockham recieved 23.0% of the vote and 85,213 number of votes
  - Diana DeGette recieved 73.8% of the vote and 272,892 number of votes
  - Raymon Anthony Doane recieved 3.1% of the vote and 11,606 number of votes
  -
- The WINNER of the elections was:
  - Diana DeGette who recieved 73.8% of the vote and 272,892 number of votes
 
 - The county with the largest number of voters: DENVER
  - Jefferson Doane recieved 10.5% of the vote and 38,855 number of votes
  - Denver recieved 82.8% of the vote and 306,055 number of votes
  - Arapahoe recieved 6.7% of the vote and 24,801 number of votes
  -
  <img width="239" alt="Election_results_pic" src="https://user-images.githubusercontent.com/105950742/174452720-73da7738-625b-4c1f-9fd2-5f1df24ddb71.png">

## Challenge Overview

### Challenge Summary
Using Python to calculate election results has various adnatages suchs as automating processes, fast execution, and reusing the code for similar projects. This code quickly returns various data for a U.S. Congressional Precinct in Colorado, but can be reused to determine:
  - The Candidates names 
  - Voter Counties
  - Number and percentage of votes for each candidate
  - Number and percentage of votes for each county
  - Declare the winning candidate and vote number/percentage
  - Declare country with the largest voter turnout/percentage
 
 The code can be motified for different elections by:
  - Changing the imported module from CSV to whatever file type/extension is needed. 
  - Chaning the PATH to collect new data "file_to_load = os.path.join("Resources", "election_results.csv")" and/or to print in a different txt file "file_to_save = os.path.join("analysis", "election_analysis.txt")"
  - The variables can be changed to calculate different voter information as well. For instance, instead of counting counties, the code can be  motifies to count voter political demographics (Republican, Democrat, etc..)
  
