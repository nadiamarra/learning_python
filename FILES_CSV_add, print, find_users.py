from csv import reader,writer,DictReader

def add_user(file_name,first_name,last_name):

    '''
    Take in a first name and a last name and add a new users a csv file.

    >>> add_user("users.csv","Dwayne", "Johnson") # None
    # CSV now has two data rows:
    # First Name,Last Name
    # Colt,Steele
    # Dwayne,Johnson
    '''

    with open(file_name,"a") as file:
        csv_writer=writer(file)
        csv_writer.writerow([first_name,last_name])


def print_lists_of_users(file_name):

    '''
    Print out lists of all the first and last names in a csv file.
    
    >>> print_users("users.csv") # None
    # prints to the console:
    # Colt Steele
    '''

    with open(file_name) as file:
        csv_reader=reader(file)
        next(csv_reader)
        for row in csv_reader:
            print(row)


def print_users(file_name):

    '''
    Print out all the first and last names in a csv file.
    
    >>> print_users("users.csv") # None
    # prints to the console:
    # Colt Steele
    '''

    with open(file_name) as file:
        csv_reader=DictReader(file)
        for row in csv_reader:
            print(row["First Name"]+" "+row["Last Name"])


def find_user(file_name,first_name,last_name):

    '''
    Return the index in which a given user is found.
    
    >>> find_user("Colt", "Steele") # 1
    >>> find_user("Alan", "Turing") # 3
    >>> find_user("Not", "Here") # 'Not Here not found.'
    '''

    with open(file_name,"r") as file:
        csv_reader=reader(file)
        count=0
        for row in csv_reader:
            if row[0] == first_name and row[1]== last_name:
                return count
            count+=1
        return f"{first_name} {last_name} not found"


