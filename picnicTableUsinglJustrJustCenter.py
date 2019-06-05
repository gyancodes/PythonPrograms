def printPicnicItem(picnicitem,leftWidth,rightWidth):
    print('PICNIC ITEMS'.center(leftWidth+rightWidth,'-'))
    for k,v in picnicitem.items():
        print(k.ljust(leftWidth,'.')+str(v).rjust(rightWidth))





picnicItem={'sandwich':'4','apples':'12','cups':'5','cookies':'8000'}
printPicnicItem(picnicItem,12,5)
printPicnicItem(picnicItem,20,6)