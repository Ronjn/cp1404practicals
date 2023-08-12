from wikipedia import *

search_phrase = input("\nEnter search phrase: ")
while search_phrase != "":
    try:
        page = wikipedia.page(search_phrase, auto_suggest=False)
        print(f"Title: {page.title}\nSummary: {page.summary}\nURL: {page.url}")
    except PageError:
        print("That page does not exist!")
    search_phrase = input("Enter search phrase: ")