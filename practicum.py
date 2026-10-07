caunter = True
while caunter:
    print('Добрый День,Я Ваш персональный помошник давайте познакомимся.=3')
    name_user = input('Как я могу к Вам обращаться?')
    print('Очень приятно,',name_user)
    age_user = int(input('Сколько Вам лет?'))
    growth_user_centi = int(input('Какой Ваш рост?'))
    growth_user_meter =float(growth_user_centi / 100)
    weight_user =float(input('Сколько килграммов Ваш вес на данный момоент?:'))
    caunter = False


bmi = weight_user/ (growth_user_meter ** 2) # Индекс массы тела

print(round(bmi,1))

water_ml = weight_user * 30 #Рассчитать норму воды в миллилитрах
water_l = water_ml / 1000
print(water_l)