Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> x = np.array([i for i in range(1,21)])
>>> y == x ** 3
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    y == x ** 3
NameError: name 'y' is not defined
>>> y = x ** 3
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x00000240D52F0100>]
>>> plt.show()
>>> x = np.array([i for i in range(-21,21)])
>>> y = x ** 3
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x00000240D74B8E20>]
>>> plt.show()
>>> x
array([-21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10,  -9,
        -8,  -7,  -6,  -5,  -4,  -3,  -2,  -1,   0,   1,   2,   3,   4,
         5,   6,   7,   8,   9,  10,  11,  12,  13,  14,  15,  16,  17,
        18,  19,  20])
>>> y
array([-9261, -8000, -6859, -5832, -4913, -4096, -3375, -2744, -2197,
       -1728, -1331, -1000,  -729,  -512,  -343,  -216,  -125,   -64,
         -27,    -8,    -1,     0,     1,     8,    27,    64,   125,
         216,   343,   512,   729,  1000,  1331,  1728,  2197,  2744,
        3375,  4096,  4913,  5832,  6859,  8000], dtype=int32)
>>> y = x ** 2
>>> y
array([441, 400, 361, 324, 289, 256, 225, 196, 169, 144, 121, 100,  81,
        64,  49,  36,  25,  16,   9,   4,   1,   0,   1,   4,   9,  16,
        25,  36,  49,  64,  81, 100, 121, 144, 169, 196, 225, 256, 289,
       324, 361, 400], dtype=int32)
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x00000240D8F25430>]
>>> plt.show()
>>> plt.style.use('ggplot')
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x00000240D8E06BB0>]
>>> plt.show()
>>> plt.plot(x,y,'o')
[<matplotlib.lines.Line2D object at 0x00000240D8E6D730>]
>>> plt.show()
>>> plt.scatter(x,y)
<matplotlib.collections.PathCollection object at 0x00000240D8E6DF40>
>>> plt.show()
>>> x
array([-21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10,  -9,
        -8,  -7,  -6,  -5,  -4,  -3,  -2,  -1,   0,   1,   2,   3,   4,
         5,   6,   7,   8,   9,  10,  11,  12,  13,  14,  15,  16,  17,
        18,  19,  20])
>>> data = {"names" : ["John","Tom","Harry","Shawn","Sam","Peter"], "age" : [23,33,32,27,65,54]}
>>> plt.bar(data["names"], data["age"])
<BarContainer object of 6 artists>
>>> plt.show()
>>> plt.hist(data["age"])
(array([2., 0., 2., 0., 0., 0., 0., 1., 0., 1.]), array([23. , 27.2, 31.4, 35.6, 39.8, 44. , 48.2, 52.4, 56.6, 60.8, 65. ]), <BarContainer object of 10 artists>)
>>> plt.show()
>>> plt.hist(data["age"], bins=10)
(array([2., 0., 2., 0., 0., 0., 0., 1., 0., 1.]), array([23. , 27.2, 31.4, 35.6, 39.8, 44. , 48.2, 52.4, 56.6, 60.8, 65. ]), <BarContainer object of 10 artists>)
>>> plt.hist(data["age"], bins=100)
(array([1., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0., 1., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.]), array([23.  , 23.42, 23.84, 24.26, 24.68, 25.1 , 25.52, 25.94, 26.36,
       26.78, 27.2 , 27.62, 28.04, 28.46, 28.88, 29.3 , 29.72, 30.14,
       30.56, 30.98, 31.4 , 31.82, 32.24, 32.66, 33.08, 33.5 , 33.92,
       34.34, 34.76, 35.18, 35.6 , 36.02, 36.44, 36.86, 37.28, 37.7 ,
       38.12, 38.54, 38.96, 39.38, 39.8 , 40.22, 40.64, 41.06, 41.48,
       41.9 , 42.32, 42.74, 43.16, 43.58, 44.  , 44.42, 44.84, 45.26,
       45.68, 46.1 , 46.52, 46.94, 47.36, 47.78, 48.2 , 48.62, 49.04,
       49.46, 49.88, 50.3 , 50.72, 51.14, 51.56, 51.98, 52.4 , 52.82,
       53.24, 53.66, 54.08, 54.5 , 54.92, 55.34, 55.76, 56.18, 56.6 ,
       57.02, 57.44, 57.86, 58.28, 58.7 , 59.12, 59.54, 59.96, 60.38,
       60.8 , 61.22, 61.64, 62.06, 62.48, 62.9 , 63.32, 63.74, 64.16,
       64.58, 65.  ]), <BarContainer object of 100 artists>)
