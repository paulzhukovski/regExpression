import re

text = 'Robert Classen 1934, SSDSaasd sdsa234, epam-1999, 1231651500000 656562-2123 2 13er432 432 ' \
       ' прикол дача Минск, 124@mail.com p.zhukovski@gmail.com, post@tut.by 3rr232r3t34%$ DDSW    ' \
       ' AAAAAAA bbbbbbbbbbbbb babababa 214242e 1ewq e21  dom sad polisad Posisad COMPAN молодечно132'\
       ' админ Апельсин остров ежик google*, auto**, (post@tut.by 3rr232r3t34%$ DDSW)'\
       '                                                                           '

textnone = '       '

textExpression1 = r"\w+\d+\w+"
results1 = re.findall(textExpression1, text)
print(results1)
print('*'*100)

textExpression2 = r"[A-Z]{2,}"
results2 = re.findall(textExpression2, text)
print(results2)
print('*'*100)

textExpression3 = r"[А-Яа-я]{2,}\w+"
results3 = re.findall(textExpression3, text)
print(results3)
print('*'*100)

textExpression4 = r"[А-ЯA-Z][a-zа-я]+"
results4 = re.findall(textExpression4, text)
print(results4)
print('*'*100)

textExpression5 = r"\b[ауоыиэяюёе]\w+"
results5 = re.findall(textExpression5, text, flags=re.IGNORECASE)
print(results5)
print('*'*100)

textExpression6 = r"[^-\w+]\d+[^-@\w+]"
results6 = re.findall(textExpression6, text)
print(results6)
print('*'*100)

textExpression7 = r"\w+[*]+"
results7 = re.findall(textExpression7, text)
print(results7)
print('*'*100)

textExpression8 = r"\([^)]+\)"
results8 = re.findall(textExpression8, text)
print(results8)
print('*'*100)

textExpression9 = r"^\s+$"
results9 = re.fullmatch(textExpression9, textnone)
print(results9)
print('*'*100)