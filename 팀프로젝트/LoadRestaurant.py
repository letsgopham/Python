def load_restaurant():
    inStr = ""
    save_list = []
    inFp = open("/Users/junseo/Desktop/Python/팀프로젝트/저장리스트.txt", "r")
    
    while True:
        inStr = inFp.readline()
        if inStr == "":
            break
        save_list.append(inStr)
        
    print('저장된 음식점: ')
    for i in save_list:
        print(f'\033[93m\033[1m{i}\033[0m')