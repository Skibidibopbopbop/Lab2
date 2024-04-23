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

#def calc_median_temperature(numlist2):
    median_temperature = (.median(numlist2))
    return median_temperature

if __name__ == "__main__":     
    main() 
