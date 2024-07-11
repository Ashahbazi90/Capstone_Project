# Capstone_Project


### Direction for running code to set up tables and load data

1. Create a env file with the following defined 
    HOST_NAME="localhost"
    USERNAME="root"
    PASSWORD='yourpassword'
Make sure to enclose everything in quotes or else it won't pick up on it.

2. When you ahve the env file uploaded, open your MySQL workbench and have it open in the background
3. in your terminal make sure you are in the correct directory where all the capstone files are
4. Once navigated to the capstone project run the following command python3 utils/mysql_conn.py
5. If you get an error, try and debugg or message justin, if successfull you just get messages saying the database was created and the table was create. Go to mysql workbench, refresh it and you should see a new database appear and an empty table
6. Once the objects in mysql are created, you should now be able to load the historical data into mysql
run the following command python3 extract_coinbase.py
7. NOTE this will take anywhere from 10 to 15 minutes to run so be patient, if you get an error it will show up in the terminal if not you should get a message that states the table was loaded properly. NOTE sometimes there might be an error with the connection to mysql with creditientals. if this is the case message justin for help to debugg. If there is an error message along with a message about the tables being loaded, no data was actually loaded.
8. If you get no errors and it indicates the data was loaded, go into MySQL workbench and refresh and select all from the table to make sure there is data in the table