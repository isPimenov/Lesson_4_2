def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

inner_function #функция не вызывается из глобального пространства, тк она прописана в локльном пр-ве test_function
