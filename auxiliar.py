
import csv

NombreCSV = 'cheques.csv'
DNIcliente = 11580999
TipoCheque = 'EMITIDO'

with open('cheques.csv','r') as file:
    reader = csv.reader(file)
    for NroCheque,CodigoBanco,CodigoScurusal,NumeroCuentaOrigen,NumeroCuentaDestino,Valor,FechaOrigen,FechaPago,DNI,Tipo,Estado in reader:
        if Tipo == TipoCheque:
            print(NroCheque,CodigoBanco,CodigoScurusal,NumeroCuentaOrigen,NumeroCuentaDestino,Valor,FechaOrigen,FechaPago,DNI,Tipo,Estado)
        else :
            pass