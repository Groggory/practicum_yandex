
conversion_ml_l = 1000
days_water=30
while True:
    print('***' * 50)
    print('Добрый День,Я Ваш персональный помошник давайте познакомимся.=3',end='\n\n')
    print('***' * 50)

    name_user = input('Как я могу к Вам обращаться?')

    print('Очень приятно,',name_user,end='\n\n')
    try:
        age_user = int(input('Сколько Вам лет?'))
        if age_user < 10 or age_user > 90:
            print('Пожалуйста, укажите возраст (от 0 до 120).')
            continue

        growth_user_centi = int(input('Какой Ваш рост?'))
        if growth_user_centi <=70:
            raise ValueError("Рост должен быть не менее 70 см.",end='\n\n')
        growth_user_meter =float(growth_user_centi / 100)
        weight_user = round(float(input('Сколько килограммов ваш вес на данный момент? ')), 1)
        if weight_user <= 10:
            raise ValueError("Вес должен быть не менее 10 кг.",end='\n\n')
        break
    except ValueError as _:
        print('***' * 50)
        print("Пожалуйста, используйте только числа и корректные значения. Давайте начнём заново.",end='\n\n')
        print('***' * 50)



bmi = weight_user/ (growth_user_meter ** 2) # Индекс массы тела

water_ml = weight_user * days_water #Рассчитать норму воды в миллилитрах
water_l = water_ml / conversion_ml_l

print(f"\nДанные приняты!")
print(f"Возраст: {age_user} лет")
print(f"Рост: {growth_user_meter:.2f} м")
print(f"Вес: {weight_user:.1f} кг")
print(f"Ваш Индекс Массы Тела (BMI): {bmi:.2f}")
print(f"Рекомедумая норма воды в день: {water_l:.2f} литра")
print("Спасибо=3")

if bmi < 18.5:
    category = "недостаточный вес"
elif bmi < 25:
    category = "нормальный вес"
elif bmi < 30:
    category = "избыточный вес"
else:
    category = "ожирение"

print(f"Категория: {category}")