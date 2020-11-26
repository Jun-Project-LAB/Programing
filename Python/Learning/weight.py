#계산 공식
#남 : 키(m) * 키(m) * 22
#여 : 키(m) * 키(m) * 21
import math

def std_weight(height, gender):                     #표준 체중 계산을 위한 함수
    heightm=height/100                              #cm 단위 키를 m 단위로 변경
    Var={"남자":22, "여자":21}                      #성별에 따른 값 입력을 위한 Dictionary
    weight=round((heightm**2)*Var[gender],2)        #표준 체중을 구하는 과정, 소수 둘째 자리에서 반올림
    print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다." \
          .format(height, gender, weight))  #출력 과정 & 각각의 변수값 지정

####################################################
    
height=int(input("키를 입력하십시오 "))          #키 입력
gender=input("성별을 입력하십시오 ")             #성별 입력(남자 혹은 여자)

std_weight(height, gender)                       #함수 호            
