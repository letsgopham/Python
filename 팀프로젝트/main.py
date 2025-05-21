# 메인 프로그램

from kakaoAPI import api
from filter import filter_restaurant
from dataFrame import restaurant_DataFrame
from randomChoice import random_choice


def main():
    y = input('위도: ')
    x = input('경도: ')
    radius = int(input('반경(m): '))
    selected_category = input("원하는 음식점 종류 (예: 한식 중식 일식): ")

    places = api(x, y, radius)
    filtered_restaurant = filter_restaurant(places, selected_category)
    restaurant_DataFrame(filtered_restaurant)
    print()
    random_choice(filtered_restaurant)

print("상명대 정문 위도 / 경도: 37.6025 / 126.9553")

main()