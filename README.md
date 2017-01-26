# Теория алгоритмов

Курс для студентов 3-го года программы [Фундаментальная и компьютерная лингвистика](https://www.hse.ru/ba/ling/)

* [Процесс отправки заданий](meta/git_workflow.md)

# Программа курса

По задумке, каждому нумерованому пункту будет соответствовать лекция (прямой шрифт) и семинар (курсивный шрифт). 

1. Анализ алгоритмов. Асимптотическое оценки вычислительной сложности.
  ([семинар](https://mkuznets.com/hse/2017-alg/seminar01.pdf), [листок](https://mkuznets.com/hse/2017-alg/problems01.pdf))
	* Вычислительная модель компьютера с памятью с произвольным доступом
	* Операторы и выражения Python в терминах процессорных команд
	* Классы O, Ω, Θ
	* Оценка времени и памяти в лучшем, худшем и среднем случаях. Амортизационная сложность.
	* Сравнение темпов роста функций. Типичные для анализа алгоритмов асимптотические классы.
	* *Примеры: возведение в целую степень, числа Фибоначчи, умножение Карацубы.*
2. Типы и структуры данных
   ([лекция](https://mkuznets.com/hse/2017-alg/lecture02.pdf), [листок](problems/02))
	* Список и его реализации: массив, связный список (одно- и двусвязный), динамический массив. Бинарный поиск в массиве. `list` в Python.
	* Стек, очередь, двухсторонняя очередь. Их реализация через динамический массив и двусвязный список. `deque` в Python.
	* Коллекции с быстрыми добавлением, удалением и поиском.
		* Словарь. Реализация через бинарное дерево и хэш-таблицы.
		* Разрешение коллизий: цепочки, открытая адресация (линейное пробирование).
		* Множество. Реализация через хэш-таблицу.
	* *Частные случаи, задачи*
		* *Алгоритмы без дополнительной памяти (in-place)*
		* *Многомерные массивы*
		* *Цикл в связном списке*
		* *Применения стека: поддержка рекурсии, скобочные выражения*
		* *LRU-кэш*
3. [предварительно] Сортировка
4. [предварительно] Поиск
5. [предварительно] Графы


