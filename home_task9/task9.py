class O:
    pass

class F(O):
    pass

class E(O):
    pass

class D(O):
    pass

class C(F, D):
    pass

class B(E, D):
    pass

class A(C, B):
    pass


print(A.__mro__)

# output:
# (<class '__main__.A'>, <class '__main__.C'>, <class '__main__.F'>, <class '__main__.B'>, <class '__main__.E'>, <class '__main__.D'>, <class '__main__.O'>, <class 'object'>)