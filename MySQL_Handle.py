import mysql.connector as connector
while True:
    try:
        host = input("Enter the host you want to connect to \n")
        usr = input("Enter the user to be connected \n")
        pwd = input("Enter the password to the username \n")

        my_db = connector.connect(host = host, user = usr,passwd = pwd)

        print("Connection successful")
        print("*****************************************************************")
        # -----------------------------------------------------------------------------------------------------
        print("DATABASES PRESENT")
        my_cursor = my_db.cursor()
        my_cursor.execute("show databases")
        for i in my_cursor:
            print(i)
        my_cursor.close()
        db = input("select a database from above you want to connect ")
        my_db = connector.connect(host = host, user = usr,passwd = pwd, database = db)
        print("Yay!! connection established")
        print("*****************************************************************")
        #---------------------------------------------------------------------------------------------------
        my_cursor = my_db.cursor()
        while(1):
            print("Enter SQL query you want to execute")
            query = input()
            my_cursor.execute(query)
            for i in my_cursor:
                print(i)

    except connector.Error as err:
        print("Oops! Something went wrong")
        choice = input("Try again (y/n)?")
        if choice.lower() != "y":
            break