>>> plt.show()
>>> plt.pie(data['age'])
([<matplotlib.patches.Wedge object at 0x00000240D90D1D90>, <matplotlib.patches.Wedge object at 0x00000240D8F152B0>, <matplotlib.patches.Wedge object at 0x00000240D8F15730>, <matplotlib.patches.Wedge object at 0x00000240D8F15BB0>, <matplotlib.patches.Wedge object at 0x00000240D8F15FD0>, <matplotlib.patches.Wedge object at 0x00000240D90EB4F0>], [Text(1.0479725183836626, 0.33429567857303205, ''), Text(0.537161176940811, 0.9599259710975441, ''), Text(-0.39006544982124386, 1.0285178388612184, ''), Text(-1.0060977728472424, 0.4447103231001264, ''), Text(-0.7512774840289375, -0.8034812642440082, ''), Text(0.8233619569507337, -0.7294347728524179, '')])
>>> plt.show()
>>> plt.pie(data['age'], labels=data["names"])
([<matplotlib.patches.Wedge object at 0x00000240D9129790>, <matplotlib.patches.Wedge object at 0x00000240D9129C70>, <matplotlib.patches.Wedge object at 0x00000240D9138130>, <matplotlib.patches.Wedge object at 0x00000240D91385B0>, <matplotlib.patches.Wedge object at 0x00000240D9138A30>, <matplotlib.patches.Wedge object at 0x00000240D9138EB0>], [Text(1.0479725183836626, 0.33429567857303205, 'John'), Text(0.537161176940811, 0.9599259710975441, 'Tom'), Text(-0.39006544982124386, 1.0285178388612184, 'Harry'), Text(-1.0060977728472424, 0.4447103231001264, 'Shawn'), Text(-0.7512774840289375, -0.8034812642440082, 'Sam'), Text(0.8233619569507337, -0.7294347728524179, 'Peter')])
>>> plt.show()
>>> plt.pie(data['age'], labels=data["names"], autopct='%1.2f%')
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    plt.pie(data['age'], labels=data["names"], autopct='%1.2f%')
  File "C:\Python38\lib\site-packages\matplotlib\pyplot.py", line 2827, in pie
    return gca().pie(
  File "C:\Python38\lib\site-packages\matplotlib\__init__.py", line 1447, in inner
    return func(ax, *map(sanitize_sequence, args), **kwargs)
  File "C:\Python38\lib\site-packages\matplotlib\axes\_axes.py", line 3105, in pie
    s = autopct % (100. * frac)
ValueError: incomplete format
>>> plt.pie(data['age'], labels=data["names"], autopct='%1.2f%%')
([<matplotlib.patches.Wedge object at 0x00000240DA561BB0>, <matplotlib.patches.Wedge object at 0x00000240DA6772B0>, <matplotlib.patches.Wedge object at 0x00000240DA6778B0>, <matplotlib.patches.Wedge object at 0x00000240DA677EB0>, <matplotlib.patches.Wedge object at 0x00000240DA687460>, <matplotlib.patches.Wedge object at 0x00000240DA687A60>], [Text(1.0479725183836626, 0.33429567857303205, 'John'), Text(0.537161176940811, 0.9599259710975441, 'Tom'), Text(-0.39006544982124386, 1.0285178388612184, 'Harry'), Text(-1.0060977728472424, 0.4447103231001264, 'Shawn'), Text(-0.7512774840289375, -0.8034812642440082, 'Sam'), Text(0.8233619569507337, -0.7294347728524179, 'Peter')], [Text(0.5716213736638159, 0.18234309740347202, '9.83%'), Text(0.29299700560407865, 0.523595984235024, '14.10%'), Text(-0.21276297262976934, 0.5610097302879372, '13.68%'), Text(-0.548780603371223, 0.2425692671455235, '11.54%'), Text(-0.4097877185612386, -0.43826250776945896, '27.78%'), Text(0.4491065219731274, -0.39787351246495517, '23.08%')])
>>> plt.title("Age of employees")
Text(0.5, 1.0, 'Age of employees')
>>> plt.show()
>>> plt.pie(data['age'], labels=data["names"], autopct='%1.2f%%')
([<matplotlib.patches.Wedge object at 0x00000240DA44C8B0>, <matplotlib.patches.Wedge object at 0x00000240DA44CFA0>, <matplotlib.patches.Wedge object at 0x00000240DA45C5B0>, <matplotlib.patches.Wedge object at 0x00000240DA45CBB0>, <matplotlib.patches.Wedge object at 0x00000240DA46A1F0>, <matplotlib.patches.Wedge object at 0x00000240DA46A7F0>], [Text(1.0479725183836626, 0.33429567857303205, 'John'), Text(0.537161176940811, 0.9599259710975441, 'Tom'), Text(-0.39006544982124386, 1.0285178388612184, 'Harry'), Text(-1.0060977728472424, 0.4447103231001264, 'Shawn'), Text(-0.7512774840289375, -0.8034812642440082, 'Sam'), Text(0.8233619569507337, -0.7294347728524179, 'Peter')], [Text(0.5716213736638159, 0.18234309740347202, '9.83%'), Text(0.29299700560407865, 0.523595984235024, '14.10%'), Text(-0.21276297262976934, 0.5610097302879372, '13.68%'), Text(-0.548780603371223, 0.2425692671455235, '11.54%'), Text(-0.4097877185612386, -0.43826250776945896, '27.78%'), Text(0.4491065219731274, -0.39787351246495517, '23.08%')])
>>> plt.legend()
<matplotlib.legend.Legend object at 0x00000240DA43D9D0>
>>> plt.title("Age of employees")
Text(0.5, 1.0, 'Age of employees')
>>> plt.show()
>>> 