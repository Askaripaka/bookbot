
import string


path = "books/frankenstein.txt"


def file_contents():
    with open(path) as f:
        contents = f.read()

    return contents


def wordcount():
    source = file_contents()
    words = source.split()
    no_of_words = len(words)

    print(f"{no_of_words} words found in the document\n")


def sort_param(d):
    return d["count"]


def report_data():

    mylist = []

    source_letters = string.ascii_lowercase
    source_file = file_contents().lower()

    for chars in source_letters:
        mylist.append({"chars": chars, "count": source_file.count(chars)})
    # print(mylist)

    mylist.sort(
        key=sort_param,
        reverse=True
    )

    return mylist


def report():
    print("-- Begin report of books/frankenstein.txt\n")
    wordcount()
    for row in report_data():
        print(f"The '{row["chars"]}' character was found {row["count"]} times")


report()
