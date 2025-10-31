def main():
    print("====You can check all your Perfect Square numbers here with hybrid====")
    user_input = int(input("Enter the number you want to check today: "))
    if not is_perfect_square(user_input):
        all_perfect_squares(user_input)
    else:
        print("invalid selection")
    exit_num = input("Enter Anthing to Exit and M to Start Again: ")
    if exit_num == "M" or exit_num == "m":
        main()
    elif exit_num == "X" or exit_num == "x":
        print("Goodbye my lad")


def is_perfect_square(n):
     
    number = 0
    while number * number <= n:
        if number * number == n:
            return True
        number += 1
    return False

def all_perfect_squares(user_input):
    if not is_perfect_square(user_input[number]): 
        return False
    return True

main()


