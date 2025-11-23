print("Alive")


while True:
    user_age = input("zadej věk: ")
    try:
        user_age_as_int = int(user_age)

        print(f"Za deset let ti bude {10 + user_age_as_int}")
        print(f"Tady je číslo 100 vydělené tvým věkem {100 / user_age_as_int}")
        break
    except ValueError as err:
        print(f"Je nutné zadat číslo! Celý text chyby je {err}")
    except ZeroDivisionError:
        print("Věk nemůže bejt 0")
    finally:
        print("Inside finally")


print("After error")
