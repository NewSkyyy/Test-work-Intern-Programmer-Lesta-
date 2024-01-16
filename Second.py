def second_question():
    from collections import deque
    import time
    import random
  
#   Реализация колцевого буфера FIFO при помощи двухсторонней очереди.
#   Старые элементы очереди всегда находятся слева, новые элементы очереди всегда находятся справа.
#   Размер списка изменятеся в зависимости от колличества элементов, но не превышает максимальный.

    class dequeCircleFIFO():
    
#       Размер буфера считается бесконечным, 
#       если в качестве размера указана отрицательная величина поля "maxsize".
#       Если указано положительное число, то максимальным размером буфера является величина "maxsize".

        def __init__(self, size = 0):
            self._maxsize = size
            
            self._init(self._maxsize)
        
        # Вывод максимального объема буфера
        def get_size(self):
            return self._maxsize
        
        # Вывод текущего объема буфера
        def get_current_size(self):
            return self._cursize()
        
        # Вывод текущего состояния буфера
        def get_entries(self):
            return list(self.buffer)
        
        # Добавление элемента в кольцевой буфер, с увеличением текущего колчиества элементов
        # или заменой самого раннего элемента (если буфер заполнен).
        def put(self, item):
            if self._maxsize > 0:
                if self._cursize == self._maxsize:
                    self._get()
                    self._put(item)
                else:
                    self._put(item)
            elif self._maxsize < 0:
                self._put(item)
            else:
                raise Exception("Буфер не может содержать элементов")
        
        # Удаление элемента из кольцевого буфера
        # В результате удаления элемент возвращает свое значение
        def get(self):
            if self._cursize() < 1:
                raise Exception("Буфер не содержит элементов")
            else:
                return self._get()
        
        def _cursize(self):
            return len(self.buffer)
        
        def _get(self):
            return self.buffer.popleft()
        
        def _put(self, item):
            self.buffer.append(item)
        
        def _init(self, size):
            if size < 0:
                self.buffer = deque(maxlen = None)
            else:
                self.buffer = deque(maxlen = size)
    
#   Реализация колцевого буфера FIFO при помощи списка и "указателей".
#   Список имеет постоянный размер. Элементы буфера могут находится в случайном месте списка,
#   по порядку их появления в буфере.
#   "Указатель чтения" указывает на самый старый элемент, "указатель записи" указывает на место записи будующего элемента.

    class listCircleFIFO():
    
#       Размер буфера ограничен и составляет величину поля "maxsize".
        
        def __init__(self, size = 0):
            self._maxsize = size
            self._init(self._maxsize)
            self._writePoint = 0
            self._readPoint = 0
        
        #Вывод текущего состояния буфера
        def get_entries(self):
            return list(self.buffer)
        
        # Добавление элемента в кольцевой буфер, с изменением положения "указателей"
        def put(self, item):
            if (self._maxsize > 0):
                if self._readPoint != self._writePoint:
                    self._put(item, self._writePoint)
                    self._writePoint += 1
                else:
                    if self.buffer[self._writePoint] is None:
                        self._put(item, self._writePoint)
                        self._writePoint += 1
                    else:
                        self._put(item, self._writePoint)
                        self._writePoint += 1
                        self._readPoint += 1
                if (self._writePoint == self._maxsize):
                    self._writePoint = 0
                if (self._readPoint == self._maxsize):
                    self._readPoint = 0
            else:
                raise Exception("Буфер не может содержать элементов")  
        
        # Удаление элемента из кольцевого буфера, с изменением положения "указателя чтения"
        # В результате удаления элемент возвращает свое значение
        def get(self):
            if (self._maxsize > 0):
                if self.buffer[self._readPoint] != None:
                    item = self._get(self._readPoint)
                    self._readPoint += 1
                    if self._readPoint == self._maxsize:
                        self._readPoint = 0
                    return item
                else:
                    raise Exception("Буфер не содержит элементов")
                    
            else:
                raise Exception("Буфер не может содержать элементов")

        def _put(self, item, writePoint):
            self.buffer[writePoint] = item
            
        def _get(self, readPoint):
            self.buffer.insert(readPoint+1, None)
            return self.buffer.pop(readPoint)
            
        def _init(self, size):
            if size < 0:
                self.buffer = []
            else:
                self.buffer = [None] * size
    
    buffSize = 15000
    entryList = list(map(lambda _: "%s" % random.randint(1, 9999999999999), range(buffSize)))
    #entryList = ["Apple", "Banana", "Citrus", "Donkey", "Elephant", "Flamingo"] 
 
    def timeTest(func):
        def wrapped(*args):
            timeStart = time.perf_counter_ns()
            res = func(*args)
            timeEnd =  time.perf_counter_ns()
            print("Время выполнения функции '%s': " % args[1].__name__, timeEnd-timeStart , "ns")
            return res
        return wrapped
    
    @timeTest
    def testBuffer(lst, cls, size = 5):
        buffer = cls(size)
        for i in range(0, 100):
            for entry in lst:
                buffer.put(entry)
            for entry in buffer.get_entries():
                buffer.get()
        
        return buffer.get_entries()
    
    # Время выполнения функций условно,
    # и показывает только относительную скорость работы буферов.
    #
    # В текущих реализациях классов, класс на основе двухсторонней очереди работает быстрее,
    # из-за моментального доступа удаляемым элементам (предполодительно O(1)), 
    # в то время как доступ к элементам в буфере с указателями осуществляется по индексу (предположительно О(n)).
    #
    # Постояноое изменение размера буфера на основе двухсторонней очереди, при больших размерах буфера,
    # может увеличить используемую память и время работы, во буфере с указателями такой проблемы нет.
    #
    testBuffer(entryList, dequeCircleFIFO, buffSize)
    testBuffer(entryList, listCircleFIFO, buffSize)

second_question()
