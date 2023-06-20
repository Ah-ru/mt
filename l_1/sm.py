word = input("Write word")
if word.lower() == word.lower()[::-1]:
    print("Word is palindrome")
else:
    print("Word isn't  palindrome")