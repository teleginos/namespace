def test_function():
    def inner_function():
        print("Я в области видимости функции test_function\n")

    inner_function()


try:
    test_function()
    inner_runction()
except NameError as err:
    print(f"Ошибка: {err}\nФункция {str(err).split()[1]} находится в не видимости глобального окружения имен)")
