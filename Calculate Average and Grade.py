#Chalen Bobish
#CS-175L
#Average and grade

def determine_grade(test_score):
    if test_score >= 90 and test_score <= 100:
        letter_grade = 'A'
    elif test_score >= 80:
        letter_grade = 'B'
    elif test_score >= 70:
        letter_grade = 'C'
    elif test_score >= 60:
        letter_grade = 'D'
    elif test_score < 60:
        letter_grade = 'F'
    return letter_grade


def input_scores():
    print('Enter 5 test scores')
    score1 = float(input('Enter score 1: '))
    score2 = float(input('Enter score 2: '))
    score3 = float(input('Enter score 3: '))
    score4 = float(input('Enter score 4: '))
    score5 = float(input('Enter score 5: '))

    letter_score1 = determine_grade(score1)
    letter_score2 = determine_grade(score2)
    letter_score3 = determine_grade(score3)
    letter_score4 = determine_grade(score4)
    letter_score5 = determine_grade(score5)

    print('Score', f'{"Numeric Grade":>25}', f'{"Letter Grade":>20}')
    print('------------------------------------------------------------')
    print('Score 1: ',f'{score1:>15}',f'{letter_score1:>21}')
    print('Score 2: ',f'{score2:>15}',f'{letter_score2:>21}')
    print('Score 3: ',f'{score3:>15}',f'{letter_score3:>21}')
    print('Score 4: ',f'{score4:>15}',f'{letter_score4:>21}')
    print('Score 5: ',f'{score5:>15}',f'{letter_score5:>21}')
    
    return score1, score2, score3, score4, score5

    
def calc_average(test1, test2, test3, test4, test5):
    average = (test1 + test2 + test3+ test4 + test5)/5
    return average


def repeat():
    ask_repeat = input('Enter "yes" if you would like to do another calculation: ')
    if ask_repeat == 'yes':
        main()

def main():
    test1,test2,test3,test4,test5=input_scores()
    avg = calc_average(test1, test2, test3, test4, test5)
    avg_letter = determine_grade(avg)
    print('Average score: ',f'{avg:>9.1f}',f'{avg_letter:>21}')
    repeat()
main()
    









