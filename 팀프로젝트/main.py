# 메인 프로그램
from kakaoAPI import api
from filter import filter_restaurant
from dataFrame import restaurant_DataFrame
from randomChoice import random_choice
import geocoder

geo = geocoder.ip('me')

def main():
    y = 37.6025 #geo.lat
    x = 126.9553 #geo.lng
    radius = 500 #int(input('반경(m): '))
    selected_category = input("원하는 음식점 종류 (예: 한식 중식 일식): ")
    places = api(x, y, radius)
    random_list = []

    if not selected_category:
        filtered_list = filter_restaurant(places, "")
        restaurant_DataFrame(filtered_list)            
        random_list.append(filtered_list)

    else:
        selected = selected_category.split()
        for i in selected:
            filtered_list = filter_restaurant(places, i)
            message = f'\033[35m\033[1m{i}\033[0m'
            print('{0:=^150}'.format(message))
            restaurant_DataFrame(filtered_list)            
            random_list.append(filtered_list)
            print()

    print()
    random_choice(random_list)

main()