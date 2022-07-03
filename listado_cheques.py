import csv
from datetime import date, datetime


# from auxiliar import Estado

newdate = datetime.now()

def buscadorCheques(NombreCSV,DNIcliente,Salida,TipoCheque):
    
    with open(NombreCSV,'r') as file:
        reader = csv.reader(file)
        for NroCheque,CodigoBanco,CodigoScurusal,NumeroCuentaOrigen,NumeroCuentaDestino,Valor,FechaOrigen,FechaPago,DNI,Tipo,Estado in reader:
            if DNI == str(DNIcliente):
                if Tipo == TipoCheque:
                    if Salida == "PANTALLA":
                        print([NroCheque,CodigoBanco,CodigoScurusal,NumeroCuentaOrigen,NumeroCuentaDestino,Valor,FechaOrigen,FechaPago,DNI,Tipo,Estado])
                    else:
                        with open(f"{DNIcliente}{newdate}",'w') as Info:
                            writer = csv.writer(Info)
                            writer.writerow([NroCheque,CodigoBanco,CodigoScurusal,NumeroCuentaOrigen,NumeroCuentaDestino,Valor,FechaOrigen,FechaPago,DNI,Tipo,Estado])
                    
                    
                   

NombreCSV="cheques.csv"
DNIcliente=int(input("Ingrese su DNI:"))
Salida = input("Ingrese Salida (PANTALLA O CSV)")
TipoCheque=input("Ingrese Tipo Cheque (EMITIDO O DEPOSITADO):")
buscadorCheques(NombreCSV,DNIcliente,Salida, TipoCheque)
# buscadorCheques("cheques.csv",23665789,"EMITIDO")






                






