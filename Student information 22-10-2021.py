stud = []
ch = 'y'
c = 'y'

while c == 'y' :
    print("-----------------------------------------")
    print("Enter the choice give below : ")
    print("1. Add Record ")
    print("2. Search  Record")
    print("3. Update Record ")
    print("4. Delete Record")
    print("5. Display Record ")
    print("------------------------------------------")

    choice = int(input("Enter the choice : "))
    if choice == 1 :
        while ch == 'y' :
            print("-------------------------------------")
            r = int(input("Enter the Roll number     : "))
            n = input("Enter the Name            : ")
            p = input("Enter the Percentage      : ")
            print("-------------------------------------")
            ch  = input("do you want to add more records 'y' / YES 'n' / NO : ")
            stud_data = [r ,n ,p]
            stud.append(stud_data)
    elif choice == 2 :
        flag = 0
        roll = int(input("Enter the Roll number to be searched : "))
        for i in range (len(stud)) :
            if stud[i][0]==roll :
                print("Roll number : ", stud[i][0])
                print("Name : ", stud[i][1])
                print("Percentage : ", stud[i][2])
                print("-------------------------------------")
                flag = 1
        if flag == 0 :
            print("Not Found !")
            
    elif choice == 5 :
        a = input("Select the choice  1. All Records 2. Individual Records : ")
        if a == 1 :
            for i in range (len(stud)) :            
                print("-------------------------------------")
                print("Roll number : ", stud[i][0])
                print("Name : ", stud[i][1])
                print("Percentage : ", stud[i][2])
                print("-------------------------------------")
                
#         else :
#             flag = 0
#             roll = int(input("Enter the Roll number to be searched : "))
#             for i in range (len(stud)) :
#                 if stud[i][0]==roll :
#                     print("Roll number : ", stud[i][0])
#                     print("Name : ", stud[i][1])
#                     print("Percentage : ", stud[i][2])
#                     print("-------------------------------------")
#                     flag = 1
#             if flag == 0 :
#                 print("Not Found !")
                
    











    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    