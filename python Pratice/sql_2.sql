SELECT B.ANIMAL_ID, B.NAME 
FROM ANIMAL_INS AS A RIGHT JOIN ANIMAL_OUTS AS B 
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE A.ANIMAL_ID IS NULL
ORDER BY B.ANIMAL_ID ASC;