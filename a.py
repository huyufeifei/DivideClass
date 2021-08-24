import random,time,os


# peonum=80
# stulist=[]
manlist=['夏新雨','袁浩涵','冯磊','张越','赵晗','李泓阳','周宏梓',
'徐天浩','刘天烨','冯然','关函宇','赵鹏舜','赵泽东','王贤俊','宋睿霖',
'牟思宇','李俊籴','吴家鑫','王宝吉','田伟琪','韩昊阳','姚歌','朱铭瀚','姚远','梁明宇',
'罗英杰','耿汉炜','董海航','李思泽','姜禹铭','邬博丰','王学澍','李有彬','柴嘉','陈俊豪','朱梓赫',
'栗彬','齐冠程','陈继元','莫子萱','张荣宸','殷明宇','崔勇俊']
girllist=['李悦','杨雨晴','高春蕊','唐菲','徐睿','姜若琳','王思诺',
'王敬儒','王婧伦','鲍越洋','孙雅倪','史佳琪','胡伊诺','于博谦','陈雯佳','张姝涵',
'张敏','鲍奕欧','张雨馨','刘桐鑫','吕雨涵','王佳艺','钱禹霏','曹紫依','赵雨珊'
]

class1=[]
class2=[]

print("""
--------------------------------------------------------------------
|            智能分班系统©（齐市一中初中部限定版） ALPHA1.0    
|                     Author：huyufeifei                    
|             本程序仅供齐齐哈尔市第一中学初中部使用            
|         如需定制其它程序请联络medunovdorofei1991@gmail.com       
|                                                       
|                        使用说明：
|       本程序通过基于Python的随机数生成函数进行阳光分班操作
|               可保证分班结果无任何人工因素介入
|      源代码查询：https://github.com/huyufeifei/DivideClass
|--------------------------------------------------------------------
""")

while True:
    userchoice = int(input("欢迎使用，请按照提示输入相应数字：\n格式化系统请输入0,分班输入1，保存并退出请输入2:\n"))
    # stulist = []
    class1 = []
    class2 = []
    if userchoice==0:
        if os.path.exists("分班信息.txt"):
            os.remove("分班信息.txt")
        print("清理完成，可以开始正式使用↓↓↓\n")
        continue
    elif userchoice == 2:
        print("感谢使用，软件版权©huyufeifei")
        time.sleep(2)
        break

    slow = 0
    while True:
        slow=0
        slow_choice = input("缓出模式请输入s，性能模式请输入e (均为小写)：")
        if slow_choice== 's':
            slow=1
            break
        elif slow_choice == 'e':
            slow=0
            break
        else:
            print("您的输入有误，请重新输入.")

    file = open("分班信息.txt", "w+")
    
    random.shuffle(manlist)
    random.shuffle(girllist)
    
    for i in range(0, len(girllist)):
        stu = girllist[i]
        class1.append(stu) if (i%2)==0 else class2.append(stu)
    for i in range(0, len(manlist)):
        stu = manlist[i]
        class1.append(stu) if (i%2)==1 else class2.append(stu)

    print("\n\n分组A人员名单:")
    file.write("分组A人员名单:\n")
    
    random.shuffle(class1)
    random.shuffle(class2)

    for i in range(0, len(class1)) :
        Str = ''
        if i<9:
            Str = str(i+1) + '  : ' + class1[i]
        else :
            Str = str(i+1) +  ' : ' + class1[i]
        if slow == 1:
            time.sleep(0.5)
        print(Str)
        file.write(Str+'\n')

    print("\n\n分组B人员名单:")
    file.write("\n\n分组B人员名单:\n")
    
    for i in range(0, len(class2)) :
        Str = ''
        if i<9:
            Str = str(i+1) + '  : ' + class2[i]
        else :
            Str = str(i+1) +  ' : ' + class2[i]
        if slow == 1:
            time.sleep(0.5)
        print(Str)
        file.write(Str+'\n')

    file.close()
    print("\n\n分班信息已存储至与此exe同一目录下\n\n")
