def main():
    counter=0
    total=0
    avgFile= open('numbers.txt','r')
    for num in avgFile:
        n=float(num)
        total+=n
        counter= counter+1
        print('I read in ', counter, 'number(s) Current number is: ', f'{n:>8.2f}','Total is: ', f'{total:>8.2f}')
    avg= total/counter
    print('Average:', avg)
    avgFile.close()
main()
    
        
