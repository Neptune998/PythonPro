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

    @staticmethod
    def usingDictionaryApproach(str1, str2):
        # if the length of the two strings is not the same, they are not anagrams.
        if len(str1) != len(str2):
            print("Ohh!! Strings are not anagrams.")
        # initialize the dictionary
        counts = {}
        # loop simultaneously through the characters of the two strings.
        for c1, c2 in zip(str1, str2):
            if c1 in counts.keys():
                counts[c1] += 1
            else:
                counts[c1] = 1
            if c2 in counts.keys():
                counts[c2] -= 1
            else:
                counts[c2] = -1
        # Loop through the dictionary values.
        # if the dictionary contains even one value which is
        # different than 0, the strings are not anagrams.
        for count in counts.values():
            if count != 0:
                print("Ohh!! Strings are not anagrams.")
        print("WOW!! Strings are anagrams.")


# driver code
if __name__ == "__main__":
    while (True):
        print("Enter two strings to check the anagram.", end='\n')
        s1 = input("Enter first string: ")
        s2 = input("Enter second string: ")
        print("Now select the approach?")
        print("1 for 'Sorted method approach'")
        print("2 for 'Counter method approach'")
        print("3 for 'Dictionary approach'")
        approach = int(input("Your input: "))
        strtTime = time.perf_counter()
        if (approach == 1):
            Anagram.usingSortedFunction(s1, s2)
        elif (approach == 2):
            Anagram.usingCounterFunction(s1, s2)
        elif (approach == 3):
            Anagram.usingDictionaryApproach(s1, s2)
        else:
            print("Enter a valid approach !!!")
        comTime = time.perf_counter()

        print("Execution time :" + str(comTime - strtTime) + " seconds.", end='\n\n')
        print("************ Try again ****************")

        # Supprt in python 3.10.0 or above
        # match approach:
        #     case 1:
        #         Anagram.usingSortedFunction(s1, s2)
        #     case default:
        #         print("Select a valid approach!!!")


# Time taken for 1,24,992 character long string.
# usingSortedFunction     :    0.037813200000000435
# usingCounterFunction    :    0.02657750000000192
# usingDictionaryApproach :    0.08346319999999707

# Time taken for 1,000,000 character long string.
# usingSortedFunction     :    0.24080619999999975
# usingCounterFunction    :    0.13294189999999162
# usingDictionaryApproach :    0.7257522999999964