# Adding the regular expression library to match strings of text such as particular characters, words, or patterns of characters
import re  

#Function to carry out required computation
def main():         
    data = input('Enter input: ') #statement to recieve input

    # Remove whitespaces that may be inputed at the beginning or end of data
    #I added \' and \" because I was not sure if the input would come as "1,2,3,4,5-3,2-10" or '1,2,3,4,5-3,2-10' or 1,2,3,4,5-3,2-10
    #Using the python .strip method to remove commas that may be inputed at the beginning or end of string data 
    data=data.strip().strip('\"').strip("\'").strip(',')
    new_data = data.split(',') # python method .split to seperate the data at every comma(,)
    
    #Invalid input Check
    #Using the .findall method to find all inputs that are not numbers 0-9, hyphen(-), widespaces(s+), comma(,)
    invalidCharacter_2 = re.findall("[^(0-9,\-,\s+,\,]", data) 
    
    #Creating an empty list to append all produced data
    li = [] 

    # Conditional statement to check for invalid input as well as input of hyphen only and no entry
    if(invalidCharacter_2 or data=='' or data=='-'):
        print('"Error"')

    # Valid input statement
    else:
        for i in range(len(new_data)):

            #if data contains double comma e.g 1,2,,3,4 that was entered in error
            #if data contains whitespaces inbetween data elements e.g 1,2,  ,4,  ,5,6
            #if data contains a negative number with optional spacing
            if((new_data[i] == '') or (new_data[i]== " ") or (re.match("(\s+)?\-(\s+)?[0-9]+", new_data[i]))):
                continue
            else:

                # check if the element is a range of numbers e.g (3-10) by looking for the hyphen(-), and assign the elements of the range to variable names
                if '-' in new_data[i]:
                    rangeData = new_data[i].split('-')
                    start = int(rangeData[0])
                    end = int(rangeData[1])
                    
                    # check if the end number of the range is greater than the start number e.g (3-8) end=8, start=3 and append the range to list li
                    if (end > start):
                        for x in range(start, end + 1):
                            li.append(x)
                    elif(start == end):  # if the range is of length 1 in case of user error (e.g 1-1 instead of 1-11), append one of the elements to list li
                        li.append(int(start))
                    else:  # if the range is reversed, start number is greater than end number e.g (8-3) start=8, end=3 and append the range to list li
                        for y in range(end, start + 1):
                            li.append(y)
                
                # if element in input is not a range, e.g a single number 1,2,3,4,5 add the element to list li
                else:
                    li.append(int(new_data[i]))

        #After checking for all conditions, print out all elements in the list li seperated with a space           
        for i in range(len(li)):
            print(li[i], end=' ')

#Calling the function to begin usage
main()