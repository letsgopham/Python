# 못 고르겠을 때 랜덤으로 골라주는 모듈
import random

def random_choice(restaurant_list):
    if not restaurant_list:
        print("추천할 음식점이 없습니다.")
        return
    choice = input('랜덤 추천을 해드릴까요? (예/아니오): ')
    print()
    if choice == "예":
        selected = random.choice(restaurant_list)
        name = selected.get('Place Name')
        category = selected.get('Category')
        address = selected.get('Address')
        distance = selected.get('Distance')
        phone = selected.get('Phone')
        print(f'오늘의 추천 음식점은 ***{name}*** 입니다!')
        print(f'{name} - {category}')
        print(address)
        print(distance)
        print(phone)