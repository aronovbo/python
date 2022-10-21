#-*- coding: utf-8 -*
import robot
r = robot.rmap()
r.lm('task8-17')
def task():
    pass
    #------- пишите код здесь -----
   
    if r.wallDown() and r.freeUp() and r.freeRight():
        x = 0
        while r.freeUp():
            r.up()
            x += 1
            y = x
        while r.freeDown():
            r.down()
            x -= 1
        if y == 2:
            r.paint()
    

    while r.freeRight():
        r.right()
        
        if r.wallDown() and r.freeUp() and r.freeRight():
            x = 0
            while r.freeUp():
                r.up()
                x += 1
                y = x
            while r.freeDown():
                r.down()
                x -= 1
            if y == 2:
                r.paint()
                
            
                
                    
                
            
            
        
            
        
        
        
            
       
            
        


       
    #------- пишите код здесь -----
r.start(task)
#Отступ слева (tab) сохранять!
#r.help() - Список команд и краткие примеры
#r.demo() - показать решение этой задачи (только результат, не текст программы)
#r.demoAll() - показать все задачи (примерно 20 минут)
#r.rt() - вправо
#r.rt(3)- вправо на 3
#r.dn() - вниз
#r.up() - вверх
#r.lt() - влево
#r.pt() - закрасить  Paint
#r.cl() - закрашена ли клетка? Color
#r.fr() - свободно ли справа? wallRight
#r.fl() - свободно ли слева?  freeLeft
#r.fu() - свободно ли сверху? freeUp
#r.fd() - свободно ли снизу?  freeDown
#r.wr() - стена ли справа? wallRight
#r.wl() - стена ли слева?  wallLeft
#r.wu() - стена ли сверху? wallUp
#r.wd() - стена ли снизу?  wallDown
#red - красный
#blue - синий
#yellow - желтый
#green - зеленый
