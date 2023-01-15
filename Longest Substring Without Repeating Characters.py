class Solution(object):
    def lengthOfLongestSubstring(self, s):
        currentMax = 0
        currentString = ""
        
        for i in xrange(len(s)):
            # If the character is new, add to our current substring
            if s[i] not in currentString:
                currentString += s[i]
                if len(currentString) > currentMax:
                    currentMax = len(currentString)
            # If the character is not new, slice away the old character and anything before it,
            # and then add the character to our current substring 
            else:
                oldCharPosition = currentString.find(s[i])
                currentString = currentString[oldCharPosition + 1:] + s[i]
                        
        return currentMax
