
def archive(name, surname, birth_year, city, email, phone):
    print(f"Имя - {name}; Фамилия - {surname}; Год Рождения - {birth_year}; Город - {city}; Email - {email}; Телефон - {phone}")

archive(name=input('Введите Имя:'), surname=input('Введите Фамилию:'), birth_year=input('Введите год рождения:'),
                city=input('Введите Город:'), email=input('Введите email:'), phone=input('Введите Телефон:'))