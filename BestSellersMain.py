def booklist():
    bestsellers = open('bestsellers.txt','r')
    collection = []
    c = 0
    for line in bestsellers:
        c += 1
        line = line.strip('\n')
        collection.append(line.split('\t'))
    print('Read', c, 'books')
    bestsellers.close()
    return collection
    
def search_years(l):
     hasBook = False
     lYear = int(input("Enter start year: "))
     uYear = int(input("Enter end year: "))
     for newLine in l:                           
         check = newLine[3]
         if check[-1] == " ":
             checkY = check[-5:-1]
         else:
             checkY = check[-4:]
         checkYInt = int(checkY)
         if (checkYInt >= lYear) and (checkYInt <= uYear):
             print(newLine[0],'by:', newLine[1],'(pub date: ',newLine[3],')')
             hasBook = True
     if not hasBook:
         print("There are no books in the collection within this range.\n")

def month_year(l):
    month = int(input('Enter a month (1-12): '))
    if (month>12) or (month<1):
        print('Try again')
        month = int(input('Enter a month (1-12): '))
    year = int(input('Enter year: '))
    for newline in l:
        check = newline[3]
        checkM=''
        slash = False
        counter = 0
        while not slash:
            if check[counter] != '/' and check[counter] != ' ':
                checkM+=check[counter]
                counter+= 1
            elif check[counter]==' ':
                slash= False
                counter+=1
            else:
                slash= True
        checkMint= int(checkM)
        if check[-1] == ' ':
            checkY= check[-5:-1]
        else:
            checkY= check[-4:]
        checkYint= int(checkY)
        if (checkMint == month) and (checkYint == year):
            print(newline[0],'by:', newline[1],'(pub date: ',newline[3], ')')
        

def author_search(l):
    author_name = input('Enter search string: ')
    for a in l:
        if author_name.lower() in a[1].lower():
            print(a[0], 'by:', a[1],'(pub date:',a[3],')')
        
def title_search(l):
    title_name = input('Enter search string: ')
    for x in l:
        if title_name.lower() in x[0].lower():
            print(x[0], 'by:', x[1],'(pub date:',x[3],')')

def main():
    books = booklist()
    go = True
    while go == True:
        print('What would you like to do?')
        print('1: Look up year range')
        print('2: Look up month/year')
        print('3: Search for author')
        print('4: Search for title')
        print('Q: Quit')
        choices = input('> ')

        if choices == '1':
            search_years(books)

        elif choices == '2':
            month_year(books)

        elif choices == '3':
            author_search(books)

        elif choices == '4': 
            title_search(books)

        if choices == 'q' or choices == 'Q':
            go= False
            print('Done')

        else:
            print("I dont't understand this command")

    
if __name__ == '__main__':
    main()
            











        
        
