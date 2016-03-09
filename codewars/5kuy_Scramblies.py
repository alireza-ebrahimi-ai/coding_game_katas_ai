from collections import Counter
def scramble(s1, s2):
    return not(Counter(s2) - Counter(s1))

def scramble1(s1, s2):
    if len(s1) < len(s2):
        return False
    str1 = Counter(s1)
    str2 = Counter(s2)
    for x in xrange(len(s2)):
        if str1[s2[x]] < str2[s2[x]]:
            return False
    return True

def scramble2(s1,s2):
    if len(s1) < len(s2):
        return False
    for x in xrange(len(s2)):
        if s1.count(s2[x]) < s2.count(s2[x]):
            return False
    return True


print scramble('rkqodlw','world')
print scramble('cedewaraaossoqqyt','codewars')
print scramble('katas','steak')