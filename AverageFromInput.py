def main():
    counter=0
    total=0
    try:
        avgFile= open('numbers.txt','r')
        for num in avgFile:
            try:
                n=float(num)
            except ValueError:
                num=num.strip('\n')
                print('One of your numbers is not an int or float')
            else:
                total+=n
                counter= counter+1
                print('I read in ', counter, 'number(s) Current number is: ', f'{n:>8.2f}','Total is: ', f'{total:>8.2f}')
        avg= total/counter
        print('Average:', avg)
        avgFile.close()
    except IOError:
        print('File not found')
if __name__ == '__main__':
    main()
     
        
