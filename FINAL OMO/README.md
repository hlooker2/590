#README
Within this folder there are sub folders:

##RAW Data
There are three files within this folder. Each one is a RAW dataset untouched. A program will run over these and process them. Once the program is done the cleaned version goes to the "Data In" Folder.

##Data In
This folder contains all of the cleaned data processed from the "RAW Data" folder and the "Concat PEM" folder.

##Concat Pem
I had to create a second program to work with the PEM data. Once it is cleaned it has to be combined together so I created this new folder to grab this stage of the data and then to put it into the "Data In" folder in the format I wanted.

##Final Dataset
This folder contains the final CSV file. Unfortunately I have run out of time to get this exactly how I want it. I have created two files:
	
	1.FinalDataSet.csv is what the Concatination program creates. The problem is that I cannot figure out how to add headers to the final 4 columns so there is no explanation to what these are unless you manually touch them. 
	2. The FinalDataSet-W:Touches.csv is the concatination but I have manually added the column names for the last four columns.

##Program Files
The program files folder should be pretty straight forward.

	1. IPM - this is how I processed the IPM data and to get the monthly counts from the cleaned up data. The data is initally ran through the IPM Cleaning.py
	2. PEM temp + RH sorting.mean() - this is how I sorted the data by month and aggregated to find the mean per month.
	3. Concat PEM - here I take the pieces from bullet point two(above) to concatinate it into 1 data file.
	4. Weather temp + RH sorting.mean() is very similar to bullet point two (above) but it is working strictly with the external RAW weather data
	5. Concatenate - this file combines all the data into one csv file and drops columns that have unnecessary or repeated data like multiple columns for month.