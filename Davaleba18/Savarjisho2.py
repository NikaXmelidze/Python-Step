

from typing import Any


class Functor:
    def __call__(self, number):
        if number < 0:
            error = ValueError("Only positive numbers are allowed")
            raise error
        else:
            print(number)



my_functor = Functor()
my_functor(5)
my_functor(-5)