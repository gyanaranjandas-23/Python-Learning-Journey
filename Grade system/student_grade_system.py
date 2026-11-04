sub1 = int(input("Enter subject1 marks: "))
sub2 = int(input("Enter subject2 marks: "))
sub3 = int(input("Enter subject3 marks: "))
sub4 = int(input("Enter subject4 marks: "))
sub5 = int(input("Enter subject5 marks: "))
marks = [sub1,sub2,sub3,sub4,sub5]
Totalmarks = sub1+sub2+sub3+sub4+sub5
print(Totalmarks)

Averagemark = Totalmarks/5
print(Averagemark)


percentage = Totalmarks/5*100
print(percentage)

if (marks >= 90) and (marks <= 100):
    print("Grade A")

    if marks> 100:
        print("something went wrong in your mark")
    else:
        print("Grade A")

elif ( marks >= 80) and (marks <= 89):
    print("Grade B")

elif (marks >= 70) and (marks <= 79):
    print("Grade C")

elif (marks >= 60) and (marks <= 69):
    print("Grade D")

else:
    print("FAIL/ Improve your result")


