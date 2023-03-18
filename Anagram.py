import time
from collections import Counter

class Anagram(object):
    def __int__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    @staticmethod
    def usingSortedFunction(str1, str2):
        if (sorted(str1) == sorted(str2)):
            print("WOW!! Strings are anagrams.")
        else:
            print("Ohh!! Strings are not anagrams.")

    @staticmethod
    def usingCounterFunction(str1, str2):
        if (Counter(str1) == Counter(str2)):
            print("WOW!! Strings are anagrams.")
        else:
            print("Ohh!! Strings are not anagrams.")


# driver code
if __name__ == "__main__":
    while (True):
        print("Enter two strings to check the anagram.", end='\n')
        s1 = input("Enter first string: ")
        s2 = input("Enter second string: ")
        print("Now select the approach?")
        print("1 for 'Sorted method approach'")
        print("2 for 'Counter method approach'")
        approch = int(input("Your input: "))
        strtTime = time.perf_counter()
        if (approch == 1):
            Anagram.usingSortedFunction(s1, s2)
        elif (approch == 2):
            Anagram.usingCounterFunction(s1, s2)
        else:
            print("Enter a valid approach !!!")
        comTime = time.perf_counter()

        print("Execution time :" + str(comTime-strtTime) + " seconds.", end='\n\n')
        print("************ Try again ****************")

        # Supprt in python 3.10.0 or above
        # match approach:
        #     case 1:
        #         Anagram.usingSortedFunction(s1, s2)
        #     case default:
        #         print("Select a valid approach!!!")
