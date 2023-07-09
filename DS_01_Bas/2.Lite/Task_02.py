print()
print('- - - - - - - - - - - - - - - - - - ')
print('Задача 2.')
print('- - - - - - - - - - - - - - - - - - ')
print('--- Перед вами стоит задача посчитать финансовые расходы за месяц. ---')
print('--- Ежедневно вы фиксировали свои траты и в итоге составили список расходов: ---')
print('--- Чтобы не ошибиться и точно посчитать свои траты, произведите вычисления тремя разными способами: ---')
print('--- 1. С помощью цикла \'while\'; ---')
print('--- 2. С помощью цикла \'for\'; ---')
print('--- 3. С помощью встроенной функции \'sum()\'. ---')
print('--- 4. С помощью Рекурсии 1. ---')
print('--- 5. С помощью Рекурсии 2. ---')
print('- - - - - - - - - - - - - - - - - - ')
print()

# -F- ------------------------------------------------------
# |--- -----------------------------------------------------
# 1. 'While'.
def SumWhile(v):
  light_purchases = len(purchases)
  result, count = 0, 0
  while count < light_purchases:
    result += purchases[count]
    count += 1
  print(f"Траты за месяц составили: {result} рубля. (в 'f')")
  return result
# |--- -----------------------------------------------------
# 2. 'For'.
def SumFor(w):
  summa = 0
  for i in purchases:
      summa += i
  print(f"Траты за месяц составили: {summa} рубля. (в 'f')")
  return summa
# |--- -----------------------------------------------------
# 3. 'Sum'.
def SumSum(x):
  print(f"Траты за месяц составили: {sum(purchases)} рубля. (в 'f')")
  return sum(purchases)
# |--- -----------------------------------------------------
# 4. 'Рекурсия 1'.
def RecSum1(y):
    if len(y)==0:
        return 0
    else:
        return y[0] + RecSum1(y[1:]) 
# |--- -----------------------------------------------------
# 5. 'Рекурсия 2'.
def RecSum2(z):
    return z[0] + RecSum2(z[1:]) if z else 0
# |--- -----------------------------------------------------
# -F- ------------------------------------------------------
# [ ] -------------------------------------------------->->->

# Список расходов
purchases = [1200, 800, 468, 235, 5800, 1350, 110, 243, 
            767, 3500, 5400, 4389, 3690, 2420, 894, 
            1766, 2100, 450, 328, 1890, 233, 766, 1765,
            237, 679, 1983, 389, 1760, 2100, 253, 789]

# |--- -----------------------------------------------------
# 1. 'While'.
print (f"     - 1. While -")
print (f"Траты за месяц составили: {SumWhile(purchases)} рубля")
print()
# |--- -----------------------------------------------------
# 2. 'For'.
print (f"     - 2. For -")
print (f"Траты за месяц составили: {SumFor(purchases)} рубля")
print()
# |--- -----------------------------------------------------
# 3. 'Sum'.
print (f"     - 3. Sum -")
print (f"Траты за месяц составили: {SumSum(purchases)} рубля")
print()
# |--- -----------------------------------------------------
# 4. 'Рекурсия 1'.
print (f"     - 4. Рекурсия 1 -")
print (f"Траты за месяц составили: {RecSum1(purchases)} рубля")
print()
# |--- -----------------------------------------------------
# 5. 'Рекурсия 2'.
print (f"     - 5. Рекурсия 2 -")
print (f"Траты за месяц составили: {RecSum2(purchases)} рубля")
# |--- -----------------------------------------------------

# [ ] -------------------------------------------------<-<-<-
print()
print('- - - - - - - - - - - - - - - - - - ')
print('- - - - - - - - - - - - - - - - - - ')
print()
# |--- -----------------------------------------------------
# 1. Подсчет расходов с помощью цикла while
print('   - 1.* Препод. - цикла "while" -')

month_spending = 0                    # Счетчик расходов в начале месяца равен нулю
i = 0                                 # Счетчик количества чеков
while i < len(purchases):             # Пока номер элемента меньше количества чеков
    month_spending += purchases[i]    # Увеличение счетчика расходов на сумму текущего чека
    i += 1                            # Увеличение количества чеков на 1
# Вывод результата
print('Траты за месяц составили:', month_spending, 'рубля')
print()
# |--- -----------------------------------------------------
# 2. Подсчет расходов с помощью цикла for
print('   - 2.* Препод. - цикла "for" -')

month_spending = 0                    # Счетчик расходов в начале месяца равен нулю
for i in purchases:                   # Для каждого элемента списка расходов    
    month_spending += i               # Увеличение счетчика расходов на сумму текущего чека
# Вывод результата    
print('Траты за месяц составили:', month_spending, 'рубля')
# |--- -----------------------------------------------------
print()
print('- - - - - - - - - - - - - - - - - - ')
print()