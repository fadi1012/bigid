#  First question solution 

# what should be tested and how :

- validate that file is opened with no errors

- validate that each generated file part has less or equal to x lines by getting the total number of lines in the generated file and comparing it to the requested value which in our case is 1000

- validate that matcher gets the file part correctly, as a string by checking it's type

- validate that after all matches completed sum of all lines/chars is equal to base file in order to assure nothing was lost from the original

- validate that if all matches are completed the aggregator is called

- validate that when aggregator is called all files are combined and printed correctly, we can store the number of the generated files from the first part and compare to the current step, also to validate that eventually data is printed

- validate that after invoking the main module a map is created it contains a word and it's location in the text, we can check the type of the generated data that it's an instance of a map and make sure that it contains in the key a string and the value contains lineOffset and charOffset

- validate that the generated map data is correct, this can be done by comparing the generated file result with an already known expected result
 
- validate that eventually the aggregator aggregates the results from all matchers and print the final result, we can store all generated maps from the different parts and compare to the current step and make sure nothing is missed

- validate that file is closed 

# what should be done manually and what can be covered in automation
- in my opinion all the cases can be covered in automation i even think it's better with this amount of data because the human eye will definitely miss something 

# corner cases
- file is empty - should be handled accordingly 
- matcher is stuck on one of the file parts
- the string is not found, a proper message should be printed

