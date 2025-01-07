def calculatePay():
    # This first line is provided for you
    hrs = input("Enter Hours:")
    try: isnumber = float(hrs)
    except: isnumber = False
    if isnumber == False: print("Error, please enter numeric input")
    else: 
        rate = input("Enter Rate:")
        try: isnumber = float(rate)
        except: isnumber = False 
        if isnumber == False: print("Error, please enter numeric input")
        else:
            if hrs <= 40: 
                pay = float(hrs)*float(rate)
            elif hrs > 40: 
                overtime = float(hrs) - 40
                pay = (40*float(rate)) + (overtime*float(rate)*1.5)
            print("Pay:", pay)
    
    # end assignment

## if you want to test locally before you try to sync
## run > python payCalculator.py

#Ignore this for now. 
if __name__ == "__main__":
    calculatePay()
