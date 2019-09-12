def CalculateYearlyBalance(balance,annualIntrest):
    """
        function takes in Yearly Debt and the annual Intrest
        returns minimum monthly Pay to pay all Debt in  A Year
    """
    unPaidBalance = balance
    MonthlyRate = 0 # starts with zero

    #keeps looking until the debt is paid
    while unPaidBalance >= 0 :

        unPaidBalance = balance
        # loops through every Month

        for i in range(12):

            unPaidBalance = unPaidBalance - MonthlyRate
            intrestAmount = (annualIntrest/12) * unPaidBalance
            unPaidBalance +=intrestAmount
        #changing monthly payement by 10 every time the loop is still true
        MonthlyRate+=10


    return MonthlyRate -10
