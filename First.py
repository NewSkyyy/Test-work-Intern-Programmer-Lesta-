def first_question():
    import time
    # Преимущества и недостатки способов:
    # isEven работает быстрее для большинства значений
    # isEvenMod2 работает быстрее для сверх больших значений
    # isEvenMod работает медленнее других реализаций, является их аналогом
    
    evenNum = 1234
    oddNum = 1235

    def timeCheck(func):
        timeStart = time.perf_counter_ns()
        func(evenNum)
        timeEnd = time.perf_counter_ns()
        print("Время выполнения функции '%s': " % func.__name__, timeEnd-timeStart , "ns")
        return func
    
    @timeCheck
    def isEven(value):
        return value % 2 == 0

    # Сравнение последнего бита двоичного представления числа
    @timeCheck
    def isEvenMod(value):
        return bin(value)[-1] == '0'

    # Применение к поcледнему биту двоичного представления числа операции and
    @timeCheck
    def isEvenMod2(value):
        return not value & 1
    #Проверка корректности работы функций
    def Test(evenValue, oddValue):
        return (isEven(evenValue) and isEvenMod(evenValue) and isEvenMod2(evenValue)) and \
                not (isEven(oddValue) or isEvenMod(oddValue) or isEvenMod2(oddValue))
    
    print('Первое значение четное ({0}) , второе нечетное ({1}): {2}'.format(evenNum, oddNum, Test(evenNum, oddNum))) # Должно вывести True
    print('Первое значение четное ({0}) , второе нечетное ({1}): {2}'.format(oddNum, evenNum, Test(oddNum, evenNum))) # Должно вывести False

first_question()
