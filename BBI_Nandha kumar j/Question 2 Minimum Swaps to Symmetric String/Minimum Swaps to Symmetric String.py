#function for swapping the letters to symmentry
def swapping_symmetry(string):
    #initialising count maximum and minimum index
    count = 0
    minimum_index = 0
    maximun_index = len(string) - 1
    #converting string to list
    String_list = [i for i in string]
    #conditioning min < max, interating min to +1 and max to -1
    while minimum_index< maximun_index:
        #assinging temp index as maximum
        temp_index = maximun_index
        #while condition to check if the charecter in the min index is != max index
        #if so max index will be reduced by -1 for each iterration till we get the charecter in min_index
        while String_list[minimum_index] != String_list[temp_index]:
            temp_index = temp_index - 1
            #if condition break the look and return value if there is no matching letter
            if temp_index == minimum_index:
                return -1
        #once the character found
        #while condition to swap the character to the max index
        #counting to check the no of swap
        while String_list[minimum_index] == String_list[temp_index] and temp_index < maximun_index:
            String_list[temp_index], String_list[temp_index + 1] = String_list[temp_index + 1], String_list[temp_index]
            count = count + 1
            #temp index is iterated till max index to  swap the charecter till max index
            temp_index = temp_index + 1
        minimum_index = minimum_index + 1
        maximun_index = maximun_index - 1

    #return the count
    return count

string = "aabb"
print("No of swapping count to get symmetry: ", swapping_symmetry(string))
