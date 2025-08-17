# When you use [::-1]:-
# start = default (start of string)
# stop = default (end of string)
# step = -1 (which means move backwards)
# So, s[::-1] gives the reverse of the string.



def palindrome(s):
    #abhabe korte hole number ke string e rupantor kore nite hobe
    return str(s)==str(s)[::-1]

text=int(input())
print(palindrome(text))


# def check_string(t):
#     t=t.lower()
#     return t==t[::-1]
# string=str(input())
# print(check_string(string))