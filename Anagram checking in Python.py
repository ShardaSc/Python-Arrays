# Input : str1 = “abcd”, str2 = “dabc”
# Output : True
#
# Input : str1 = “abcf”, str2 = “kabc”
# Output : False
str1 = "abcf"
str2 = "dabc"
# Output : True
if sorted(str1) == sorted(str2):
    print("Is Annagram")
else:
    print("Is not Annagram")