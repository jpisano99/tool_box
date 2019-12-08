load data local infile 'C:/Users/jpisano/Desktop/Bookings Data/fy17_data_as_of_Oct_12_2016.csv' into table wed_data
fields terminated by ','
	enclosed by '"'
    escaped by ''
lines terminated by '\r\n'
