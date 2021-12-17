# The purpose is to process new insurance policy
# Date Modified = 2021-12-17-11:03 AM
# Created by - Asian htoo

import datetime

# You Could call this my constant

Basic_Prem_Rate = 869.00
Discount_Add_Cars = .25
Extra_Lia_Rate = 130.00
Glass_Cov_Rate = 86.00
Loan_Car_Rate = 58.00
HST_Rate = .15
Mon_Payment_Fee = 39.99
Num_Car_InsCtr = 0
Next_Pol_NumCtr = 0
Tot_Extra_CostAcc = 0
InsPremAcc = 0
Tot_Ins_PremAcc = 0
HSTAcc = 0
TotalCostAcc = 0
MonthlyPayAcc = 0

f = open("OSICDef.dat", "r")
for OSICDefdataLine in f:
    OSICDefLine = OSICDefdataLine.split(",")

    Next_Pol_Num = OSICDefLine[0].strip()
    Basic_Prem_Rate = float(OSICDefLine[1].strip())
    Discount_Add_Cars = float(OSICDefLine[2].strip())
    Extra_Lia_Rate = float(OSICDefLine[3].strip())
    Glass_Cov_Rate = float(OSICDefLine[4].strip())
    Loan_Car_Rate = float(OSICDefLine[5].strip())
    HST_Rate = float(OSICDefLine[6].strip())
    Mon_Payment_Fee = float(OSICDefLine[7].strip())

f.close()

# My inputs

while True:

    while True:
        allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-'")

        NameF = input("Enter the customer first Name or (END) to end program: ")

        if NameF == "":
            print("Cannot leave blank (Enter customer first name): ")
        else:
            NameF = NameF.title()
            break

    if NameF.upper() == "END":
        print()
        print("             Thank you for using One Stop Insurance         ")
        print("                  Policy processed and saved    ^*^         ")
        break
    while True:
        allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-'")

        NameL = input("Enter the customer last name: ")

        if NameL == "":
            print("Cannot leave blank (Enter customer last name): ")
        else:
            NameL = NameL.title()
            break
    StAdd = input("Enter the customer street address: ")
    StAdd = StAdd.title()
    City = input("Enter the customer city: ")
    City = City.title()
    Prov = input("Enter the customer province: ")
    Prov = Prov.title()

    Postal = input("Enter the customer postal code: ")
    Postal = Postal.capitalize()

    while True:
        allowed_num = set("1234567890")

        PhoneNum = input("Enter the customer home phone (9999999999): ")

        if len(PhoneNum) != 10:
            print("invalid home phone - must be 10 digits: ")
        elif PhoneNum.isdigit() == False:
            print("invalid home phone - must be 10 digits: ")
        else:
            break

    Num_Car_Ins = int(input("Enter how many cars you would like to insured: "))
    ExtraLib = input("Enter if you would like Extra liability up to $1,000,000 (Y/N): ")
    ExtraLib = ExtraLib.upper()
    OPP_Glass_Cov = input("Enter if you would like Glass coverage (Y/N): ")
    OPP_Glass_Cov = OPP_Glass_Cov.upper()
    OPP_Loan_Car = input("Enter if you would like a loaner car (Y/N): ")
    OPP_Loan_Car = OPP_Loan_Car.upper()
    PayMethod = input("Enter which option you would like to pay full or Monthly (F/M): ")
    PayMethod = PayMethod.upper()

