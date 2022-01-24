# Surfs Up

In this module, we covered the use of SQLite and SQLAlchemy in Jupyter Notebooks and Python.

Since we want to open a Surf n’ Snake shop serving surfboards and ice cream to locals and tourists in Oahu, Aloha, the investor W. Avy wants some weather analysis.


## Overview of the analysis 

The investor wants more information about temperature trends before opening the surf shop. 

In the Jupyter Notebook `[climate_analysis.ipynb]`, we prepared and reflected tables into SQLAlchemy ORM so we could do the exploratory analysis. In the analysis we found out that some months have higher amounts of precipitation than others, the most active station is USC00519281 and the temperature histogram shows that the temperature was between 70° and 78° degrees the most days in the last year.

W. Avy pointed that the board of directors won't use the jupyter notebook to get the results. For this reason, we used Python and Flask to display the results in a webpage — `[app.py]`.  

For this challenge, specifically, he wants temperature data for the months of June and December in Oahu, in order to determine if the surf and ice cream shop business is sustainable year-round.


##  Results

Major points from the two analysis deliverables

| June Observations| December Observations |
|--|--|
| ![june_desctobs](https://user-images.githubusercontent.com/90414330/150699395-312de7e5-4b59-4d69-9a62-f135dbac4c64.png) | ![dic_desctobs](https://user-images.githubusercontent.com/90414330/150699393-499b5443-2309-4967-b19c-f34d9dd98ac8.png) |


- June, in general, is warmer than December

- The lowest temperature observation was 56°F, taken in December. 

- Both June and December can have hot days, as seen in the `max row`.

##  Summary

W. Avy will be pleased to know that in the year, specially on the vacation months, the temperature is constant. In many days, Oahu, Aloha was between the 68°F and 72°F. 

A little bit colder in December, but just for some degrees and in rare days. 


| June | December |
|--|--|
| ![june_linechart](https://user-images.githubusercontent.com/90414330/150705624-cac75190-1eeb-4b21-8dbf-4edf56533069.png) | ![dic_linechart](https://user-images.githubusercontent.com/90414330/150705622-f226aeea-e2fb-4bca-8d6d-5ac07af4eccf.png) |
| ![june_histogram](https://user-images.githubusercontent.com/90414330/150705623-771e441a-99a2-414d-be96-58c66db1f376.png) | ![dic_histogram](https://user-images.githubusercontent.com/90414330/150705620-c36fd31c-aeb6-4f88-9414-614e6b434a1a.png) |


Queries used to get the last charts:

![additional_queries](https://user-images.githubusercontent.com/90414330/150707438-48358d0c-8325-4d23-b509-1a8aabc0a6f5.png)




> Written with [StackEdit](https://stackedit.io/).
