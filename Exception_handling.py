# Try except finally

try:
    print("in the try block")
    print(1/0)
except:
    print("In the except block")
finally:
    print("In the finally block")


# Try raise except

while True:
    try:
        user = int(input())
        if user < 0:
            raise ValueError("please give positive number")
        else:
            print("user input: %s" % user)
    except ValueError as e:
        print(e)