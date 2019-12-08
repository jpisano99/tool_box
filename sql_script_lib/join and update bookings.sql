UPDATE wed_data
        JOIN
    tue_data ON tue_data.`Hash Value` = wed_data.`Hash Value` 
SET 
    wed_data.`Corporate Bookings Flag` = 'delete'
WHERE
    wed_data.`Hash Value` = tue_data.`Hash Value`