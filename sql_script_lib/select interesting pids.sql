select * 
from master_bookings_data
inner join product_ids on `master_bookings_data`.`Product ID` = `product_ids`.`product ID`
order by master_bookings_data.`End Customer Global Ultimate Name` ;