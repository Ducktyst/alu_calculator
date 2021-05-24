
def asssert_equal(expected, func, *params):
    got = func(*params)
    assert func(*params) == expected, f"Ожидалось \"{expected}\" Получено \"{got}\" Аргументы \"{', '.join(map(str, params))}\""
