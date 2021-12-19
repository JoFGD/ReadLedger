#function takes a ledger and returns true if in the correct order

def validate_ledger(s):
    u = []
    if len(s) < 1: #if the ledger is empty return True
        return True
    for i in s:
        u.append(i[3]) #create a list of the dates (4th element) for each entry
    return u == sorted(u) #return True if a sorted version of u = u
