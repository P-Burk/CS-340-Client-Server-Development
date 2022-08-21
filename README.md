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

### -	USER ACCOUNT SETUP
- ADMIN ACCOUNT
  -	Start the Mongo instance using the mongo command.
  -	Navigate to the admin database using the use admin command.
  -	From here use the following command to add a user with administrative privileges: </br>
  `db.createUser({ 
      user: “admin”, 
      pwd: “password”, 
      roles: [{ role: “userAdminAnyDatabase”, db: “admin”}, “readWriteAnyDatabase” ]
  })` </br>
  You can see the example below where the username is “PEBurkhardt” and the password is “adminPass”.
  ![image](https://user-images.githubusercontent.com/68164093/185775408-d29ae412-8cea-4bcc-83e6-7bef13f3324e.png)
- READ/WRITE USER ACCOUNT
  - For a regular user account, you follow the same steps as above, except the roles will be different. In this case, we made a user account for someone using the AAC database we created previously. For this one, use the command: </br>
  `db.createUser({ 
      user: “aacuser”, 
      pwd: “password”, 
      roles: [{ role: “readWrite”, db: “AAC”}]
  })` </br>
  ![image](https://user-images.githubusercontent.com/68164093/185775474-e8db37ab-930b-42c8-ab3d-a3f26eab3789.png)
  
### -	LOGGING INTO THE DATABASE
  - In order to log into the database as a user, first exit the database using the `exit` command.
  - From here, restart the database using the following commands: </br>
  `/usr/local/bin/mongod_ctl stop` </br>
  `/usr/local/bin/mongod_ctl start` </br>
  - You can then log into the database using the following command: </br>
  `mongo --authenticationDatabase "DBNAME" -u "USERNAME" -p` </br>
  Replace `DBNAME` with the database used when creating the user account and replace `USERNAME` with the username. You can see in the below image the commands used to log into the admin account and user account that we created in previous steps. </br>
  ![image](https://user-images.githubusercontent.com/68164093/185775538-7017608b-88e1-4d85-896c-7a1bdf1c23cc.png) </br>
  One thing to note is that the admin can see all of the databases when you use the `show dbs` command while the aacuser account can only see the database that they have privileges for.
  - For any issues creating a user account, see the [MongoDB documentation for creating users](https://www.mongodb.com/docs/v4.2/tutorial/create-users/).

### -	PYTHON MODULE SETUP
  - Pull the `Animal_Shelter.py` and `Animal_Shelter_tests.ipynb` files from the GitHub repository or your cloned version of the repository.
  - Navigate to these files in a program like Jupyter Notebook and open them. </br>
  ![image](https://user-images.githubusercontent.com/68164093/185775659-74567843-cf56-433e-a068-7ee84227e671.png)
  - Once they are open, you can make changes to the .py file and test the changes/functions in the .ipynb file.
  - NOTE: you don’t NEED to use Jupyter Notebook, but it makes editing and testing the project files easier.

## SETUP: Installation
The tools needed for this project are as follows:
  - MongoDB (v4.2.6) – Chosen for its ease of use and ease of scalability.  
    - [MongoDB installation.](https://www.mongodb.com/docs/v4.2/installation/)
  - Python (v3.6.9) – Chosen because of its ease of use for beginners and the fact that it is free and open source.
    - [Python installation.](https://wiki.python.org/moin/BeginnersGuide/Download)
  -	PyMongo (v3.10.1) – Chosen because it is the official MongoDB driver for Python applications interfacing with MongoDB databases. Easy to use and built specifically for Python + MongoDB.
	  -	Open the command prompt or terminal once Python has been installed
    -	Run the command: </br>
      `pip install pymongo==3.10.1` </br>
  -	Dash (v1.10.0) – Chosen for it being open source, modularity, and ability to easily create interactive data apps. Dash allows a user to set up a web application without needing to know HTML5 and CSS. It has functions of both built in, making it easy to learn and quick to deploy a working web application.
    -	Open the command prompt or terminal once Python has been installed
    -	Run the command: </br>
      `pip install dash==1.10.0` </br>
    - [Dash installation.](https://dash.plotly.com/installation)
  -	A requirements.txt file will be included that contains all Python dependencies. These can be installed using the command: `pip install -r requirements.txt`

## USAGE
The main part of this project acts as a CRUD (create, read, update, delete) application that interfaces with the MongoDB database.
- CREATE
  - This portion of the module is used to add entries to the database. It takes a dictionary containing the data to be added as an argument.
- READ
  - This portion of the module is used to read entries from the database. You can either read a whole list of entries matching the search query or read the first entry in the list of matching results. You select the output based on the second argument of the read() command. True for outputting all matches, False for outputting only the first match.
- UPDATE
  - This portion of the module is used for updating documents within the database. It takes two arguments, both being dictionaries. The first one is the parameters you wish to search for and the second one is the parameters which you wish to update. The function has handling for “None” arguments and if the search comes back empty. Also, it will ask the user if they wish to delete multiple or single documents if more than one meet the search criteria.
- DELETE
  -	This portion of the module is used for deleting documents out of the database. It is modeled and performs almost exactly the same as the update function except it only takes one argument. That argument is the search parameters for the documents(s) you wish to delete.

## TESTS
NOTE: Ensure that the MongoDB instance is running BEFORE testing. </br>
To test the Python module, use the Animal_Shelter_tests.ipynb file. </br>
- Initialize the class and test variables: </br>
NOTE: You can use an account that you set up during the user account setup section OR you can start the MongoDB instance in “noauth” mode and omit the username and password.
![image](https://user-images.githubusercontent.com/68164093/185776835-6e156410-bdcc-469e-9bb6-58d45eb6ca89.png)
- Select the cells you containing the tests you wish to run and hit the “>| Run” button. It is advised that they are tested in the order they are in or else unexpected results may occur. An example is running the test to display “data not found” output after you have run the test where the data is created. The previous test will return the created data rather than the expected error output.
- EXAMPLE: running the create() test with the test variable initialized in a previous step.
![image](https://user-images.githubusercontent.com/68164093/185776859-c2c1e634-6ce1-48e3-ba2f-7ab7264e89d1.png) </br>
MongoDB query showing the database entry: </br>
![image](https://user-images.githubusercontent.com/68164093/185776876-7de433a6-403e-4040-b07d-d826cfd08515.png)
- EXAMPLE: reading the first entry from that database that meets the search criteria:
![image](https://user-images.githubusercontent.com/68164093/185776893-1199e5a4-6163-4313-94c2-07ca735d7a50.png)
- EXAMPLE: reading multiple entries from the database (note the multiple IDs and scroll bar, indicating there are multiple entries that meet the criteria of the search): </br>
![image](https://user-images.githubusercontent.com/68164093/185776902-75405e23-da24-4fa1-b7a4-c5d9e2c90f34.png)
- EXAMPLE: running the update function when multiple entries meet the search criteria prompts the user with a question on whether or not they want to update all entries or just one. Selecting just one will further prompt for the Animal ID of the one the user wishes to update or to type “exit” to exit out of the function:
![image](https://user-images.githubusercontent.com/68164093/185776910-07320a86-e07a-4026-9bdb-f402fd1d40b3.png) </br>
"n" was entered into the box: </br>
![image](https://user-images.githubusercontent.com/68164093/185776921-af6bd8ef-2948-448d-a73c-d0489bd95b25.png) </br>
Upon entering a valid ID, that animal’s record will be displayed with the updated information along with a conformation message about the total number of animals
updated: </br>
![image](https://user-images.githubusercontent.com/68164093/185776928-00ba84f3-4d76-4eca-be8b-65f3f0386002.png)
- EXAMPLE: running the same command but entering “y” for the prompt asking if the user wishes to update all entries will update all the entries and display the updated entries along with the count of how many animals were updated:
![image](https://user-images.githubusercontent.com/68164093/185776937-6a5444a9-9a3b-46f6-865e-3087af95bedc.png) </br>
NOTE: run the command under that one and enter “y” for the prompt to change all of the updates from the previous two commands back to their original values. This is accomplished using the same update() command, but swapping the arguments. </br>
![image](https://user-images.githubusercontent.com/68164093/185776948-076e1021-1acd-41b9-b5e7-6cdb1595f201.png)</br>
- EXAMPLE: The delete() command works exactly the same way as the update() command. For this one we will add multiple documents to use for a demonstration.:</br>
![image](https://user-images.githubusercontent.com/68164093/185776978-06f485d1-270e-46bb-b273-883734f2c8b2.png)</br>
![image](https://user-images.githubusercontent.com/68164093/185776983-a275d528-89d8-4e14-98fc-2ecaaee811fb.png) </br>
We can first try deleting a single cat from the ones we added: </br>
![image](https://user-images.githubusercontent.com/68164093/185777000-bc833040-b0c2-4c7d-b541-ced3bcbd9680.png) </br>
After entering the ID: </br>
![image](https://user-images.githubusercontent.com/68164093/185777019-734ee226-ac8a-406a-997f-2363fc7287ec.png) </br>
We can confirm the delete by running our read() command, which should only return two documents: </br>
![image](https://user-images.githubusercontent.com/68164093/185777033-519eb380-763b-4e56-be8f-698722e8a8a9.png) </br>
Running the delete command again, but selection “y” will result in the other two documents being deleted: </br>
![image](https://user-images.githubusercontent.com/68164093/185777048-e759fb8f-ffba-4d16-a6a7-3ea849a735f1.png) </br>
Running the search again should result in "no items matching": </br>
![image](https://user-images.githubusercontent.com/68164093/185777052-8d305542-633f-4d8a-861c-bc816b392c38.png) </br>
Finally, if you run the delete() command and only one document in the database matches the search criteria, it will be automatically deleted: </br>
![image](https://user-images.githubusercontent.com/68164093/185777062-0325c3dc-706b-4dfa-a665-0f9d9e2c1dbf.png) </br>

## Roadmap/Features
- TODO
	- ~~Implement update() functionality.~~
	- ~~Implement delete() functionality.~~
- FIXME
	- ~~Roll realAll() and readOne() into a single read() command where a second argument determines whether a list of entries or a single entry is returned.~~

## Steps to Complete the Project + Challenges
In order to complete this project, I broke it down into different sections, completed each section individually, then combined all sections into the final dashboard. The first section was the header with the logo, title, and author note. This section was challenging for me because I couldn’t figure out how to get the layout right. My header was rendering the different sections on top of each other like: </br>

Logo </br>
Title </br>
Author </br>

My goal was for it to render side by side. For this, I used some of the style features of Dash to implement some formatting via Flexbox. The [CSS-Tricks](https://css-tricks.com/snippets/css/a-guide-to-flexbox/) site was especially helpful for this section and other sections where display formatting was utilized.

The next section I tackled was the radio buttons. These weren’t particularly difficult because Dash has functions to generate these natively. The hard part was tying filtering to the radio buttons. For this, I used a Dash callback function and a helper function. The callback function first takes the filter option from the radio button module, then it calls the helper function, using the filter option as an argument. Finally, it feeds the helper function’s output data frame to the table for display. The helper function is fairly straight forward. It executes one of the preset queries on the database based on the filter option it is fed, passes it to another helper function for formatting, then returns the final data frame. I found it easier to generate a new data frame with the query results and use that for table/graph generation versus filtering the initial data frame populated with all of the documents from the database.

The next/concurrent section was the data table. The only real challenges to this section were choosing the different attribute options and formatting. The data used in the table comes pre-formatted thanks to a helper function used in generating the data frame. The formatting of the actual table itself was taken care of via style_data options that lock the column width and handle text overflow. 

After the table, I wanted to implement row selection because I knew this would integrate with a later section (map + markers). For this I modified code that was to used to highlight columns, which I wasn’t going to use. It was as simple as changing all of the “column” keywords to “row_index” and changing the input value fed to the callback function.
I tackled the map section next. For this section, I used Dash_Leaflet’s built in Map() function. I fed this the data from the table completed in a previous section. One issue I faced when completing this section what that I was getting IndexErrors when the no dog had been selected in the table. To remedy this, I used a try/except clause to return a map with no markers if an IndexError occurs. The rest of the callback function is pretty straightforward. It uses the selectedRow attribute from the table to get a row. Then it uses the values in the 5th and 6th index locations to plot the longitude and latitude for the marker. 

The final section I tackled was the pie chart. The callback function for this section takes in all of the data from the chart. It uses this data to create a new data frame. This data frame gets edited so that it consists of all the different breeds and the count for each. All dog breeds with 50 or less entries in the database get lumped into the “other breeds” category. The only issue I had with this section was getting the counts of each breed and translating that into something that could be used by the plotly express library. Once I learned that the pie function of the library had options for names and values, I didn’t have any more issues. I used breeds for the names and counts/totals for the values in order to get the pie chart to represent breed totals.

