n =  int(input())


if n % 100 == 0 :
    print("-1")
elif n%10==0:
    print("-1")

check = 0



def checkdigit(N,n):

    last_digit = N % 10 
    digit2  = N // 10

    middle_digit= n//10%10
    first_digit = n//100

    if ((first_digit != last_digit) and (middle_digit!=first_digit) and (middle_digit!=last_digit)):
        
        while (N != 0) :
 
        
            current_digit = digit2 % 10;
        
        
            N = N // 10;
 
    
            if (current_digit == last_digit) :
                return "No";
        return "Yes"
    
        
 
    
    return "No";



for i in range(2,100):
    check = n * i 
    if checkdigit(check,check)=="Yes":
        print(check)
        check == 0
        break;
    else:
        check==0




