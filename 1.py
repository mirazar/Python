m = ([[31, 37, 51], [-1, 0, 1], [22, 83, -1], [3, 5, 8, ]])
new_m = ([[22, 43, 86], [-2, 0, 2], [0, 2, -2], [8, 3, 7, ]])


class Matrix:

    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        return str('\n'.join(['\t'.join([str(el) for el in i]) for i in self.my_list]))

    def __add__(self, other):
        for i in range(len(self.my_list)):
            for i_2 in range(len(other.my_list[i])):
                self.my_list[i][i_2] = self.my_list[i][i_2] + other.my_list[i][i_2]
        return Matrix.__str__(self)


matrix1 = Matrix(m)
matrix2 = Matrix(new_m)

print(matrix1, '\n')
print(matrix2, '\n')
print(matrix1 + matrix2)
