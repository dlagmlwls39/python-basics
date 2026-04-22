def read(text):
    textlist = text.split(':')
    ridename = textlist[0].strip()
    height = textlist[1].strip()
    
    cmmin = cmmax = None

    if '~' in height:
        height = height.split('~')
        cmmin = height[0].replace('cm', '').strip()
        cmmax = height[1].replace('cm', '').strip()    
    else:
        if '이상' in height:
            cmmin = height.split('cm')[0].strip()
        elif '이하' in height:
            cmmax = height.split('cm')[0].strip()
        
    return ridename, cmmin, cmmax

if __name__ == "__main__":
    ridename, cmmin, cmmax = read(input())
    print("이름:", ridename)
    print("하한:", cmmin)
    print("상한:", cmmax)
