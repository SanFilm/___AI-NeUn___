print()
print('- - - - - - - - - - - - - - - - - - ')
print()

# -F- ------------------------------------------------------

def del_from_tuple(tpl, elem):
    if elem in tpl:
        elem_index = tpl.index(elem)
        print('-> Что происходит в функции ?: ->'.rjust(99, '-'))
        print('ДО иск. элем.:    ', end = '')
        print(tpl[:elem_index])
        print('Искомый элемент:     ', end = '')
        print(f'   ({tpl[elem_index]})   ')
        print('ПОСЛЕ иск. элем.:          ', end = '')
        print(tpl[elem_index + 1:])
        print('<- Что происходит в функции ?: <-'.rjust(99, '-'))
        tpl = tpl[:elem_index] + tpl[elem_index + 1:]
    return tpl

tuple_3 = (2, 4, 6, 6, 4, 2)
element_3 = 6
print("Кортеж исходный: ", tuple_3, ". Элемент: ", element_3)
print("Кортеж финальный: ", del_from_tuple(tuple_3, element_3))
print()

# [ ] -------------------------------------------------<-<-<-
print()
print('- - - - - - - - - - - - - - - - - - ')
print()
