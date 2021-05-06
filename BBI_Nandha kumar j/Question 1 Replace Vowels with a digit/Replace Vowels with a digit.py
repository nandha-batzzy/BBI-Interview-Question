#function to find the sum of the digits
def sum_of_the_digits(number):
    #initialising sum as 0
    sum = 0

    #iterating through the number and finding the sum
    #mod by 10 to take last digit and add it to the sum
    #dividing number by 10 as integer to remove the last digit"

    while number != 0:
        sum = sum + (number % 10)
        number = int(number / 10)
        #if the sum is more than single digit
        #assinging number as sum and adding again those remaining digit till we get single digit
        if number == 0 and int(sum / 10) > 0:
            number = sum
            sum = 0
    return sum

#function to find the sum of prime number
def sum_of_the_prime(index_multiplied_with_100):
    #initiating sum as 0
    sum = 0
    #iterating through out the number
    for number in range(2, index_multiplied_with_100):
        #since 1 and 2 are divisible by iteself taking number >1
        if number > 1:
            #iterating through the number to get the number divisible by itself
            #if so break the statement and add the number
            for i in range(2, number):
                if number % i == 0:
                    break
            else:
                sum = sum + number
    return sum


#main function
if __name__ == "__main__":
    String = 'replace this'
    Vowels = 'aeiou'
    # List to append the values
    List_Final = []
    #iterating through the string
    for i in range(len(String)):
        #checking if the charecter in the vowels
        if String[i] in Vowels:
            #if so mutiply the index number of the charecter with 100
            index_multiplied_with_100 = i * 100
            #calling sum_of_the_prime to calculate prime number sum
            Prime_Number_Sum = sum_of_the_prime(index_multiplied_with_100)
            #calling the sum_of_the_digits to find the sum of the digits in the number
            Sum_of_the_digit = sum_of_the_digits(Prime_Number_Sum)
            #appending the calculated number
            List_Final.append(Sum_of_the_digit)
        # appending the letters which are not vowels
        else:
            List_Final.append(String[i])
        # printing the values
    for Values in List_Final:
        print(Values, end="")
