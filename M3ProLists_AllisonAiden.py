#Aiden Allison
#2/1/24
#CSC121 M3Pro_list
'''
 number of people infected = rate_inf *rate of spread
    
''' 
def infoget():
    startInfect = int(input("The starting amount of people infected?"))
    weeklyRates = float(input("Estimated rate of spread"))
    return startInfect,weeklyRates 
def calcInfect(startInfect,weeklyRates):
    startInfect = startInfect * weeklyRates
    return startInfect
def calclist(Infecttotal):
    pass
def main():
    virus_list = []
    vac_list = []
    week_list =[1,2,3,4,5,6,7,8]
    
    startInfect,weeklyRates = infoget()
    startInfect = calcInfect(startInfect,weeklyRates)
    print(week_list)
    for x in range(8):
        startInfect = calcInfect(startInfect,weeklyRates)
        virus_list.append(startInfect)
        startVaccine =  startInfect  * 0.8
        if len(vac_list) >= 4:
            vac_list.append(startVaccine)
        else:
            vac_list.append(startInfect)
    print(virus_list)
    print(vac_list)



if __name__ == "__main__":
    main()
