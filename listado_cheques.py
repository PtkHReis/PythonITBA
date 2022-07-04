import csv
from datetime import date, datetime


newdate = date.today()

def crearCsv(NroCheque,CodigoBanco,CodigoSucursal,NumeroCuentaOrigen,NumeroCuentaDestino,Valor,FechaOrigen,FechaPago,DNI,Tipo,Estado):
    with open(f"{DNIcliente}{newdate}.csv",'a') as Info:
        writer = csv.writer(Info)
        if contador == 1:
            writer.writerow(["NroCheque,CodigoBanco,CodigoSucursal,NumeroCuentaOrigen,NumeroCuentaDestino,Valor,FechaOrigen,FechaPago,DNI,Tipo,Estado"])
            contador += 1
        writer.writerow([NroCheque,CodigoBanco,CodigoSucursal,NumeroCuentaOrigen,NumeroCuentaDestino,Valor,FechaOrigen,FechaPago,DNI,Tipo,Estado])

def buscadorCheques(NombreCSV, DNIcliente, Salida, TipoCheque, Estados):
    contador = 1
    with open(NombreCSV, 'r') as file:
        reader = csv.reader(file)
        for NroCheque, CodigoBanco, CodigoSucursal, NumeroCuentaOrigen, NumeroCuentaDestino, Valor, FechaOrigen, FechaPago, DNI, Tipo, Estado in reader:
            if DNI == str(DNIcliente) and Tipo == TipoCheque and Estado == Estados:
                if Salida == "PANTALLA":
                    print([NroCheque, CodigoBanco, CodigoSucursal, NumeroCuentaOrigen,NumeroCuentaDestino, Valor, FechaOrigen, FechaPago, DNI, Tipo, Estado])
                else:
                    crearCsv(NroCheque,CodigoBanco,CodigoSucursal,NumeroCuentaOrigen,NumeroCuentaDestino,Valor,FechaOrigen,FechaPago,DNI,Tipo,Estado)
            elif DNI == str(DNIcliente) and Tipo==TipoCheque and Estados!="RECHAZADO" and Estados!="PENDIENTE" and Estados!="APROBADO":
                if Salida == "PANTALLA":
                        print([NroCheque,CodigoBanco,CodigoSucursal,NumeroCuentaOrigen,NumeroCuentaDestino,Valor,FechaOrigen,FechaPago,DNI,Tipo,Estado])
                else:
                        crearCsv(NroCheque,CodigoBanco,CodigoSucursal,NumeroCuentaOrigen,NumeroCuentaDestino,Valor,FechaOrigen,FechaPago,DNI,Tipo,Estado)


NombreCSV="cheques.csv"
DNIcliente=int(input("Ingrese su DNI: "))
Salida = input("Ingrese Salida (PANTALLA O CSV): ")
TipoCheque=input("Ingrese Tipo Cheque (EMITIDO O DEPOSITADO): ")
Estados=input("Ingrese Estado (APROBADO,PEDIENTE,RECHAZADO): ")
buscadorCheques(NombreCSV,DNIcliente,Salida, TipoCheque, Estados)
# buscadorCheques("cheques.csv",23665789,"EMITIDO")






                






