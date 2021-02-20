class Board:
    def __init__(self):
        self.__rows = 16
        self.__cols = 16
        self.__matrix = [[0 for _ in range(self.__cols)] for _ in range(self.__rows)]

    def load(self, file_name):
        f = open(file_name, "r")
        for line in f.readlines():
            x, y = line.split(" ")
            x = int(x)
            y = int(y)
            self.__matrix[x][y] = 1

    def __str__(self):
        result = ""
        for i in range(self.__rows):
            for j in range(self.__cols):
                if self.__matrix[i][j] == 1:
                    result += "#"
                else:
                    result += "@"
            result += '\n'
        return result

    @property
    def all(self):
        result = []
        for i in range(self.__rows):
            for j in range(self.__cols):
                if self.__matrix[i][j] == 1:
                    result.append((i, j))
        return result

    def update(self, i, j):
        di = [0, 0, -1, -1, -1, 1, 1, 1]
        dj = [-1, 1, 0, 1, -1, -1, 1, 0]
        alive = 0
        for d in range(8):
            ii = i + di[d]
            jj = j + dj[d]
            if 0 <= ii < self.__rows and 0 <= jj < self.__cols and self.__matrix[ii][jj]:
                alive += 1
        if alive > 3 or alive < 2:
            return 0
        elif alive == 3:
            return 1
        return self.__matrix[i][j]

    def update_board(self):
        result = []
        for i in range(self.__rows):
            for j in range(self.__cols):
                result.append((i, j, self.update(i, j)))
        for elem in result:
            i, j, c = elem
            self.__matrix[i][j] = c


class SparseBoard:
    def __init__(self):
        self.__mat = {}
        pass

    def __setitem__(self, key, value):
        i, j = key
        if i not in self.__mat:
            self.__mat[i] = {}
        self.__mat[i][j] = value
        if self.__mat[i][j] is None or self.__mat[i][j] == 0:
            del self.__mat[i][j]

    def __getitem__(self, key):
        i, j = key
        if i not in self.__mat:
            return None
        if j not in self.__mat[i]:
            return None
        return self.__mat[i][j]

    @property
    def all(self):
        result = []
        for i in self.__mat:
            for j in self.__mat[i]:
                result.append((i, j))
        return result

    def load(self, file_name):
        f = open(file_name, "r")
        for line in f.readlines():
            x, y = line.split(" ")
            x = int(x)
            y = int(y)
            self.__setitem__((y, x), 1)

    def rules(self, i, j):
        di = [0, 0, -1, -1, -1, 1, 1, 1]
        dj = [-1, 1, 0, 1, -1, -1, 1, 0]
        alive = 0
        for d in range(8):
            ii = i + di[d]
            jj = j + dj[d]
            if self.__getitem__((ii, jj)):
                alive += 1
        if alive > 3 or alive < 2:
            return False
        if alive == 3:
            return True
        if self.__getitem__((i, j)) == 1:
            return True
        return False

    def update(self):
        di = [0, 0, -1, -1, -1, 1, 1, 1]
        dj = [-1, 1, 0, 1, -1, -1, 1, 0]
        new_board = SparseBoard()
        for i in self.__mat:
            for j in self.__mat[i]:
                for d in range(8):
                    ii = i + di[d]
                    jj = j + dj[d]
                    if self.rules(ii, jj):
                        new_board[(ii, jj)] = 1
        del self.__mat
        self.__mat = new_board.__mat

