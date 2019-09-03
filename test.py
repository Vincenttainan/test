score=0
print('Do your best')
def check_guess(guess,answer):
    global score
    fail=0
    still_guessing='Ture'
    while still_guessing and fail<3:
        if guess==answer:
            print('Correct')
            score=score+30
            still_guessing='Flase'
            fail=4
        else:
            if fail<2:
                guess=input('Uncorrect,try again')
                score=score-10
                fail=fail+1
            else:
                print('Answer is '+ answer)
                fail=0
guess1=input('1+1=?')
check_guess(guess1,'2')
guess2=input('2+2=?')
check_guess(guess2,'4')
guess3=input('(4/2)+98=?')
check_guess(guess3,'100')
guess4=input('(4+40/40)+95=?')
check_guess(guess4,'100')
print('your score is '+str(score))
