import requests
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 150)

def api(x, y, radius):
    url = "https://dapi.kakao.com/v2/local/search/category.json"
    search_info = {
        "category_group_code": "FD6",
        "x": str(x), 
        "y": str(y),
        "radius": radius,
        "sort": "distance"
    }

    head = {
        "Authorization": "KakaoAK 1a251a6ce8afd58ca6fd538cfefab12b"
    }

    res = requests.get(url, params=search_info, headers=head)

    if res.status_code == 200:
        return res.json()["documents"]
    
    else:
        print("API 요청 실패:", res.status_code)
        print("응답 내용:", res.text)

def restaurants(places):
    restaurant_list = []

    for restaurant in places:
        restaurant_dict = {
            "Place Name": restaurant.get("place_name", 'N/A'),
            "Address": restaurant.get("address_name", "N/A"),
            "Distance": restaurant.get("distance", "N/A") + "m",
            "Phone": restaurant.get("phone", "N/A")
        }
        restaurant_list.append(restaurant_dict)
    return restaurant_list
    
def restaurant_df(restaurant_list):
    df = pd.DataFrame(restaurant_list)
    print(df.to_string(index=False))

def main():
    y = input('위도: ')
    x = input('경도: ')
    radius = int(input('반경(m): '))

    places = api(x, y, radius)
    restaurant_list = restaurants(places)
    restaurant_df(restaurant_list)

print("""상명대 정문 위도 / 경도: 37.6025 / 126.9553

홍제행복기숙사 위도 / 경도: 37.5860 / 126.9553

우리집 위도 / 경도: 37.1592 / 127.0811

홍제역 4번출구 위도 / 경도: 37.5892 / 126.9433""")

main()