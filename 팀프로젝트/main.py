# 메인 프로그램

from kakaoAPI import api
from filter import rest
from dataFrame import rest_df


def main():
    y = input('위도: ')
    x = input('경도: ')
    radius = int(input('반경(m): '))
    wantedCategory = input("원하는 음식점 종류 (예: 한식 중식 일식): ")

    places = api(x, y, radius)
    rest_list = rest(places, wantedCategory)
    rest_df(rest_list)

print("상명대 정문 위도 / 경도: 37.6025 / 126.9553")

main()