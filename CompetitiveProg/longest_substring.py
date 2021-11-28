#brute force
test_string = "abcbdca"
def get_longest_substring(string):
    if len(string) <= 1:
        return len(string)
    longest = 0
    for i, c in enumerate(string):
        string_cache = set()
        sec_pointer = i
        while (sec_pointer < len(string) and string[sec_pointer] not in string_cache):
            string_cache.add(string[sec_pointer])
            sec_pointer += 1
            longest = max(len(string_cache), longest)
        if len(string[i:]) < longest:
            break 
    return longest

print(get_longest_substring(test_string))

#optimized (sliding window) 

def get_longest_substring_v2(string):
    if len(string) <= 1:
        return len(string)
    longest = 0
    cache_chars = {}
    left = 0
    for right in range(len(string)):
        curr_char = string[right]
        prev_seen_char = cache_chars.get(curr_char)
        if prev_seen_char is not None and prev_seen_char >= left:
            left = prev_seen_char + 1
        cache_chars[curr_char] = right
        longest = max(longest, right - left + 1)
    return longest
