
class tok:
    num = 0
    def __init__(self):
        self.num = 34

pre_filter1 = lambda d: d.num > 0 #noqa

s = tok()
print(pre_filter1(s))