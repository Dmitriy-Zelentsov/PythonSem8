import model
import logger

while True:
    mode = model.mode()
    if mode == 1 :
        logger.write_new(model.get_contact())
    elif mode == 2:
        contact = model.request()
        book = logger.get_book()
        print(model.find_contact(book,contact))
    elif mode == 3:
        book = logger.get_book()
        new_book = model.diff_contact(book)
    elif mode == 0:
        print('Выход')
        break
    else:
        print('Запрос неверный')
