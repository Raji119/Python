class Calc:

        def data(self):
                self.a = int(input("Enter a Number:"))

        def __and__(self, other):
                r=self.a & other.a
                print(r)

        def __or__(self, other):
                r=self.a | other.a
                print(r)

        def __gt__(self, other):
                r=self.a > other.a
                print(r)

        def __lt__(self, other):
                r=self.a < other.a
                print(r)

        def __xor__(self, other):
                r=self.a ^ other.a
                print(r)

