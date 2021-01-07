#!/bin/bash

start_time=`date +%s`

python3 preprocess.py
python3 multiply.py M.txt v.txt
python3 post_multiplication.py

while :
do
	test -f top_ten_pageranks.txt
	if (( $? == 0 ))
	then 
		break
	fi
	
	python3 multiply.py M.txt v.txt
	python3 post_multiplication.py
done

end_time=`date +%s`
echo Execution time: `expr $end_time - $start_time` s.