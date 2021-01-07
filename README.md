# PageRank-Algorithm
PageRank algorithm implementation from scratch using Python.

- Run the algorithm using run.sh shell script.
- We used Google's [Web Graph 2002](http://snap.stanford.edu/data/web-Google.html) as input. The computation time of our algorithm on this benchmark set is 9366s. 
- The code has been written considering the input data and the input filename has been hard-coded as "web-Google.txt" in source file "process.py". Change the input filename/process.py as required.


## Source files description:
run.sh:
This shell script allows the user to run this algorithm. It first runs preprocess.py first, then it runs multiply.py and finally it runs post_multiplication.py. Then it checks if top_ten_pageranks.txt has been created, if no, then it runs multiply.py and post_multiplication.py in loop until top_ten_pageranks.txt is created. After completing the execution, it displays the total time taken for execution in seconds.

preprocess.py: 
This source file take input file "web-Google.txt" and creates M.txt and v.txt files for our computation. Since matrix M is sparse in nature, to save space, the data of matrix M has been stored in a format "row name, column name, value" in the .txt file. The data of vector v has been stored in format "row name, value" since it has only one column 0, we didn't store the column name. This file also creates a "original_v.txt" file to store the original vector v values and "nodes.txt" file to store the list of all from_node and to_node present in input file.

multiply.py:
This source file as the name suggests performs multiplication. It takes M.txt and v.txt files which has been created by preprocess.py and performs multiplication between them and it creates a multiplication_result.txt file as an output. The format of multiplication.txt file is "row, value" since the result is a vector which has only one column, so we have not considered column number in result.
For multiplication, we have used 2 mapreduce jobs. First mapreduce job performs the multiplication between elements and the second mapreduce job sums up the multiplication results corresponding to the same row and writes the result in the resultant .txt file.


post_multiplication.py:
This source file takes the multiplication_result.txt file created by multiply.py file and v.txt. It computes new_v based on the multiplication_result.txt results. We have chosen beta to be 0.85. Then it computes the difference between v and new_v. We have taken 8.9e-7 as threshold. 
If the difference is greater than this threshold then we break from the loop of calculating the difference and save v as old_v.txt and new_v as new v.txt. 
If the difference is less than this threshold for all nodes then we save all page ranks in all_pageranks.txt and save top ten page ranks as top_ten_pageranks.txt. 









