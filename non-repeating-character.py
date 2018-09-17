"""Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1."""
def non_rep(text):
    a= {}
    i =0
    for letter in text:
        a[letter] = i
        i +=1

    pos = 0
    for letter in text:
        if pos == a.get(letter, -1):
            return pos
        else:
            try:
                del a[letter]
            except:
                pass
        pos +=1
    return -1


#Example:
s = "leetcode"
non_rep(s)  #return 0
s = "loveleetcode"
non_rep(s)  #return 2
s = "aabb"
non_rep(s)  #return -1

