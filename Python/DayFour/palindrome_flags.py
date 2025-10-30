def main():
    print("====You can check all your Palindrome words here with hybrid====")
    string = input("Enter the word you want to check today: ")
    if not ((ord(string[0]) >= 65 and ord(string[0]) <= 90) or (ord(string[0]) >= 97 and ord(string[0]) <= 122)):
        print("invalid selection")
    else:
        print(get_palindrome(string))
    exit_num = input("Enter Anthing to Exit and M to Start Again: ")
    if exit_num == "M" or exit_num == "m":
        main()
    elif exit_num == "X" or exit_num == "x":
        print("Goodbye my lad")


def get_palindrome(string):
    is_palindrome = True
    length = len(string)
    i = 0
    while i < length // 2:
        if string[i] != string[length - 1 - i]:
            is_palindrome = False
            break
        i += 1
    return is_palindrome
    

main()
