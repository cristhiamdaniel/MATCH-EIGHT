import sys

class PairsFinder:
    def __init__(self, argv):
        self.argv = argv
        self.run()
    def convert_list(self, l):
        '''
        Objective: To convert a list of strings to a list of integers
        :param l: List of strings
        :return: List of integers
        '''
        return list(map(int, l))
    def find_pairs(self, arr, sum):
        '''
        Objective: To find pairs of elements in a list whose sum is equal to a given number
        :param arr: List of elements
        :param sum: Sum of elements
        :return: List of pairs
        '''
        pairs = [(num, sum - num) for i, num in enumerate(arr) if num != sum - num and (sum - num) in arr[:i] + arr[i + 1:] and num < sum - num]
        return pairs
    def read_file(self, name):
        '''
        Objective: To read the data from a file
        :param name: Name of the file
        :return: List of strings
        '''
        with open(name, 'r') as file:
            lines = list(map(str.strip, file.readlines()))
        return lines
    def run(self):
        '''
        Objective: To find pairs of elements in a list whose sum is equal to a given number
        :return: None
        '''
        if len(self.argv) == 3:
            l = self.convert_list(self.argv[1].split(','))
            result = self.find_pairs(l, int(self.argv[2]))
            print(*result, sep='\n')
        elif len(self.argv) == 2:
            tex = self.read_file(self.argv[1])
            for i in range(len(tex)):
                l = self.convert_list(tex[i].split()[0].split(','))
                result = self.find_pairs(l, int(tex[i].split()[1]))
                print(*result, sep='\n')
        else:
            print("the data is not correct")

if __name__ == '__main__':
    pairs_finder = PairsFinder(sys.argv)
