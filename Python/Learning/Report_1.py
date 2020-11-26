for weeks in range(1,51):                                                                       #1부터 50까지 반복하며 이 값을 weeks에 할당
    with open("{}주차.txt".format(weeks), "w", encoding="utf8") as report:                      #with 문을 사용해서 파일 오픈
        report.write(" - {}주차 주간 보고 -\n부서 : \n이름 : \n업무 요약 : \n".format(weeks))   #파일에 형식에 맞춰 값 입력

for a in range(1,51):                                                                           #1부터 50까지 반복하며 이 값을 weeks에 할당
    with open("{}주차.txt".format(a), "r", encoding="utf8") as report:                          #이전에 생성한 파일을 열기위해 r 모드로 오픈
            print(report.read())                                                                #각각의 파일 내용 출력
