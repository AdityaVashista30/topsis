# topsis
Topsis package to find the best option among given products depending upon their features and weightage of each feature for product selection
This is command-line program, where the user has to give in 3 lists of arguments:

 1.InputDataFile: CSV file containing all different types of products and their attribute/features
  
 2.Weights: list of weight the weights are given in order of attributes in CSV file as one to one mapping; separated by commas
 
 3.Impacts: a list of the impact of each attribute while product selection. The impact can be positive or negative represented as '+' and '-'    respectively. The input impacts have one to one mapping and are separated by commas.


  Example of usage:
    python topsis.py myData.csv “1,2,1,1” “+,+,-+”
    
Output:  best option: (best product name from given input)
