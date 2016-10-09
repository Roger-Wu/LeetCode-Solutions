class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        signStr = ""
        if numerator * denominator < 0:
            signStr = "-"

        numerator = abs(numerator)
        denominator = abs(denominator)

        intPart = numerator / denominator
        remainder = numerator % denominator

        if remainder == 0:
            return signStr + str(intPart)

        fracStr = ""
        # appearedRemainderSet = set([remainder])
        appearedRemainder = [remainder]
        while True:
            fracStr += str((remainder * 10) / denominator)
            newRemainder = (remainder * 10) % denominator
            if newRemainder == 0:
                break
            start = safeIndex(appearedRemainder, newRemainder)
            if start != -1:
                fracStr = fracStr[:start] + '(' + fracStr[start:] + ')'
                break
            # appearedRemainderSet.add(newRemainder)
            appearedRemainder.append(newRemainder)
            remainder = newRemainder
        return signStr + str(intPart) + '.' + fracStr

def safeIndex(l, item):
    try:
        return l.index(item)
    except:
        return -1
