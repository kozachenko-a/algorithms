def BinarySearch(pArr, pSearchItem, pStepNumber):
    '''
    Recursive function BinarySearch - find item in array pArr using BinarySearch algorithm

    Agruments
    pArr  input Array
    pSearchItem   search item
    pStepNumber   number of search iteration
    '''
    if len(pArr) == 1:
        if pArr[0] == pSearchItem:
            return True, pStepNumber
        else:
            return False, pStepNumber
    else:
        vMediumElement = len(pArr)//2
        if pArr[vMediumElement] > pSearchItem:
            return BinarySearch(pArr[:vMediumElement], pSearchItem, pStepNumber+1)
        elif pArr[vMediumElement] < pSearchItem:
            return BinarySearch(pArr[vMediumElement:], pSearchItem, pStepNumber+1)
        elif pArr[vMediumElement] == pSearchItem:
            return True, pStepNumber

def BinarySearchWhile(pArr, pSearchItem):
    '''
    function BinarySearch using While cycle

    Agruments
    pArr  input Array
    pSearchItem   search item
    '''
    low = 0
    high = len(pArr)-1
    while low <= high:
        mid = (low+high) // 2
        guess = pArr[mid]
        if guess == pSearchItem:
            return True
        if guess > pSearchItem:
            high = mid -1
        else:
            low = mid + 1
    return False

# test case
pArr = [2,3,6,11,25,34,45,90,34,22,19,45]
# tesh using while cycle
if BinarySearchWhile(sorted(pArr), 25):
    print ('Item found!')

# test using recursive function
(vFound, pStepNumber) = BinarySearch(sorted(pArr), 25, 1)
# return FoundFlag and number of iterations
if vFound:
    print ('Item found! Number of Iterations = ' + str(pStepNumber))
else:
    print ('Item not found!')

