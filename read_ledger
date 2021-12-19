# Takes a long string formatted as a repetition of [sender] => [receiver] £[amount] [datetime] 
# and converts it into a list of tuples in the format [(sender, receiver, amount, datetime), ...].

def read_ledger(s):
    l = [] 
    if len(s) < 29:
        return l #less than the minimum amount of characters returns an empty list
    for i in s.split("\n"):
        l.append(i.split()) #loop through a list of entries and then append the split list of each
    for v in range(len(l)):
        l[v].remove("=>") #remove excess character
        l[v][2] = int(l[v][2][1:]) #turn the amount part of the entry into an integer 
    return [tuple(x) for x in l] #list comprehension to turn each entry into a tuple
