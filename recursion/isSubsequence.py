# Write a recursive function named ​isSubsequence​ that
# takes two strings and returns true if the second string
# is a subsequence of the first string. A string is a
# subsequence of another if it contains the same letters
# in the same order, but not necessarily consecutively.
# You can assume both strings are all lowercase characters.
# For example,
#
# isSubsequence("computer", "core") false
# isSubsequence("​co​m​p​ut​e​r", "cope") true
# isSubsequence("​computer​", "computer") true



class Solution:
    def isSubsequence(self, str1, str2):
        if str2 == str1:
            return True




