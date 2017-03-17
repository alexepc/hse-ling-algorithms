# Теория алгоритмов

Курс для студентов 3-го года программы [Фундаментальная и компьютерная лингвистика](https://www.hse.ru/ba/ling/)

* [Оценки за задания](https://docs.google.com/spreadsheets/d/1Lwz38H7USB2HzAwjWA8EarTZ6FIvJI_kNmKAMUbJTaA/pubhtml)
* Как отправлять задания: [инструкция](meta/git_workflow.md), [видео](https://youtu.be/dpHrqlhC_NE)
* [О подозрениях в списывании](meta/cheating.md)

# Литература

* **CLRS:** Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest and Clifford Stein *Introduction to Algorithms*, 3rd edition, 2009
  (*Алгоритмы: построение и анализ*, 3-е издание, 2013)
* Steven Skiena *Algorithm Design Manual* (2nd edition, 2008)

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
		* Словарь. Реализация через хэш-таблицы.
		* Разрешение коллизий: цепочки, открытая адресация (линейное пробирование).
		* Множество. Реализация через хэш-таблицу.
	* *Частные случаи, задачи*
		* *Алгоритмы без дополнительной памяти (in-place)*
		* *Многомерные массивы*
		* *Цикл в связном списке*
		* *Применения стека: поддержка рекурсии, скобочные выражения*
		* *LRU-кэш*
3. Алгоритмы сортировки ([конспект](http://nbviewer.jupyter.org/github/mkuznets/hse-ling-algorithms/blob/master/lecture_notes/03_sorting.ipynb), [листок](problems/03))
	* Задача сортировки. Сортировки основанные на сравнениях (Comparison sort).
	* Сортировка вставками (Insertion sort)
	* Парадигма «разделяй и властвуй» (divide and conquer). Сортировка слиянием (Mergesort). Master theorem и её применение для оценки сложности.
	* Нижняя граница сложности сортировки, основанной на сравнениях.
	* *Quicksort. Поиск порядковых статистик (Selection problem).*
	* *Selection sort (как приквел к Heapsort)*
	* *Двоичная куча (Binary heap)*
	* *Heapsort*
4. Двоичные деревья 
	* *Определения, реализация, операции поиска* ([конспект](http://nbviewer.jupyter.org/github/mkuznets/hse-ling-algorithms/blob/master/lecture_notes/04_1_bst.ipynb))
		* *Поиск элемента*
		* *Поиск минимума/максимума*
		* *Обходы дерева: в глубину (pre-, in-, post-order), в ширину*
		* *Поиск следующего и предыдущего значений*
	* Динамические деревья поиска (главы 12.3, 13 и 18 в CLRS, [лекция в MIT](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-introduction-to-algorithms-sma-5503-fall-2005/video-lectures/lecture-10-red-black-trees-rotations-insertions-deletions/))
		* Операции добавления и удаление элементов
		* Сбалансированные деревья поиска (Balanced BST)
			* Красно-чёрное дерево (Red-Black Tree)
			* B-tree и общие свойства алгоритмов для внешней памяти
5. [предварительно] Графы