# My processing for the program

    PercentOff = Basic_Prem_Rate * 25 / 100

    if Num_Car_Ins == 1:
        InsPrem = Basic_Prem_Rate
    else:
        if Num_Car_Ins > 1:
            InsPrem = Basic_Prem_Rate - PercentOff
    while True:
        if ExtraLib == "Y":
            ExtraLiab = Extra_Lia_Rate * Num_Car_Ins

        if OPP_Glass_Cov == "Y":
            GlassCov = Glass_Cov_Rate * Num_Car_Ins

        if OPP_Loan_Car == "Y":
            LoanerCar = Loan_Car_Rate * Num_Car_Ins
            break

    Tot_Extra_Cost = ExtraLiab + GlassCov + LoanerCar
    Tot_Ins_Prem = InsPrem + Tot_Extra_Cost
    HST = Tot_Ins_Prem * HST_Rate
    TotalCost = Tot_Ins_Prem + HST
    MonthlyPay = TotalCost + Mon_Payment_Fee / 12

    Today = datetime.datetime.now()

    Num_Car_InsPad = "{:>6}".format(Num_Car_Ins)
    Tot_Extra_CostStr = "${:,.2f}".format(Tot_Extra_Cost)
    Tot_Extra_CostPad = "{:>3}".format(Tot_Extra_CostStr)
    InsPremStr = "${:,.2f}".format(InsPrem)
    InsPremPad = "{:>20}".format(InsPremStr)
    Tot_Ins_PremStr = "${:,.2f}".format(Tot_Ins_Prem)
    Tot_Ins_PremPad = "{:>5}".format(Tot_Ins_Prem)
    HSTStr = "${:,.2f}".format(HST)
    HSTPad = "{:>6}".format(HSTStr)
    TotalCostStr = "${:,.2f}".format(TotalCost)
    TotalCostPad = "{:>6}".format(TotalCostStr)
    MonthlyPayStr = "${:,.2f}".format(MonthlyPay)
    MonthlyPayPad = "{:>6}".format(MonthlyPayStr)

    # My Counter and accumulator

    Num_Car_InsCtr += Num_Car_Ins
    Next_Pol_NumCtr += 1
    Tot_Extra_CostAcc += Tot_Extra_Cost
    InsPremAcc += InsPrem
    Tot_Ins_PremAcc += Tot_Ins_Prem
    HSTAcc += HST
    TotalCostAcc += TotalCost
    MonthlyPayAcc += MonthlyPay
    Next_Pol_NumCtr = 1 + int(Next_Pol_Num)

# To add information to file Policies.dat

    f = open("Policies.dat", "a")
    f.write("{}, ".format(str(Next_Pol_NumCtr)))
    f.write("{}, ".format(str(Today)))
    f.write("{}, ".format(str(NameF)))
    f.write("{}, ".format(str(NameL)))
    f.write("{}, ".format(str(StAdd)))
    f.write("{}, ".format(str(City)))
    f.write("{}, ".format(str(Prov)))
    f.write("{}, ".format(str(Postal)))
    f.write("{}, ".format(str(PhoneNum)))
    f.write("{}, ".format(str(Num_Car_Ins)))
    f.write("{}, ".format(str(ExtraLib)))
    f.write("{}, ".format(str(OPP_Glass_Cov)))
    f.write("{}, ".format(str(OPP_Loan_Car)))
    f.write("{}\n".format(Tot_Ins_Prem))

# My output and formatting
    print()
    print("123456789012345678901234567890123456789012345678901234567890")
    print("                One Stop Insurance Company                  ")
    print("_" * 60)
    print("Customer Name: {} {}  Customers Address: {}".format(NameF, NameL, StAdd))
    print("_" * 60)
    print("      City              Province            Postal Code     ")
    print("      {}              {}                 {}            ".format(City, Prov, Postal))
    print("-" * 60)
    print("Number of cars insured:                                   #{}".format(Num_Car_InsCtr))
    print("Extra Liability (Y/N): {}                             ${:,.2f}".format(ExtraLib, ExtraLiab))
    print("Optional Glass Coverage (Y/N): {}                     ${:,.2f}".format(OPP_Glass_Cov, GlassCov))
    print("Optional Loaner Car (Y/N): {}                         ${:,.2f}".format(OPP_Loan_Car, LoanerCar))
    while True:

        if PayMethod == "F":
            print("Pay Type Full or Monthly (F/M): {}                 ${:,.2f} ".format(PayMethod, TotalCost ))
        else:
            if PayMethod == "M":
                print("Pay Type Full or Monthly (F/M): {}                 ${} ".format(PayMethod, MonthlyPay ))
                break
    print("-" * 60)
