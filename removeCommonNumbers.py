class NumberRemover:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def remove_numbers(self):
        result = ''.join([x for x in self.str1 if x not in self.str2])
        return result


str1 = "12345"
str2 = "45678"

remover = NumberRemover(str1, str2)

result = remover.remove_numbers()

print(result)
