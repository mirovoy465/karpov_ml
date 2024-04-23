#Теперь, когда мы определились со структурой данных, мы можем создать свою записную книжку.
#Ее содержание должно быть следующим: 
tasks = {0 : ['Feed the cat', 'Feed the cat2','Feed the cat'],
         1 : ['Water the flowers', 'Get the mail'],
         2 : ['Read a book'],
         3 : ['Respond to auntie']
         }

#Сейчас мы хотим выполнить простую проверку: если есть задачи нулевого приоритета,
#программа должна выводить строку "есть срочные дела", иначе —  "можно отдохнуть".
def has_important(tasks):
    if any(tasks[0]): 
        print("There is some important business")
    else:
        print("It's ok to chill")
# Demo
# has_important(tasks)
# tasks[0].pop()
# has_important(tasks)

# В этом задании мы продолжим работать со словарем tasks, в котором содержатся задачи разного приоритета, и напишем свой первый цикл!
# Проитерируйтесь по ключам словаря и добавьте его значения (списки задач) в список values.
def return_values(tasks):
    values = []
    for i in tasks.keys():
        values.append(tasks[i])
    return values
# Demo
# print(return_values(tasks))

# Немного усложним задачу. Прежде мы итерировались по ключам словаря и сохраняли его значения —  списки задач. 
# Теперь мы хотим сохранить не списки задач, а сами задачи. 
# Для этого необходимо проитерироваться по всем объектам в значениях словаря и добавить задачи в список doings.
def return_doings(tasks):
    doings = []
    for task_list in tasks.values():
        for task in task_list:
            doings.append(task)
    return doings
# Demo
# print(return_doings(tasks))

# Это задание включает часть идей реализации из предыдущего, но теперь, помимо итерации по всем ключам и значениям, 
# вам необходимо отобрать только те задачи, в которых есть подстрока "кот", и добавить их в список answer.
def find_cat_tasks(tasks):
    answer = []
    for key in tasks:
        for task in tasks[key]:
            if 'cat' in task:
                answer.append(task)
    return answer
# Demo
# print(find_cat_tasks(tasks))

# Мы будем итерироваться по ключам словаря tasks, брать задания оттуда и по одному добавлять их в список answer. 
# Вот только мы хотим уберечь себя от большого количества задач, поэтому в процессе будем проверять, не взяли ли мы уже на себя слишком много работы.
# Сегодня мы ленимся, поэтому готовы взять только самые срочные задания. Конкретно — только те, приоритет которых меньше двух.
# Если длина списка answer достигает двух, то мы решаем, что дел на сегодня уже достаточно, и прерываем выполнение цикла. 
# И еще важный момент — в список нужно добавлять только задачи в которых содержится подстрока "кот". 

def find_cat_tasks_2(tasks):
    answer = []
    for key in range(2):
        for task in tasks[key]:
            if len(answer) >= 2:
                break
            if 'cat' in task:
                answer.append(task)
    return answer
# Demo
# print(find_cat_tasks_2(tasks))

# Последняя неделя выдалась тяжелой, и вам постоянно приходилось в спешке добавлять в записную книжку новые задачи. 
# Теперь одна и та же задача в вашей книжке может дублироваться! Дедлайны вовсю бьют, поэтому вы готовы садиться за задачи без разбора их порядка.
# Вам дан словарь с задачами tasks. Пройдитесь по всем ключам и устраните дублирование только в рамках значений, соответствующих одному ключу. 
# Создайте новый словарь new_tasks, в котором будут те же ключи и те же задачи, но уже без дублей.

def remove_duplicates(tasks):
    new_tasks = {}
    for key in tasks:
        new_tasks[key] = list(set(tasks[key]))
    return new_tasks
# Demo
# print(remove_duplicates(tasks))