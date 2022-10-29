import math

valueA  = float(input('Digite o valor A em cm: '))
valueB  = float(input('Digite o valor B em cm: '))
valueC  = float(input('Digite o valor C em cm: '))

if valueA > (valueB + valueC):
    print(f'{int(valueA)}, {int(valueB)}, {int(valueC)} não formam um triângulo!')
else:
    p = (valueA + valueB + valueC) / 2
    area = round(math.sqrt(p*(p-valueA)*(p-valueB)*(p-valueC)),2)
    print(f'A área é de aproximadamente {area}cm²')