#Workflow steps

	Start by creating a parent folder naming it UNIT_YYYY_initials. Within that parent folder create several folders. Concat PEM, Concat Weather, Data In, Final Dataset, and RAW Data 
	
	1. Run IPM excel data through IPM Cleaning.py. Do this by simply copying and pasting data from excel sheets into the program. When this exports have it go into the "RAW data" folder that is created.
	2. Run the cleaned IPM data through IPM - getting monthly counts.ipynb. When this exports have it go to the "data in" folder that is created.
	3. Run PEM dat through PEM temp + RH sorting.mean().ipynb. When this data exports have it go into the "Concat PEM" folder created.
	4. Run Concat PEM.ipynb on files inside of the Concat PEM folder. Have that csv go into the "Data In" folder.
	5. Run steps 3 and 4 on the Weather data using the Weather temp + RH sorting.mean().ipynb. Export the Concat Weather into the "Data in" folder.
	6. Run Concatenate on everything in the "Data in" folder.