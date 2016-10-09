"""
Problem:    418. Sentence Screen Fitting
            https://leetcode.com/contest/8/problems/pacific-atlantic-water-flow/
Language:   Python 2
Result:     Accepted
"""

class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        # Assume each line starts with a space
        # i.e. "a-bcd-" will be "-a-bcd- "
        # and each word starts with a space
        # i.e. ["-a", "-bcd", "-e"]

        wordLens = [len(word) + 1 for word in sentence]
        sentenceLen = sum(wordLens)
        lineLen = cols + 1

        # Try to find how many sentences can be printed in how many lines.
        # Halt when reaching a cycle (n sentences just fit m lines)
        #   or reaching the end of the screen
        lineIdx = 1  # 1-based
        sentenceCount = 0
        unfilledSpaces = lineLen  # spaces not yet filled in this line
        linesToSentences = dict()  # how many sentences can be printed in lines
        linesToSentences[0] = 0
        while True:
            # try to fill a line with sentences
            if unfilledSpaces > sentenceLen:  # not necessary
                sentenceCount += unfilledSpaces / sentenceLen
                unfilledSpaces = unfilledSpaces % sentenceLen

            # if reaching a cycle (n sentences just fit m lines)
            if wordLens[0] > unfilledSpaces:
                linesToSentences[lineIdx] = sentenceCount
                break

            # try to fill line(s) with words in a sentence
            for wordLen in wordLens:
                if wordLen <= unfilledSpaces:
                    unfilledSpaces -= wordLen
                else:
                    linesToSentences[lineIdx] = sentenceCount
                    lineIdx += 1
                    unfilledSpaces = lineLen

                    # if reach the end of the screen
                    if lineIdx > rows:
                        return sentenceCount

                    if wordLen <= unfilledSpaces:
                        unfilledSpaces -= wordLen
                    else:  # if a word is longer than a line
                        return 0

            sentenceCount += 1

            # if reaching a cycle (n sentences just fit m lines)
            if wordLens[0] > unfilledSpaces:
                linesToSentences[lineIdx] = sentenceCount
                break

        return (rows / lineIdx) * sentenceCount + linesToSentences[rows % lineIdx]
