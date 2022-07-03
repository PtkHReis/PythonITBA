import csv

def buscadorCheques(NombreCSV,DNIcliente,TipoCheque):
    
    with open(NombreCSV,'r') as file:
        reader = csv.reader(file)
        for NroCheque,CodigoBanco,CodigoScurusal,NumeroCuentaOrigen,NumeroCuentaDestino,Valor,FechaOrigen,FechaPago,DNI,Estado,Tipo in reader:
            if DNI == DNIcliente:
                if Tipo == TipoCheque:
                    with open('info.csv','w',newline='') as Info:
                        writer = csv.writer(Info)
                        writer.writerow([NroCheque,CodigoBanco,CodigoScurusal,NumeroCuentaOrigen,NumeroCuentaDestino,Valor,FechaOrigen,FechaPago,DNI,Estado,Tipo])

                






