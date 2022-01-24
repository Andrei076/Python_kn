class Buffer:
    def __init__(self):
        self.my_list = []

    def add(self, *a):
        self.my_list.extend(a)
        while len(self.my_list) - 5 >= 0:
            print(sum(self.my_list[0:5]))
            self.my_list = self.my_list[5:]

    def get_current_part(self):
        return self.my_list


list_1 = Buffer()
list_1.add(5, 5, 4)
list_1.get_current_part()
list_1.add(6, 5, 8, 5)
list_1.get_current_part()
list_1.add(8, 8, 8, 8)
list_1.get_current_part()
list_1.add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
list_1.get_current_part()
