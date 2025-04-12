def func():
    a=10
    print('func()에서 a값 %d' %a)

def func2():
    print('func2()에서 a값 %d' %a)


a=20

func()
func2()

#===============================================

def func():
    global a
    a=10
    print('func()에서 a값 %d' %a)

def func2():
    print('func2()에서 a값 %d' %a)


func()
func2()