#Menu basics
#1/13/24
#CSC121 M2lab-Function Review
#Aiden Allison
'''
"arrival rate of customers: "
input rateCustomers
"The service rate: "
input serviceRate
waitTime = 1/(servicerate-ratecustomers) - 1/ratecustomers
customersLine = rateCustomer/(servicerate-ratecustomers)- ratecustomers/servicerate
'''
def getInputs():
    rateCustomers = float(input("arrival rate of customers: "))
    serviceRate = float(input("The service rate: "))
    return rateCustomers, serviceRate
def calcWaitTime(Crate, Srate):
    waitTime = float(1/(Srate-Crate) - 1/Crate)
    customersLine = float(Crate/(Srate-Crate)- Crate/Srate)
    return waitTime,customersLine
def displayResult(expWaitTime):
    MinuteWait = float(expWaitTime*60)
    return MinuteWait
def main():
    a,b = getInputs()
    waitTime,customersLine = calcWaitTime(a,b)
    print(displayResult(waitTime))
'''
    print(f"Average wait time: {waitTime}")
    print(f"Average amount of customers in line: {customersLine}")
'''
if __name__ == "__main__":
    main()
