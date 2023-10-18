# biz range() funksiyasiga faqat,
# integer ya'ni butun son berishimiz mumkin
# float o'nlik son berganimizda esa
# TypeError: 'float' object cannot be interpreted as an integer
# yani 'float' xuddi butun son kabi interprete qilinmaydi
# chunki range() funksiyasi floatni support ya'ni uni qo'llamaydi
# ammo float sonlarni ketma-ketligini hosil qiluvchi funksiya yasashimiz mumkin

def iterate_floats(foo, bar, buzz):
    while foo < bar:
        yield foo
        foo += buzz

for i in iterate_floats(0.0, 1.0, 0.1):
    print(round(i, 1))


