# Lesson Пространство имён


calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    a = len(string)
    a1 = str.upper(string)
    a2 = str.lower(string)
    count_calls()

    return a, a1, a2

def is_contains(string, list_to_search):
    b = str.lower(string)
    b1 = list_to_search
    count_calls()
    for i in range(len(b1)):
        b1[i] = b1[i].lower()
    if b in b1:
        return True
    else:
        return False


print(string_info('КвазиЛенд'))
print(is_contains('Квазиленд', ['Семиречье','Англия','Азия','Европа','Дальний Восток']))
print(string_info('СОБес'))
print(is_contains('Москва', ['Воронеж','Москва','Абакан','Ростов','Нижний-Новгород']))
print(string_info('КАВКАз'))
print(is_contains('Репа', ['Репа','Арбуз','Дыня']))



print(calls)

