def reverse_string(s):
        result = ""
        if len(s) <= 1:
            return s
        else:
            return reverse_string(s[1:]) + s[0]
