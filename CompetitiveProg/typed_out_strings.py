# if char is equals to # it means ig is a back space
# compare if 2 strings are the same example abcd#abcd == abcabcd 
def back_space_compare(s, t):
    p1 = len(s) - 1
    p2 = len(t) - 1
    while p1 >= 0 or p2 >= 0:
        if s[p1] == '#' or s[p2] == '#':
            if s[p1] == '#':
                back_count = 2
                while back_count > 0:
                    p1 -= 1
                    back_count -= 1
                    if s[p1] == '#':
                        back_count += 2
            if t[p2] == '#':
                back_count = 2
                while back_count > 0:
                    p2 -= 1
                    back_count -= 1
                    if t[p2] == '#':
                        back_count += 2
        else:
            if s[p1] != t[p2]:
                return False
            else:
                p1 -= 1
                p2 -= 2
    return True

              

