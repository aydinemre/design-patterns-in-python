# Open Closed Principle
# OCP = Open for extension, closed for modification
from abc import ABC, abstractmethod
from enum import Enum
from typing import List


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name: str, color: Color, size: Size):
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:
    def filter_by_color(self, products: List[Product], color: Color):
        for p in products:
            if p.color == color:
                yield p

    def filter_by_size(self, products: List[Product], size: Size):
        for p in products:
            if p.size == size:
                yield p

    def filter_by_size_and_color(self, products: List[Product],
                                 size: Size, color: Color):
        for p in products:
            if p.color == color and p.size == size:
                yield p

    # 2 --> 3
    # 3 --> 7 c s w cs sw cw csw !!!


class Specification(ABC):
    @abstractmethod
    def is_satisfied(self, item: Product):
        pass

    def __and__(self, other):
        return AndSpecifications(self, other)


class Filter(ABC):
    @abstractmethod
    def filter(self, items: List[Product], spec: Specification):
        pass


class ColorSpecification(Specification):
    def __init__(self, color: Color):
        self.color = color

    def is_satisfied(self, item: Product):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size: Size):
        self.size = size

    def is_satisfied(self, item: Product):
        return item.size == self.size


class AndSpecifications(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item: Product):
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))


class BetterFilter(Filter):
    def filter(self, items: List[Product], spec: Specification):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == '__main__':
    products = [
        Product('Apple', Color.GREEN, Size.SMALL),
        Product('Tree', Color.GREEN, Size.LARGE),
        Product('House', Color.BLUE, Size.LARGE)
    ]

    pf = ProductFilter()
    print("Green products (old): ")
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f' - {p.name} is green')

    bf = BetterFilter()
    print("Green products (new): ")
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(f' - {p.name} is green')

    print("Large products (new): ")
    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large):
        print(f' - {p.name} is large')

    print('Large and blue items: ')
    large_blue = AndSpecifications(
        SizeSpecification(Size.LARGE),
        ColorSpecification(Color.BLUE)
    )
    for p in bf.filter(products, large_blue):
        print(f' - {p.name} is large and blue')

    # And operator override
    print('Large and blue items: ')
    large_and_blue = SizeSpecification(Size.LARGE) & ColorSpecification(Color.BLUE)
    for p in bf.filter(products, large_and_blue):
        print(f' - {p.name} is large and blue')
