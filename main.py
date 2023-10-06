def fibonacci():
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(7):
        c = a + b
        print(c)
        a, b = b, c
def display_odd(list):
    for i in range(len(list)):
        if i%2 != 0:
            print(list[i])
def reverse(list):
    for i in range(len(list)):
        print(list[-(i+1)], end = " ")
def count_words(string):
    # count = 0
    # for i in range(1,len(string)):
    #     if not string[i].isalpha() and string[i-1].isalpha():
    #         count += 1
    list_words = string.split(" ")
    return len(list_words)
def count_vowels_in_word(word):
    count = 0
    for i in range(len(word)):
        if word[i] in "aeiouAEIOU":
            count += 1
    return count
def print_caps(list):
    for i in range(len(list)):
        print(list[i].upper())
def even_or_odd():
    for i in range(1,16):
        print(i, ": ", end = "")
        if i%2 == 0:
            print("even")
        else:
            print("odd")
def sum():
    num1 = int(input("Enter a number"))
    num2 = int(input("Enter another number"))
    return num1+num2
def main():
    #fibonacci()
    #display_odd([1,2,3,4,5])
    # reverse([1,2,3,4,5])
    string = """
    	ChatGPT has created this text to provide tips on creating interesting paragraphs.
    	First, start with a clear topic sentence that introduces the main idea.
    	Then, support the topic sentence with specific details, examples, and evidence.
    	Vary the sentence length and structure to keep the reader engaged.
    	Finally, end with a strong concluding sentence that summarizes the main points.
    	Remember, practice makes perfect!
    	"""
    print(count_words(string))
    # print(count_vowels_in_word("hello"))
    # animals = ['tiger', 'elephant', 'monkey', 'zebra', 'panther']
    # print_caps(animals)
    even_or_odd()
    print(sum())
main()

