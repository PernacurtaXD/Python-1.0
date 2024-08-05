"""
Tipo Numérico


>>> 1_000_000
1000000

>>> 1_000_000_000
1000000000

>>> num = 42
>>> print(num)
42

>>> 
>>> num + 1
43

>>> print(num + 1)
43

_________________________________

-Primeira forma (+)

>>> num += 1 
>>> num
43


- Segunda forma (+)

>>> num = num + 1
>>> 
>>> num
44

__________________________________

- Primeira forma (-)

>>> num-=1
>>> num
43

- Segunda forma (-)

>>> num = num - 1
>>> num
42

___________________________________

- Primeira forma (*)
>>> num *= 2
>>> num
84


- Segunda forma (*)
>>> num = num * 2
>>> num
168

__________________________________

-Primeira forma (/)

>>> num /= 2
>>> num
84.0

- Segunda forma (/)

num = num / 2
>>> num
10.5

__________________________

>>> num = 43
>>> num
43

- Arredondado
>>> num //= 2
>>> num
21
>>> 


type(num) -> Ele fala passa a variável ou valor, e fala o tipo de dado
<class 'int'>

name = "Luis Felipe de jesus Santana"
>>> type(name)
<class 'str'>

>>> num = 42
>>> num.__add__(8)
50

 5 /2 
2.5
>>> 
>>> int(5 / 2) -> "Cast"
2
>>> 5//2
2

"""

num = 1_000_000

print(num)