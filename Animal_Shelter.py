from pymongo import MongoClient
from pymongo import ReturnDocument
from bson.objectid import ObjectId
import pprint
from bson.json_util import dumps

class AnimalShelter():
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, userName:str = None, passWord:str = None):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.userName = userName
        self.passWord = passWord
        
        if userName is not None and passWord is not None:
            self.client = MongoClient('mongodb://%s:%s@localhost:37450/?authMechanism=DEFAULT&authSource=AAC' % (self.userName, self.passWord))
        else:
            self.client = MongoClient('mongodb://localhost:37450')
            
        self.database = self.client['AAC']
    
        # private function that returns cursor containing the search data
    def __searchDB(self, searchData: dict):
        """Helper function used for finding docuements.

        Args:
            searchData (dict): Criteria for document search.

        Raises:
            Exception: If searchData is None.

        Returns:
            Cursor: Doccuements that meet the search criteria.
        """
        # error handling for blank search data
        if searchData is None:
            raise Exception("Nothing to search for. Data argument is empty.")
            
        allData = self.database.animals.find(searchData)
        if allData.count() == 0:
            print("No items matching the below query: ")
            pprint.pprint(searchData)
            return None
        else:
            return allData

    # creates a document
    def create(self, data: dict) -> bool:
        """Creates a document object with the data arguement.

        Args:
            data (dict): data to be written to the new document.

        Raises:
            Exception: If the data argement is None.

        Returns:
            bool: True if successful.
        """
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary
            return True
        else:
            raise Exception("Nothing to write. Data argument is empty.")
                            
    # searches for and returns a document that meets the search criteria
    def read(self, searchData: dict, allItems: bool):
        """Reads documents from the database.

        Args:
            searchData (dict): Search parameters/criteria
            allItems (bool): Selects whether function returs all matches or just the first one.
            True = all results, False = first result.

        Returns:
            outputData (Cursor): results from the search IF allItems is True
            outputData[0] (JSON): results from the search IF allItems is False
        """
        outputData = self.__searchDB(searchData)
        if outputData is None:
            return None

        if allItems is True:
            return outputData
        else:
            return dumps(outputData[0])
             
    # find a document and update it
    def update(self, searchData: dict, updateData: dict):
        """Updates documents in the database. Can update a single docuement or all docuements that
        meet the search criteria.

        Args:
            searchData (dict): Search criteria for documents.
            updateData (dict): The data is to be updated on the found documents

        Raises:
            Exception: If the update data is None.

        Returns:
            result (JSON): result of the documents that were updated.
        """
        updateData = {"$set": updateData}

        if updateData is None:
            raise Exception("No update data provided.")
        
        #return if there are no documents in the collection that meet the search criteria
        outputData = self.__searchDB(searchData)
        if outputData is None:
            return None
        else:
            result = self.database.animals.find_one_and_update(searchData, updateData, 
                                                               return_document = ReturnDocument.AFTER)
            return dumps(result)
          
    # find a document and delete it
    def delete(self, searchData: dict):
        """Deletes a document or multiple documents that meet the search criteria.

        Args:
            searchData (dict): Search criteria for documents.

        Returns:
            result (JSON): result of the documents that were deleted.
        """
        #return if there are no documents in the collection that meet the search criteria
        outputData = self.__searchDB(searchData)
        if outputData is None:
            return None
        else:
            result = self.database.animals.find_one_and_delete(searchData)
            return dumps(result)
