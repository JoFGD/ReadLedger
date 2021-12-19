#function takes list of tuples from read_ledger and returns a dictionary with each individual mapped to their final balance after all transactions.

def totalise_ledger(ledger):
    d = {}
    for i in ledger:
        for k in range(2):
            if i[k] in d: #if a transaction from any given individual has happened before (their name is already in d)
                if k == 0:
                    d[i[k]] -= i[2] #if k==0 then individual is sender and so should have amount subtracted
                else:
                    d[i[k]] += i[2] #otherwise add to balance (since it must be the receiver)
            else: #transaction has not happened before, so add new key:value pair to d
                if k == 0: 
                    d[i[k]] = -i[2] 
                else:
                    d[i[k]] = i[2]

    return d
