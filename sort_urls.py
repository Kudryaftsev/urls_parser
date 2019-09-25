import re
from collections import Counter

pattern = r'/\w+'    #    Action : вернуть все символы после /. После первого вхождения, конечно.
prog = re.compile(pattern)

news = []

#   найти, обработать, поместить в список
with open('URLs.txt', 'r') as f:
    for line in f:
        line = line.strip()
        line = re.match( pattern, line )
        
        try:
#             print(line.group(0)) - - - строка нужна была для отладки

            news.append(line.group(0).replace('/', ''))    #    не смог сразу поставить правильные скобки
        except AttributeError:
            continue

# отсортировать
ready_news = Counter(news)
gaga = sorted(ready_news.items(), key=lambda x: x[1], reverse = True)

#   проверить работу
for i in gaga:
    print(i)