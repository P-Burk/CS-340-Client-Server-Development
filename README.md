# CS-340-Client-Server-Development

## Class Reflection Questions

### •	How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?
I write programs that are maintainable and adaptable by breaking down tasks that a function should do into functions. Any code that is repeated across functions, I break off into its own function. I did this in my Python CRUD module with my searchDB() function. I knew all of my other functions were going to need to search the database for documents matching the search criteria, so I broke the actual search off into its own function that gets used by all the other functions. I write readable code by using intuitive variable and function names while also commenting my code where it would be beneficial. I added docstring comments to my CRUD module so that someone would be able to easily see how each function works.

### • How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?
I approached the problem given to us in project two by breaking down the requirements into different parts, building the specific parts, then combining them all into the final product. I was also given a framework that I had never worked with before (Plotly/Dash) and took the time to browse the documentation to get a general idea of what it’s used for and how to use it to accomplish the task given to me. In the future, if I need to create a database to meet client requirements, I will consider using MongoDB. I feel that there is a lot more to MongoDB than what this course taught us and I like that its format is basically a 1:1 match to JSON. One technique I would use is enforcing schemas. The idea behind this is so that data that shouldn’t be in the database doesn’t get added to it and the data that is there has the same structure and contents.

### • What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?
Computer scientists solve problems using computers and software. This matters because some problems are best solved using computers and software. Inventory tracking used to be done with paper ledgers. What if the ledger got lost, destroyed, or stolen? While all of this is possible with using an electronic/software-based inventory system, it’s a lot easier to have backups and copies made. Computer scientists helped design, build, and deploy the electronic inventory systems used today. Our work on this type of project helps companies like Grazioso Salvare by making their jobs easier, which in turn helps them field a better product to their customers. 

## About the Project
This project was commissioned by the Grazioso Salvare company to help them identify shelter dogs in the Austin, TX area for search-and-rescue training. They want the software to be free and open source so that similar organizations in other areas can make use of its features as well.

## Motivation
The motivation behind the project is that we want to make it easier for companies like Grazioso Salvare to help the dogs and people around them. It helps the dogs in the shelter system by making it easier to find ones that would qualify for search-and-rescue training programs or any other kind of service dog training programs. Finally, with being able to identify dogs for service training programs easier, more dogs will get trained. This leads to service dogs being available when the need arises such as during natural disasters.

## Dashboard
The dashboard can be accessed by running the `ProjectTwoDashboard.ipynb` file. This will present the user with a link to the actual dashboard. 
![gif1](https://user-images.githubusercontent.com/68164093/185774027-4649118c-5777-4adb-b5e3-64b0ba2835f8.gif)

When on the dashboard, you will see a table of the dogs that meet the different filtering options (based on training type). These filters are selectable in the space above the table.
![gif3](https://user-images.githubusercontent.com/68164093/185774073-d76e25f3-7ff6-486b-9e46-ebbf8e628e92.gif)
![gif4](https://user-images.githubusercontent.com/68164093/185774087-81907dd4-b0e1-4940-a6ed-7dcae2dcb360.gif)

The pie chart details the number of each breed is based off of the current filtered results.
![gif5](https://user-images.githubusercontent.com/68164093/185774114-d839eccb-e485-4a52-aece-9314d859c13c.gif)

If a user selects the row of a dog, the map will update with a marker where said dog is located. The map maker also contains a text box showing the dog’s ID number and their name.
![gif2](https://user-images.githubusercontent.com/68164093/185774138-018104b1-6c3e-4349-849b-90ca30e6615b.gif)

## SETUP: Getting Started
In order to get started with this project, you will first need to follow the instructions in the installation section to get MongoDB and Python installed. Please see the below steps to recreate the database and Python module.
### -	DATABASE SETUP
- To set up the database, you will need the appropriate csv file with the animal information. For this, you can use the Austin Animal Center (AAC) Outcomes data set (aac_shelter_outcomes.csv).
- In order to create the database, you need to open the terminal and navigate to the directory where the csv file is located. 
Example code:`cd /usr/local/datasets/`
- Next, you import the csv and create the database via the following command: </br>
`mongoimport --port PORTNUMBER --db DBNAME --collection COLLECTIONNAME --type=csv --headerline --file=./aac_shelter_outcome.csv` </br>
Replace `PORTNUMBER`, `DBNAME`, and `COLLECTIONNAME` with your port number and desired names. You should get a log stating the connection to the MongoDB instance and how many documents were imported successfully and/or failed to import.
![image](https://user-images.githubusercontent.com/68164093/185774325-57cbfac7-d4a6-4fd6-82e8-eebbeb98cd73.png)
- From here you can start your MongoDB instance and get into the command line using the commands: </br>
`/usr/local/bin/mongod_ctl start-noauth` </br>
and </br>
`mongo` </br>
- Ensure that the database was created/imported correctly by using the commands below (for the example, the database name was AAC and the collection name was animals): </br>
`show dbs` </br>
`use AAC` </br>
`show collections` </br>
![image](https://user-images.githubusercontent.com/68164093/185774513-5c2962a3-2783-4dcb-a3eb-361a136759d8.png)




