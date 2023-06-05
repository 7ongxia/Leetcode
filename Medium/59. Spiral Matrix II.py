class Solution:
    """
    1  2  3  4  5
    16 17 18 19 6
    15 24 25 20 7
    14 23 22 21 8
    13 12 11 10 9
    """

    def go_right(self) -> None:
        try:
            if self.response[self.i][self.j] is False:
                self.response[self.i][self.j] = self.value
                self.j += 1
                self.value += 1
                self.direction = "R"
            else:
                self.i += 1
                self.j -= 1
                self.direction = "D"
        except:
            self.i += 1
            self.j -= 1
            self.direction = "D"

    def go_down(self) -> None:
        try:
            if self.response[self.i][self.j] is False:
                self.response[self.i][self.j] = self.value
                self.i += 1
                self.value += 1
                self.direction = "D"
            else:
                self.j -= 1
                self.i -= 1
                self.direction = "L"
        except:
            self.j -= 1
            self.i -= 1
            self.direction = "L"

    def go_left(self) -> None:
        try:
            if (self.j) < 0:
                self.i -= 1
                self.j += 1
                self.direction = "U"
            elif self.response[self.i][self.j] is False:
                self.response[self.i][self.j] = self.value
                self.j -= 1
                self.value += 1
                self.direction = "L"
            else:
                self.i -= 1
                self.j += 1
                self.direction = "U"
        except:
            self.i -= 1
            self.j += 1
            self.direction = "U"

    def go_up(self) -> None:
        try:
            if (self.i) < 0:
                self.j += 1
                self.i += 1
                self.direction = "R"
            elif self.response[self.i][self.j] is False:
                self.response[self.i][self.j] = self.value
                self.i -= 1
                self.value += 1
                self.direction = "U"
            else:
                self.j += 1
                self.i += 1
                self.direction = "R"
        except:
            self.j += 1
            self.i += 1
            self.direction = "R"

    def generateMatrix(self, n: int) -> List[List[int]]:
        self.response = [[False for _ in range(n)] for _ in range(n)]
        self.i, self.j = 0, 0
        self.direction = "R"
        self.value = 1

        while self.value < (n * n) + 1:
            match self.direction:
                case "R":
                    self.go_right()
                case "D":
                    self.go_down()
                case "L":
                    self.go_left()
                case "U":
                    self.go_up()
                case _:
                    print("ERROR")

        return self.response
