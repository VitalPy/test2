def polyndrom(s):
    s=s.replace(' ','')
    if s[::1]==s[::-1]:
        return True
    else:
        return False