myset = {4, 5,}
your_set = {4, 5, 6, 7, 8, 9, 10}
print(myset.issuperset(your_set))





#.difference() print(myset.difference(your_set))Сравнивает первый сет со вторым. Отображает несовпадения первого сета
# .discard() Удаляет из сета указанное значение myset.discard(5) ВОЗВРАЩАЕТ None нужно принить на новой строке!!
# .dfference_update() Сравнивает два сета, удаляет совпадения из первого сета, возвращает None
# .intersection() print(myset.intersection(your_set)) показывает пересечения 1 СЕТА в сравнении со вторым можно методом (myset & your_set)
# .isdisjoint() Сравнивает два сета на совпадения, возвращает True если 1 сет не имеет общих данных со вторым
# .issubset() print(myset.issubset(your_set)) Спрашивает сет 1 это часть сета 2? Возвращает булево. True если 1 set полностью содержится в сет 2
# .issuperset() print(myset.issuperset(your_set)) Спрашивает сет 1 это суперсет сета 2? Возвратит True в случае если сет 1 полностью содержит в себе сет 2
# .union() Связывает два сета между собой и удаляет повторяющиеся данные print(myset | your_set) или myset.union(your_set)
