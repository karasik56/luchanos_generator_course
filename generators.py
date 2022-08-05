"""1.1 Напишите функцию, которая возвращает объект-генератор. Объект-генератор должен бесконечно долго возвращать
значения по запросу от 0 до бесконечности."""

def gen_1():
    a = 0
    while True:
        yield a
        a += 1

# gen = gen_1()
# print(next(gen))
# print(next(gen))
# print(next(gen))


"""1.2 Сделайте так, чтобы функция принимала на вход параметр start и stop и возвращала объект генератор. 
Объект-генератор должен возвращать значения в диапазоне от start до stop.
 Если start и stop не были заданы явно, то генератор должен возвращать значения от 0 до бесконечности."""

def gen_2(**kwargs):
    start = kwargs.get('start')
    stop = kwargs.get('stop')
    if start and stop:
        while start <= stop:
            yield start
            start += 1
    else:
        a = 0
        while True:
            yield a
            a += 1


# gen = gen_2(start=1, stop=2)
# print(next(gen))
# print(next(gen))
# print(next(gen))

"""1.3 Теперь идобавьте в функцию ещё один параметр generator_name. При возвращении каждого нового значения
 генератор должен писать на экране своё имя и то значение, которое он собирается вернуть"""


def gen_3(generator_name, **kwargs):
    start = kwargs.get('start')
    stop = kwargs.get('stop')
    if start and stop:
        while start <= stop:
            yield f'{generator_name}, {start}'
            start += 1
    else:
        a = 0
        while True:
            yield f'{generator_name}, {a}'
            a += 1


gen = gen_3(generator_name="best generator", start=1, stop=2)
print(next(gen))
print(next(gen))


"""1.4 Напишите логику консольного меню для пользователя так, чтобы пользователь мог ввести какое-то
 имя и границы для генератора и имел возможность создать сколь угодно много генераторов с разными именами
  и границами. Как только пользователь закончит ввод данных необходимо спрашивать пользователя о том из генератора
   с каким именем он хочет получить очередное значение и либо получать его, либо говорить, что значений больше нет,
    либо что такого генератора не существует."""


