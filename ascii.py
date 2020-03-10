## built-in
##chr(65) 'A'
##chr(66) 'B'
##chr(90) 'Z'

##Return
##
##answer={chr(65):'A',...}


##answer={}
##for char in range(chr(65),chr(90)):
##    answer=dict(char)


##char=chr(65)
##answer={}
##
##while char<chr(90):
##    char+=1
##    answer=dict(char)
##    
##for ascii in range(65,91):
##    answer={ascii:chr(ascii)}
##    print(answer)

answer={ascii:chr(ascii) for ascii in range(65,91)}

        
    

            
