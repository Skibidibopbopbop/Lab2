def main():
    print("ET0735 (DevOps for AIOT) - Lab 2 - Introduction to Python")
    display_main_menu()
    numlist = get_user_input()
    print("List of temperature: ", numlist)
    sort_temperature(numlist)
    Lowest_temp, Highest_temp = find_min_max(numlist)
    print("Highest temperature is: ", Highest_temp)
    print("Lowest temperature is: ", Lowest_temp)
    average = calc_average(numlist)
    print("Average temperature is: " ,average)
    median_temperature(numlist)
    
def display_main_menu():
    print("Enter recent TEMPERATURES separated by commas (e.g. 5, 67, 32)")
    return

def get_user_input():
    numlist1 = input("Enter recent temperatures here: ")
    x1= numlist1.split(",")
    numfloat = [float(x) for x in x1]
    return numfloat

def calc_average(numlist1):
    total_temp = sum(numlist1 )
    average = total_temp / len(numlist1)
    return average

def find_min_max(numlist3):
    min_value = min(numlist3)
    max_value = max(numlist3)
    return min_value,max_value

def sort_temperature(numlist2):
    numlist2.sort()
    print("Ascending order:", numlist2)
    return 

def median_temperature(numlist4):
    numlist4.sort
    n = len(numlist4)
    if len(numlist4)%2 == 0:
        median1 = numlist4[n//2]
        median2 = numlist4[n//2-1]
        median = (median1 + median2)/2

    else:
        median = numlist4[n//2]
    print("The Median is: "+str(median))
    
    return median 

if __name__ == "__main__":     
    main() 
