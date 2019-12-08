SELECT 
    tue_data.`Hash Value` AS TUE_HASH,
    tue_data.`End Customer Global Ultimate Name` AS TUE_CUST,
    wed_data.`Hash Value` AS WED_HASH,
    wed_data.`End Customer Global Ultimate Name` AS WED_CUST
FROM
    tue_data
        INNER JOIN
    wed_data
    on tue_data.`Hash Value` = wed_data.`Hash Value` ;
    