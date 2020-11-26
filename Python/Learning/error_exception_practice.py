chicken = 10
waiting = 1

class SoldOutError(Exception):
    def __init__(self, chicken):
        self.chicken = chicken
        print("재고가 소진되어 더 이상 주문을 받지 못합니다.\n주문 가능하신 수량은 {}개 남았습니다.".format(self.chicken))
    
while(True):
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까? "))
        if order < 1:
            raise ValueError
        
        if order > chicken:
            raise SoldOutError(chicken)
        else:
            print("[대기번호 {0}] {1}마리 주문이 완료되었습니다.".format(waiting, order))
            waiting += 1
            chicken -= order
            
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError:
        pass

    finally:
        print("이용해 주셔서 감사합니다.")
