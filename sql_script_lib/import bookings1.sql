load data local infile 'C:/Users/jpisano/Desktop/ACI to Production Database - Beta/Todays Data/ALL_Bookings_Data_as_of_Dec_7_2016.csv' into table master_bookings_data
fields terminated by ','
	enclosed by '"'
    escaped by ''
lines terminated by '\r\n'
