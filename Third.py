def third_question():
    import random
    import time
    
    # Алгоритм поразрядной сортировки является одним из наиболее быстрых алогритмов сортировки чисел,
    # со временем O(nk), где k - колчиество цифр.
    # В среднем, в сортируемых списках чисел, количество их цифр намного меньше количества элементов.
    # Таким образом для данного алгоритма сортировки более вероятно быстрее сортировать массив чисел,
    # чем для других алогритмов.
    
    base_list = list(map(lambda _: random.randint(1, 500), range(500000)))
    #base_list = [1, 156, 1569, 135792468, 125792468]
    timeStart = time.perf_counter()
    
    def radixSort(lst):
        radNum = len(str(max(lst)))
        bufLst = lst
        #Предполагаю что масив десятичных чисел
        numBase = 10
        
        for i in range(0, radNum):
            radGroups = [[] for _ in range(numBase)]
            for num in bufLst:
                digit = (num // (numBase ** i)) % numBase
                radGroups[digit].append(int(num))
            bufLst = sum(radGroups, [])
        return bufLst
    
    a = radixSort(base_list)
    print(time.perf_counter() - timeStart)
    if (a == sorted(base_list)):
        print(True)

third_question()
