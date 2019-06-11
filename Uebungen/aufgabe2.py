import datetime

def age_checker():
    age = input("give me your age: ")
    year = int(datetime.date.today().year) - int(age)
    print(year + 100)

age_checker()
