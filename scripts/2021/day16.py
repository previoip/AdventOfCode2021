class Puzzle:

    def __init__(self, verbose):
        self.data = None
        self.cache = None
        self.verbose = verbose

    def appendData(self, data):
        self.data = data

    def part1(self):
        return None

    def part2(self):
        return None

    def run(self, part):
        if part == 1:
            self.result = self.part1()
        else:
            self.result = self.part2()

        if self.verbose:
            self.dump()

    def dump(self):
        print('Dumping')
        print(self.data)
        return

    def getResult(self):
        return self.result

if __name__ == "__main__":
    print('no')