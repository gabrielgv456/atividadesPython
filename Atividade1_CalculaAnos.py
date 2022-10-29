import math

def calcDates(daysYearsOld):
    years  = daysYearsOld / 365
    months = (daysYearsOld % 365) / 30

    days   = (daysYearsOld % 365)  % 30
    return math.floor(years), math.floor(months), days


daysYearsOld = input('Digite a sua idade expressa em dias: ')
resultYears, resultMonths, resultDays = calcDates(int(daysYearsOld))
print(f'Você possui {resultYears} anos, {resultMonths} meses e {resultDays} dias de vida')



