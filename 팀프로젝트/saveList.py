#리스트에 저장하는 모듈
def save(Input):
    outFp = None
    inStr = ""
    save_list = []

    outFp = open("/Users/junseo/Desktop/plz-plz-plz/plz-plz-plz-1/팀프로젝트/저장리스트.txt", "a")
    inFp = open("/Users/junseo/Desktop/plz-plz-plz/plz-plz-plz-1/팀프로젝트/저장리스트.txt", "r")

    while True:
        inStr = inFp.readline()
        if inStr == "":
            break
        save_list.append(inStr)

    name = Input + "\n"

    if name in save_list:
        print('\033[36m이미 저장되어있습니다.\033[0m')
        print()
    else:
        outFp.writelines(f'{Input}\n')
        print("---\033[92m정상적으로 저장되었습니다!\033[0m---")
        print()

    outFp.close()
    return