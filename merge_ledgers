#merge ledgers while keeping all transactions in order, this is done without using a basic sort algorithm

def merge_two_ledgers(arg1, arg2 = 0):
    if arg2 == 0: #if arg2 is 0 then all args are contained in arg1, args split into ledger_a and ledger_b
        ledger_a = arg1[0]
        ledger_b = arg1[1]
    else:
        ledger_a = arg1
        ledger_b = arg2
    comb = ledger_a+ledger_b
    l = []
    dup = []
    
    if ledger_a == []: #if either ledger is empty then return the other
        return ledger_b
    elif ledger_b == []:
        return ledger_a

    for i in ledger_a:
        for j in ledger_b:
            if i[3] > j[3]: #compare dates in each ledger, if i[3] is greater than j[3] then add to new list
                l.append(i)
            else:
                l.append(j)
    #the resulting list is ordered with the last entry for each element being the true index
                
    for n in comb:
        if not n in l:
            l.insert(0,n) #using this method the foremost element will be missing
            
    for k in l[::-1]:
        if k in dup:
            l.remove(k) #if k is in a list of elements already in l then remove k
        if not k in dup:
            dup.append(k) #if k is not yet in a list of elements already in l (dup) then add k to dup
            
    return l


def merge_ledgers(*args):
    if len(args[0]) == 0:
        return args[0] #if there aren't any arguments return args
    
    while not isinstance(args[0][0][0], str) or len(args[0]) == 0:
        args = args[0] #while the arguments are a list of lists remove outer list

    def merge_more_ledgers(args):
        if len(args) == 2: #if there are only 2 args left, return the merge of each
            return merge_two_ledgers(args[0], args[1])
        elif len(args) == 1: #if there is only a single argument (ledger) return that
            return args[0]
        else: #pop the last two arguments in args, add the merged arg1 and arg2 to the args (repeat until you only have 2 arguments left)
            arg1 = args.pop() 
            arg2 = args.pop()

            args.append(merge_two_ledgers(arg1, arg2))
            return merge_more_ledgers(args)
    return merge_more_ledgers(args)
