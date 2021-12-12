from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

def main():
    r = Rectangle("синий", 21, 20)
    c = Circle("зеленый", 20)
    s = Square("красный", 20)
    print(r)
    print(c)
    print(s)


if __name__ == '__main__':
    main()