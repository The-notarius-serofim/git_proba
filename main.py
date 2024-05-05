"""
cat .git/ORIG_HEAD - просмотр индт. коммита


git status --статус внесенных изменений
git add main.py добавление одного файла
git add . добавление всех файлов
git add -f . < путь к файлу который находится в гит игнор>
git reset HEAD . <путь к директории >удаление ненужной директории из git

git com добавление с вызовом редактора при длянных сообшенийх
git com -m ' нужно ввести сообщение' добавление без вызова редактора
git com -a добавление изменений в обход index
git com -am ' текст коммита' тоже самое но без вызова текстового редактора
git allcom - добавление и коммит
git acp -добавление комит и пуш

git rm <path> удаление файла
git rm --cached <path> удаление из индекса но не из рабочего файла
git rm -r <path> удаление дирректории
git rm -r cached <path> удаление из индекса но не из рабочего файла

git mv файл что нужно переименовать--<path> новое название файла--<path>

git branch просморт ветки
git branch -v просмотр ветки и верщины ветки(последнего коммита в ветке)
git branch feature-название ветки --- создание новой ветки
git branch -f master 54a4 команда используется тогда,когда необходимо создать ветку в процессе разработки
в ветке мастер,т.к мастер это основная ветка для инф 100 изменений
в даннном случае мы сначала создаем новую ветку, после этого переносим в нее последнии коммиты из master
а ветку мастер передвигаем к нужному нам коммиту

git checkout -b feature общая команда которая создает ветку и переключает на нее
git checkout -B тот же функционал, что и в git branch -f master 54a4
git checkout -f feature  при переходе на другую ветку изменения в текущей не сохраняются
git checkout -f HEAD если нужно удалить все изменения в ветке(которые были без коммита)
git checkout -f  без указания ветки тоже работает т.к по умолчанию без указания ветки мы остаемся в той же
git checkout <название ветки или коммит(54a4)> <название файла > восстанавливаем содержание файла на момент коммита
git checkout HEAD <название файла> восстанавливаем последнюю версию файла, сохраненную в git
git checkout  <название файла> тоже самое как и прошлый но без указания конкретной дирректории так как если путь указан а коммит нет,
то восстановление идет в текущую директорию
git checkout -- master двойной -- указывает на то, что нужно искать файл с таким именем а не ветку


git stash - архивирует специальным образом изменения в файле для того, что бы можно было переключиться
git stash pop возвращает инфу в файл (важно,файл менять нельзя)
можно сохранить изменения на одной ветке а перенести на другую
нужно относиться внимательнее ну и можно использовать для переноса части кода

git cherry-pick

git log -просмотр коммитов
git log --oneline более удобный способ просмотра коммитов

git show <индт, комита или ветки>-просмотр конкретного коммита
git show <инд. коммита >~ (значек называется тильда) количество их обозночает количесво коммитов назад для просмотра
git show <инд. коммита>~2/3/4/5 можно указать тильду и число/цифру для просмотра коммитов
git show "@~" вместо HEAD можно ставить @
git show "@~:main.py" -изменения конкретного файла
git show :/указываем то что ищем ---- если мы не помним коммит а помним ту функцию что добавляли и нужно их глянуть

git merge <feature> находясь на ветке в которую нужно произвести слияние  прописываем название ветки которую нужно перенести






"""


"""
добавление текстового редакотора для git commit
git config --global core.editor "'C:\Program Files\Sublime Text/subl.exe' -w"
"""

"""
после выполненеия команд на вывод количесвта информации нажимаем q
"""
"""
вывод информации о измениях 
git show --pretty=fuller

"""

"""
git com -p main.py коммитим только избранные изменения
вылетает меню 
(1/2) Stage this hunk [y,n,q,a,d,e,p,?]? ?
где:
т - выставляй этот кусок
на всеобщее обозрение, 
н - не выставляй этот кусок на всеобщее обозрение.
q - завершите работу; не добавляйте этот фрагмент или любой из оставшихся
a - добавляйте этот фрагмент и все последующие фрагменты в файл
d - не добавляйте этот фрагмент или любой из более поздних фрагментов в файл
e - отредактируйте текущий фрагмент вручную
p - распечатайте текущий фрагмент
? - распечатать справку

(2/2) Stage this hunk [y,n,q,a,d,e,p,?]? ?

вылетают несколько шагов по одобрению комитов 
 и есть выбор что добавлять а что нет

"""




