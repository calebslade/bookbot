
def wordcount(book):
    bookList = book.split()
    return len(book)
    
def get_book_text(path):
    with open('books/frankenstein.txt') as f:
        return f.read()

def stringtoLower(string):
    lowered_string = string.lower()
    return lowered_string

def countCharacter(string):
    chars = [{"char":'a', "num":0}, {"char":'b',"num":0}, {"char":'c',"num":0}, {"char":'d',"num":0}, {"char":'e',"num":0}, {"char":'f',"num":0}, {"char":'g',"num":0}, {"char":'h',"num":0}, {"char":'i',"num":0}, {"char":'j',"num":0}, {"char":'k',"num":0}, {"char":'l',"num":0},
              {"char":'m',"num":0}, {"char":'n',"num":0}, {"char":'o',"num":0}, {"char":'p',"num":0}, {"char":'q',"num":0}, {"char":'r',"num":0}, {"char":'s',"num":0}, {"char":'t',"num":0}, {"char":'u',"num":0}, {"char":'v',"num":0}, {"char":'w',"num":0}, {"char":'x',"num":0}, {"char":'y',"num":0}, {"char":'z',"num":0}]
    for char in chars:
        for j in range(len(string)):
            if string[j] == char['char']:
                char['num'] += 1
    return chars

def sorton(dict):
    return dict['num']

def generateReport(chars):
    for char in chars:
        print(f"The '{char['char']}' character was found {char['num']} times")

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    wordCount = wordcount(text)
    text_lowered = stringtoLower(text)
    charCount = countCharacter(text_lowered)
    charCount.sort(reverse=True,key=sorton)

    print(f'--- Begin report of {path} ---')
    print(f"{wordCount} words found in the document")
    print()
    generateReport(charCount)
    print("--- End Report ---")
    #print(f"This document contains {wordCount} words!")
    #print(charCount)
    


main()