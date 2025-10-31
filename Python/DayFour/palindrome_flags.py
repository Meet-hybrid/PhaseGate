import turtle
import threading
import time

def show_animation():
    a = 0
    b = 0
    turtle.bgcolor("black")
    turtle.speed(0)
    turtle.pencolor("green")
    turtle.penup()
    turtle.goto(0, 200)
    turtle.pendown()

    while b < 200:
        turtle.forward(a)
        turtle.right(b)
        a += 3
        b += 1
    time.sleep(1)
    turtle.bye()  

def main():
    print("====You can check all your Palindrome words here with hybrid====")
    string = input("Enter the word you want to check today: ")
    for numbers in range(len(string)):
        if ((ord(string[numbers]) < 65 or ord(string[numbers]) > 90) and (ord(string[numbers]) < 97 or ord(string[numbers]) > 122)):
           print("invalid selection\ntry again")
           main()
           
    
    print(get_palindrome(string))
           
    exit_num = input("Enter Anthing to Exit and M to Start Again: ")
    if exit_num == "M" or exit_num == "m":
        main()
    elif exit_num == "X" or exit_num == "x":
        print("Goodbye my lad")


def get_palindrome(string):
	reverse = ""
	for num in range(len(string)-1,-1,-1):
		reverse += string[num].upper()
	return reverse == string.upper()
print(reversed)
	

animation_thread = threading.Thread(target=show_animation)
animation_thread.start()


time.sleep(1)


main()
