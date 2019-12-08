ALTER TABLE `ref_db`.`current_data` 
ADD COLUMN `PSS` VARCHAR(45) NULL AFTER `Bookings Adjustments Description`,
ADD COLUMN `TSA` VARCHAR(45) NULL AFTER `PSS`;