def function1():
    while(True):
        updateAll = str(input("Would you like to update all documents? (y/n) "))
        if updateAll.lower() == "y":        #update many
            print("Updated documents: ")
            return
        elif updateAll.lower() == "n":      #update one
            updateOne = str(input("Enter the Animal ID of the one you wish to update: "))
            searchData = {"animal_id" : updateOne}

            print("Updated document: ")

            return

function1()