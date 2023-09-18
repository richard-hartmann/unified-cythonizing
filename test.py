import foo

assert foo.foo_c.crazy_abs_value(4) == 4
assert foo.foo_c.crazy_abs_value(-4) == 4

assert foo.bar.bar_c.crazy_square(4) == 16

f = foo.Fooby()
print(f())
