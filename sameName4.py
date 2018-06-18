def spam():
    global eggs
    print(eggs) #error!
    eggs = 'spam local'

eggs = 'global'
spam()
