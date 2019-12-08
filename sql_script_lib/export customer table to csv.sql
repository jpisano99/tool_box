SELECT * FROM cust_ref_db.master_customer_data
	INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/Customer_List.csv' 
	FIELDS ENCLOSED BY '"' 
	TERMINATED BY ',' 
	ESCAPED BY '' 
	LINES TERMINATED BY '\r\n';