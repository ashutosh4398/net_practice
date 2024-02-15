# USING YIELD TO GENERATE A CO-ROUTINE
# sometimes, it is better to keep the function running instead of executing common steps again 
# and again

# eg. if a function is reading a common file and then searching from it
# here we dont have to keep reading a book again and again
# python, knows it's a coroutine by checking (yield)

def searcher():
    import time
    book_content = "some time consuming book reading..."
    time.sleep(4)
    
    
    while True:
        text = (yield) # indicate function to be used as a co-routine
        if text in book_content:
            print("Your text is in the book")
            continue

        print("Text is not in the book")

# search = searcher()
# print(search)
# search.send(None) # primer
# search.send("time")
# search.send("time")
# search.send("time")
# search.close()
        
def random_nums():
    for i in range(10):
        yield i

def random_nums_100():
    for i in range(100, 110):
        yield i

def generator():
    yield from random_nums()
    print("next generator")
    yield from random_nums_100()

gen = generator()
