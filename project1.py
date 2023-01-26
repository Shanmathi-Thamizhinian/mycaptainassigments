import csv

def infile(list):
    with open("studinfo.csv","a",newline='') as csvf:
        w=csv.writer(csvf)
        if csvf.tell()==0:
            w.writerow(["Name","Age","Contact","Email"])
        w.writerow(list)

if __name__=='__main__':
    condition=True
    sno=1
    while(condition):
        s_info=input("Please enter student #{} information(name,age,contact,email):".format(sno))
        s_list=s_info.split(' ')
        print("\nThe information of student "+str(sno)+" is: \n"
              " Name:{}\n Age:{}\n Contact:{}\n Email:{}\n".format(s_list[0],s_list[1],s_list[2],s_list[3]))
        check=input("Is the information you entered correct?(yes/no)")
        if check=='yes':
              infile(s_list)
              cond=input("Would you like to input another student information?(yes/no)")
              if cond=='yes':
                   condition=True
                   sno=sno+1
              elif cond=='no':
                   condition=False
        elif check=='no':
              print("Please re-enter the information!")
        
