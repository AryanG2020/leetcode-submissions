class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score=[]
        x=0
        for y in operations:
            if y=="+":
                score.append(score[-1]+score[-2])
            elif y=='D':
                score.append(score[-1]*2)
            elif y=='C':
                score.pop()
            else:
                score.append(int(y))
        return sum(score)

        