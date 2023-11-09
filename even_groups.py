# funxtion that takes two integers as input and splits the the first input a in b groups evenly as possible

def split_integer(a,b):
    divider, rest = divmod(a,b) # first take the divider and the rest from the divions of both numbers
    qoutient_parts = b - rest # get the number of groups that take the divier as element by subtracting the amount of rests from the second number
    groups = qoutient_parts * [divider] # create a list that has the number of divider elements that are taken as they are
    end_with_rests = rest * [divider+1] # create the rest list where each elemtne is one larger than the numbers of the divider 
    return groups+end_with_rests # get them together


print(split_integer(7,3))
print(split_integer(13,3))