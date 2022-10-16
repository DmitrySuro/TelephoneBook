import telephone_book as tb
import view

t_book = {}
print(t_book)

def writing_down(t_book=t_book):
    name = view.get_name()
    number = view.get_number()
    action = view.what_to_do()
    if action == 'contact':
        if name[0] not in t_book:
            t_book = tb.add_new_person(name, t_book, number)
        t_book = tb.person_create(name, t_book[name[0]], number)
    elif action == 'смена номера':
        t_book = tb.person_update(name, t_book[name[0]], number)
    elif action == 'дополнительный номер':
        t_book = tb.number_append(name, number, t_book[name[0]])
    view.export_book(t_book)
    
