def CalculateYearlyBalance(balance,annualIntrest):
    """
        This Function Takes in Balance in Debt and the annual interest
        this function is used to speed process by using bisection to find
        best possible minmum monthly payement to pay debt

        returns monthly Payement as a float
    """

    unPaidBalance = balance

    monthlyIntrest = annualIntrest / 12

    # we create an upper bond and a lower bond to average them
    monthlyLowerBond = unPaidBalance / 12

    upperMonthlyBond  = (unPaidBalance * ((1+ monthlyIntrest)**12) ) / 12


    #result = (monthlyLowerBond + upperMonthlyBond) / 2

    # looping and checking if the balance is bigger than epilson of 0.01
    while abs(unPaidBalance) > 0.01    :
        # the average of heighest possible payement with lowest possible payement
        result = (monthlyLowerBond + upperMonthlyBond) / 2
        unPaidBalance = balance
        for i in range(12):

            unPaidBalance = unPaidBalance - result
            intrestAmount = (annualIntrest/12) * unPaidBalance
            unPaidBalance +=intrestAmount

        # checking if the result is on the right or left side of epilson
        # to make sure to change the upper and lopwer bonds
        if(unPaidBalance > 0.01):
            monthlyLowerBond = result

        elif unPaidBalance < -0.01:
            upperMonthlyBond = result
        else:
            break


            upperMonthlyBond = result




    return round(result,2)
