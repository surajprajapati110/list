ans='y'
slist=[]
while ans=='Y':
    print('1. add name')
    print('2. display name')
    print('3. search name')
    print('4. modify name')
    print('5. delete name')
    print('6. exit')
    print('enter your choice 1,2,3,4,5,6')
    choice=int(input())
    if choice==1:
        name=input('enter name')
        slist.append(name)
        print('record saved')
    if choice==2:
            for x in slist:
                print(x)
    elif choice==3:
            sname=input('enter name search')
    if sname in select:
            print('name found')
    else:
            print('not found')
    elif choice==4:
            sname=input('enter old name')
            oname=input('enter new name')
    if oname in slist:
            i=slist index (oname)
            slist[i]=nname:
                print('saved record')
    else:
            print ('record not found')
    elif choice==5:
            dname=input('enter name to delete')
    if dname in slist:
            slist.remove (dname)
            print ('record delete')
    else:
            print ('not found')
            else:
                exit(0)
                print('countinue y/n')
        ans=input()
