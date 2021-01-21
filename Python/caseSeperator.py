#!/usr/bin/python

"""
Launched Date : 2021-1-21
Program Version : 1.0

SQL Injection 시 종종 대문자와 소문자 두 번의 중복된 결과가 출력되어 이를 분리하기 위해 개발

ASCII Code가 대문자가 소문자보다 작기 때문에 대문자가 먼저 검출되는 특징을 이용하여 짝수 번째 글자가 대문자, 홀수 번째 글자를 소문자로 분리

대/소문자를 비교하는 것이 아닌 초기 버전이므로 대소문자 순서가 혼합된 경우에는 사용 지양
"""

class caseSeperator:

    def __init__(self, inStr):
        self.string = list(inStr)
        self.length = len(self.string)

    def seperate(self):
        self.upper = ""
        self.lower = ""

        for index in range(self.length):
            if index % 2 == 0:
                self.upper += "".join(self.string[index])
            elif index % 2 != 0:
                self.lower += "".join(self.string[index])
            else:
                print("Invalid Value Error")
        return self.upper, self.lower

inStr = input("Enter for Seprate according to case : ")

cs = caseSeperator(inStr)
upper, lower = cs.seperate()

print("Upper case : {}\nLower case : {}".format(upper, lower))