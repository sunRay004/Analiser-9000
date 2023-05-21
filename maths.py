import statistics

statistics.stdev([1, 3, 5, 7, 9, 11])
statistics.mean
statistics.median
statistics.linear_regression
statistics.geometric_mean

def extractNum(expArray):
    reitem = []
    for item in expArray:
        reitem.append(item[1])
    return reitem

def SD(expArray):
    return statistics.stdev(extractNum(expArray))
def mean(expArray):
    return statistics.mean(extractNum(expArray))
def median(expArray):
    return statistics.median(extractNum(expArray))
def mode(expArray):
    return statistics.mode(extractNum(expArray))
def gmean(expArray):
    return statistics.geometric_mean(extractNum(expArray))