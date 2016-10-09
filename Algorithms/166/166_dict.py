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
        appearedRemainder = dict()
        fracIndex = 0
        while True:
            appearedRemainder[remainder] = fracIndex
            fracStr += str((remainder * 10) / denominator)
            newRemainder = (remainder * 10) % denominator
            if newRemainder == 0:
                break
            start = appearedRemainder.get(newRemainder)
            if start is not None:
                fracStr = fracStr[:start] + '(' + fracStr[start:] + ')'
                break
            remainder = newRemainder
            fracIndex += 1
        return signStr + str(intPart) + '.' + fracStr
