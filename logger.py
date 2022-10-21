def write_new(new_contact):
    with open('book.txt','a',encoding ='utf-8') as f:
        f.write(f'{new_contact}\n')

def get_book():
    book = []
    with open('book.txt','r',encoding ='utf-8') as f:
        for line in f:
            book.append(line)
    return (book)
        