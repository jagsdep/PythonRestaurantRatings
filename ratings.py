# """Restaurant rating lister."""

# put your code here

rating_file = open('scores.txt') #Opened the file and assigned it to new variable

dict ={} #Created new dictionary that contains key value pair

for line in rating_file: #looped through each line of data in rating_file
   line = line.split(':')  #line is list that has two strings in it on index 0 and index 1
   
   dict[line[0]]=line[1] # assign the key value in the dict

# defined a function that sort the dict   
def print_sort_dict(): 
    
    for restaurant in sorted(dict):
        print(restaurant + 'is rated ' + dict.get(restaurant))
print_sort_dict()
   
# Prompt the user to add the restaurant name and rating

new_restaurant = raw_input("Add restaurant: ")
new_ratings = str(input('Rate the restaurant: '))
dict[new_restaurant] = new_ratings #Storing new restaurant_name and rating in dictionary

print_sort_dict()

   

    


