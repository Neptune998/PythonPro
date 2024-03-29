import time
from timeit import timeit


class Prime_no_generators(object):

    def __init__(self, end):
        self.end = end

    def sieve(self):
        # Create a boolean list of end elements
        prime_list = [True] * self.end
        prime_no = list()  # output list
        val = 2  # variable upto n
        while (val * val <= self.end):
            if prime_list[val] == True:
                for i in range(val * val, self.end, val):
                    # print(i,prime_list)
                    prime_list[i] = False
            val += 1
        # create a prime no list
        for i in range(len(prime_list)):
            if prime_list[i] and i != 1 and i != 0:
                prime_no.append(i)
        return prime_no


if __name__ == "__main__":
    while (True):
        n = int(input("Enter a +ve number to find the prime numbers: "))
        strtTime = time.perf_counter()
        obj = Prime_no_generators(n)
        prime_numbers = obj.sieve()
        print(*prime_numbers)
        print("There are " + str(len(prime_numbers)) + " prime numbers till " + str(n) + ".")
        comTime = time.perf_counter()
        print("Execution time :" + str(comTime - strtTime) + " seconds.")
