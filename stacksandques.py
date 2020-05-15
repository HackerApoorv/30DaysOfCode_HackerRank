import sys

class Solution:
    # Write your code here
    def __init__(self):
        self.queue = []
        self.stack = []

    def pushCharacter(self, item):
        self.stack.append(item)

    def popCharacter(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def enqueueCharacter(self, item):
        self.queue.append(item)

    def dequeueCharacter(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop(0)
# read the string s
s=input()
#Create the Solution class object
obj=Solution()

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    
