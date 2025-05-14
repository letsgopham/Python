# API서버에서 받은 값들을 정리해주는 모듈

def rest(places, wantedCategory):
    rest_list = []

    for place in places:
        category = place.get("category_name", "N/A")
        if wantedCategory in category:
            rest_dict = {
                "Place Name": place.get("place_name", 'N/A'),
                "Address": place.get("address_name", "N/A"),
                "Distance": place.get("distance", "N/A") + "m",
                "Category": place.get("category_name", "N/A"),
                "Phone": place.get("phone", "N/A")
            }
            rest_list.append(rest_dict)
        
    if not rest_list:
        print("입력하신 카테고리가 검색되지 않았습니다. 가까운 순으로 다른 음식점을 추천합니다.")
        for place in places:
            rest_dict = {
                "Place Name": place.get("place_name", 'N/A'),
                "Address": place.get("address_name", "N/A"),
                "Distance": place.get("distance", "N/A") + "m",
                "Category": place.get("category_name", "N/A"),
                "Phone": place.get("phone", "N/A")
            }
            rest_list.append(rest_dict)

    
    return rest_list