#Program 3 – Imperial to Metric Conversion
#Write a console program that converts a weight given in tons (imperial), stones, pounds, and ounces 
# to the metric equivalent in metric tons, kilograms, and grams.
"""
Student Name:    Mathew Akunyili
Program Title:  3 - Imperial to metric Conversion
Description:    convert imperial to metric
"""
def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    # declare variables
    x = 35840
    y = 224
    e = 16
    v = 35.274
    r = 1000

    # Identify program
    print("Imperian To Metric Conversion")

    # Ask user to input number of tons
    tons = float(input("Enter the number of tons:"))

    # Ask user to input number of stone
    stone = float(input("Enter the number of stone:"))

    # Ask user to input number of pounds
    pounds = float(input("Enter the number of pounds:"))

    # Ask user to input number of ounces
    ounces = float(input("Enter the number of ounces:"))

    # perform calculations
    totalOunces = x * tons + y * stone + e * pounds + ounces
    totalKilos = totalOunces / v
    metricTons = int(totalKilos / r)
    #to get the kilos take the total kilos and devide it by 1000, then its remainder is the value of kilos, which is what the % symbol performs
    remainderKilos = totalKilos % r
    # to get grams you have to take the remainderkilos and minus its integeer form which would recult in the remainder then multiply it by 100
    grams = (remainderKilos - int(remainderKilos)) * r

    #print values
    print(f"The metric weight is {metricTons:.0f} metric tons, {remainderKilos:.0f} Kilos, and {grams:.1f} grams")
   









    # YOUR CODE ENDS HERE

main()