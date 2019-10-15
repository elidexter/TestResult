def andLogical(X,Y):
    return X and Y
def orLogical(X,Y):
    return X or Y
def notLogical(X):
    return not X
def xorLogical(X,Y):
    return andLogical(notLogical(andLogical(X,Y)),orLogical(X,Y))
