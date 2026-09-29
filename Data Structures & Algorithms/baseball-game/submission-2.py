class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []

        for oper in operations:
            if  oper == "+":
                scores.append(scores[-1] + scores[-2])
            elif oper == "D":
                scores.append(scores[-1] * 2);
            elif oper == "C":
                scores.pop()
            else:
                scores.append(int(oper))
        return sum(scores)
        