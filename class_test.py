class Fruit(object):
    version = 1.0
    color = 'red'

    def __init__(self):
        super(Fruit, self).__init__()
        self.color = 'blue'

    def is_clean(cls):
        print
        cls.color
        return True

    @classmethod
    def foo(cls):

        Fruit.version += 1
        print
        cls.color
        print
        'calling this method foo()'

    @staticmethod
    def pish_color(color):

        Fruit.color = color

    def add_foo(self):
        Fruit.version += 1


if __name__ == "__main__":
    o = Fruit()
    o.is_clean()
    Fruit.foo()
