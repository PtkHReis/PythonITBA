import csv

from auxiliar import Estado

def buscadorCheques(NombreCSV,DNIcliente,TipoCheque):
    
    with open(NombreCSV,'r') as file:
        reader = csv.reader(file)
        for NroCheque,CodigoBanco,CodigoScurusal,NumeroCuentaOrigen,NumeroCuentaDestino,Valor,FechaOrigen,FechaPago,DNI,Tipo,Estado in reader:
            if str(DNI) == DNIcliente:
                if Tipo == TipoCheque:
                    with open('info.csv','a',newline='') as Info:
                        writer = csv.writer(Info)
                        writer.writerow([NroCheque,CodigoBanco,CodigoScurusal,NumeroCuentaOrigen,NumeroCuentaDestino,Valor,FechaOrigen,FechaPago,DNI,Tipo,Estado])








                






