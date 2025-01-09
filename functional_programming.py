import os

os.system('COLOR B')


def apply_all_func(int_list, *functions) -> dict:
    results = dict()

    for f in functions:
        results[f.__name__] = f(int_list)

    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

try:
    os.system('PAUSE')
except:
    os.system('CLS')
