#Chalen Bobish
#Stocks

commRate=float(input('What was the commission rate? '))
shares=int(input('How many shares did you purchase? '))
purchase=float(input('What was the purchase price? '))
selling=float(input('What was the selling price? '))
             
amount= purchase*shares
comm_paid1= amount*commRate
sold= selling*shares
comm_paid2= sold*commRate
total_comm= comm_paid1+comm_paid2
profit_total= sold-amount-total_comm

print(f'Amount paid for stock: ${amount:,.2f}')
print(f'Commission paid on the purchase: ${comm_paid1:,.2f}')
print(f'Amount the stock sold for: ${sold:,.2f}')
print(f'Commission paid on the sale: ${comm_paid2:,.2f}')
print(f'Total commission paid: ${total_comm:,.2f}')
print(f'Profit (or loss if negative): ${profit_total:,.2f}')
      
