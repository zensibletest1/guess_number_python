import random
# timer=10
# while timer>=1:
#     print(random.randint(1,10)) #both inclusive
#     timer-=1
def guess_number():
    target_number=random.randint(1,10)
    user_guess=''
    total_guess=0
    while user_guess!=target_number:
        try:
            user_guess=int(input('Please enter your guess: '))
            total_guess+=1
            if user_guess<target_number:
                print('Too Low')
            elif user_guess>target_number:
                print('Too High')  
        except ValueError as e:
            print(f'The input is invalid {e}')        
    print(f'Congrats! You guessed it all! It took you {total_guess} guesses') 
    ans=input('Do you want to play again? (Y/N)')
    if ans.lower()=='y':
        guess_number()
    elif ans.lower()=='n':
        return    
            
# print('1'==1)   
if __name__=='__main__':
    guess_number()

 