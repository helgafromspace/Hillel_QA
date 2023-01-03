"""Написать класс-миксин, наследуя который объект будет выводится в консоль в виде имени класса и словаря аттрибутов со значениями:
ClassName: {
    key: value
}
class AttributePrinterMixin:
    pass

Протектед и приватные аттрибуты должны выводить только свое имя (без знака подчеркивания для протектед и префикса "_<имя класса>__")

Каждя строка с полем начинается с символа табуляции.

Если класс наслудует другие классы, их аттрибуты тоже должны выводится по тем же правилам.

Свойства обрабатывать не надо.



Пример:
class A(AttributePrinterMixin):
    def __init__(self):
        self.public_filed = 3
        self._protected_field = 'q'
        self.__private_field = [1, 2, 3]

a = A()
print(a)
A: {
   public_filed: 3
   protected_field: q
   private_field: [1, 2, 3]
}


"""
class AttributePrinterMixin:
    def __str__(self):
        attr = {}
        for i in self.__dir__():
            if not i.startswith('__'):
                attr.setdefault(i, getattr(self, i))
        result = ''
        for i in attr:
            if '__' in i:
                    i__ = i.split('__')
                    result += f'    {i__[1]}: {attr[i]}\n'
            elif i.startswith('_'):
                i_ = i[1:]
                result += f'    {i_}: {attr[i]}\n'
            else:
                result += f'    {i}: {attr[i]}\n'
        return f'{self.__class__.__name__}: {{\n{result}}}'
class A(AttributePrinterMixin):
    def __init__(self):
        self.public_field = 3
        self._protected_field = 'q'
        self.__private_field = [1, 2, 3]

class B(A):
    pass

a = A()
print(a)
b = B()
print(b)


