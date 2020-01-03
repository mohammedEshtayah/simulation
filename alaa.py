if __name__ == "__main__":
    student_name=[]
    First_Activity_first=[]
    First_Activity_second=[]
    Theoretical_infinite=[]
    final_practical=[]
    mark=0
    # result
    print("Please enter the number of students")
    number_students=input()
    print("student's name ,First Activity first , Activity marker and second, Theoretical infinite sign ,The final practical sign")
    for i in range(int(number_students)):
        student_name.append(input().upper())
        mark=input()
        if int(mark) > 101:
            break
        First_Activity_first.append(float(mark)*0.05)
        mark=input()
        if int(mark) > 101:
            break
        First_Activity_second.append(float(mark)*0.05)
        mark=input()
        if int(mark) > 101:
            break
        Theoretical_infinite.append(float(mark)*0.30)
        mark=input()
        if int(mark) > 101:
            break
        final_practical.append(float(mark)*0.60)
    sum=0    
    for i in range(int(number_students)):
        mark=First_Activity_first[i]*First_Activity_second[i]*Theoretical_infinite[i]*final_practical[i]
        
        if float(mark) >= 70:
            result="pass"
        else:
            result="fill"
        print("-----------------------------------------------")
        print(int(i),"  ",student_name[i] ,"  ",mark,"  ",result)
        sum=sum+mark
    avg=sum/len(student_name)
    print("avg  ",avg)
   
    