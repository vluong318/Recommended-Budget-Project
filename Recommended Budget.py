recommendation_budget = 0

def main():
    print()
    print('Basic Recommended Budget From Chime.com' ) 

    budget_program = 'Recommendation Budget'
    your_budget = recommendation_budget
    while budget_program == 'Recommendation Budget':
        print()
        print('YOUR RECOMMENDED BUDGET CATEGORY PERCENTAGES!')        
        print('Housing is 25%:\n $', format(round(your_budget *.25,2), '.2f'))
        print('Insurance is 15%:\n $', format(round(your_budget *.15,2), '.2f'))
        print('Food is 10%:\n $', format(round(your_budget *.10,2), '.2f'))
        print('Transportion is 5%:\n $', format(round(your_budget *.05,2), '.2f'))
        print('Utilities is 5%:\n $', format(round(your_budget *.05,2), '.2f'))
        print('Savings is 15%:\n $', format(round(your_budget *.15,2), '.2f'))
        print('Entertainment is 10%:\n $', format(round(your_budget *.10,2), '.2f'))
        print('Giving is 10%:\n $', format(round(your_budget *.10,2), '.2f'))
        print('Personal is 5%:\n $', format(round(your_budget *.05,2), '.2f'))
        print()
        print('Menu:')
        print('1 to Add your income: ')
        print('Q to Quit')
        choice = input('Select 1 or Q: ')
        if choice == '1':
            your_budget = addincome(your_budget)
        elif choice == 'q':
            print('Goodbye!')
            break
        elif choice == 'Q':
            print('Thank You!')
            break
        else:
            print('Invalid selection, please select 1 or Q')

def addincome(your_budget):
    income = float(input('Enter income: $'))
    your_budget = income
    if your_budget >= 1:
        return your_budget
    else:
        print('Please enter amount over $1')
        return addincome(your_budget)

main()