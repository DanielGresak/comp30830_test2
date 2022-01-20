import random
def main(text):
    print(text)


if __name__ == '__main__':
    main("hello world!")
    if random.randrange(0,2) == 1:
        did_this_change = False
    else: did_this_change = True
    if did_this_change:
        print("true")
        print("allgooddawg")