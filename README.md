# topsis
Topsis package to find the best option among given products depending upon their features and weightage of each feature for product selection
This is comand line program, here the user has to give in 3 list of arguments:

 1.InputDataFile: CSV file containg all different types of prducts adn their attribute/features
  
 2.Weigths: list of weight the weights are given in orderr of attributes in CSV file as one to one mapping; seperated by commas
 
 3.Impacts: a list of imapct of each attribute while product selection. Impact can be positive or negative represented as '+' and '-'                  respectively. The input impacts have one to one mapping and are seperated by commas.


  Example of usage:
    python topsis.py myData.csv “1,2,1,1” “+,+,-+”
    
Output:  best option: (best product name from given input)
