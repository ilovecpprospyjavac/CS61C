def fizzbuzz(num):
    if num%3==0 and num%5!=0:
        print("num: fizz")
    elif num%5==0 and num%3!=0:
        print("num: buzz")
    elif num%3==0 and num%5==0:
        print("num: fizzbuzzcll")
    else:
        return
num = input()
num = int(num)
fizzbuzz(num)

