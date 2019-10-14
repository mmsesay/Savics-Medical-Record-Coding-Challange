#!/usr/bin/python
import csv

def createNewRecord():
    """This fucntion creates a new medical record"""

    with open('medical_record.csv', mode='a', newline='') as csvfile:

 
        fieldnames = ['first_name', 'last_name', 'gender', 'age','city','country']
        
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        try:
            first_name = input('Input patient first name: ').capitalize()
            last_name = input('Input patient last name: ').capitalize()
            gender = input('Input patient\'s gender: ').capitalize()
            age = int(input('Input patient\'s age: '))
            city = input('Input patient\'s city: ').capitalize()
            country = input('Input patient\'s country: ').capitalize()
            
        except ValueError:
            print("The age must be an integer only")
            createNewRecord()  # call the function again
        finally:
            writer.writerow({'first_name': first_name, 'last_name': last_name,
            'gender': gender, 'age': age, 'city': city, 'country':country})
            print('data saved')
        
def searchMedicalRecord():
    """ This function search for a medical record """

    # opening the csv file
    with open('medical_record.csv', mode='r') as csvFile:
        """ Read from the file line by line and closes automatically. """

        # reading from the csv file and saving the content to the contents variable
        contents = csv.DictReader(csvFile)

        # get the user input
        user_input = input('Enter the first name of the patient: ').capitalize()

        # looping through the content
        for row in contents:
            if row['first_name'] == user_input:
                print('result=> '+ row['first_name'], row['last_name'], row['gender'],
                row['age'], row['city'], row['country'])

def filterAge():
    """ This function filter only patients under 18 yrs """

    # opening the csv file
    with open('medical_record.csv', mode='r') as csvFile:
        """ Read from the file line by line and closes automatically. """

        # reading from the csv file and saving the content to the contents variable
        contents = csv.DictReader(csvFile)

        # get the user input
        user_input = int(input('Enter age to filter patients: '))

        # looping through the content
        for row in contents:
            age = row['age']
            if int(age) == user_input:
                print('result => '+ row['first_name'], row['last_name'], row['gender'],
                row['age'], row['city'], row['country'])

def showMedicalRecord():
    """ This function returns all medical record """

    # opening the csv file
    with open('medical_record.csv', mode='r') as csvFile:
        """ Read from the file line by line and closes automatically. """

        # reading from the csv file and saving the content to the contents variable
        contents = csv.DictReader(csvFile)

        # looping through the content
        for row in contents:
            print(row['first_name'], row['last_name'], row['gender'],
                row['age'], row['city'], row['country'])

def main():
    print('\n\n** Welcome to Savics Medical Record\n**')
    reply = int(input('1. Add new medical record\n2. Search for a record'
    '\n3. Filter age under 18yrs\n4. Show all medical records\n5. Exit\nReply with (1, 2, 3, 4 or 5): '))
    # print('----------------------------------------------------\n')
    
    if reply == 1:
        print('--------------ADD NEW RECORD---------------------\n')
        createNewRecord()
        main()  # call main again
    elif reply == 2:
        print('--------------SEARCH RECORD---------------------\n')
        searchMedicalRecord()
        main()  # call main again
    elif reply == 3:
        print('--------------FILTER RECORD---------------------\n')
        filterAge()
        main()  # call main again
    elif reply == 4:
        print('--------------ALL RECORS---------------------\n')
        showMedicalRecord()
        main()  # call main again
    elif reply == 5:
        exit() 
    else:
        print('Invalid input')
        main()  # call main again
    
if __name__=="__main__":
    # strating the main function
    main()
