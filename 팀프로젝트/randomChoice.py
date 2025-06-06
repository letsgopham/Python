# 못 고르겠을 때 랜덤으로 골라주는 + 음식점 저장해주는 모듈
import random
import sys
from saveList import save

response = '예', 'dP', 'yes', 'Yes', '네', 'sp', '응', 'dmd'

def random_choice(random_list):
    if not random_list:
        print("추천할 음식점이 없습니다.")
        return
        
    
    choice = input('랜덤 추천을 해드릴까요? (예/아니오): ')
    print()
    
    def Choice():
        if choice in response:
            selected = random.choice(random_list)
            selected2 = random.choice(selected)
            name = selected2.get('Place Name')
            category = selected2.get('Category')
            address = selected2.get('Address')
            distance = selected2.get('Distance')
            phone = selected2.get('Phone')
            Kakao_URL = selected2.get('Kakao Map URL')
            print(f'오늘의 추천은 ***\033[93m\033[1m{name}\033[0m*** 입니다!')
            print(f'종류: \033[35m{category}\033[0m')
            print(f'주소: {address}')
            print(f'거리: {distance}')
            print(f'번호: {phone}')
            print(f'카카오맵 바로 가기: {Kakao_URL}')
            
            try:
                Save = input('이 집을 리스트에 저장 하시겠습니까?: ')
                if Save in response:
                    save(name)
            except:
                pass
                
        else:
            sys.exit('\033[34m\033[1m추첨을 종료합니다.\033[0m')

        try:
            retry = input('다시 추첨할까요?: ')
            if retry in response:
                print('{0:=^56}'.format(""))
                Choice()
            else:
                print('\033[34m\033[1m추첨을 종료합니다.\n\033[0m')
        except:
            pass
    Choice()