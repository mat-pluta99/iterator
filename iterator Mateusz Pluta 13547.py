#Mateusz Pluta 13547

class CoffeeRecipeGet:
    def __init__(self, lst, reverse=False):
        self.lst = lst
        self.reverse = reverse
        if self.reverse:
            self.position = -1
        else:
            self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self.lst[self.position]
            if self.reverse:
                self.position -= 1
            else:
                self.position += 1
        except IndexError:
            raise StopIteration
        
        return item


class CoffeeRecipeList:
    def __init__(self, lst=list(), reverse=False):
        self.lst = lst
        self.reverse = reverse

    def __iter__(self):
        return CoffeeRecipeGet(self.lst, False)

    def reverse_iterator(self):
        return CoffeeRecipeGet(self.lst, True)

    def add_recipe(self, item):
        self.lst.append(item)
    def sort(self):
        self.lst.sort()

lst = CoffeeRecipeList()
lst.add_recipe("Espresso")
lst.add_recipe("Americano")
lst.add_recipe("Cappuccino")
lst.add_recipe("Latte")
lst.add_recipe("Macchiato")
lst.sort()
print("Przepisy na kawę:")
lst1 = print("\n".join(str(item) for item in lst))
print("")
print("Odwrotna lista przepisów na kawę:")
print("\n".join(str(item) for item in lst.reverse_iterator()))