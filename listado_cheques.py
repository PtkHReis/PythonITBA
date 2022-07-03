import csv

info=[

]



# from auxiliar import Estado

def buscadorCheques(NombreCSV,DNIcliente,TipoCheque):
    
    with open(NombreCSV,'r') as file:
        reader = csv.reader(file)
        for NroCheque,CodigoBanco,CodigoScurusal,NumeroCuentaOrigen,NumeroCuentaDestino,Valor,FechaOrigen,FechaPago,DNI,Tipo,Estado in reader:
            if DNI == str(DNIcliente):
                if Tipo == TipoCheque:
                    # with open('info.csv','a',newline='') as Info:
                    #     writer = csv.writer(Info)
                    #     writer.writerow([NroCheque,CodigoBanco,CodigoScurusal,NumeroCuentaOrigen,NumeroCuentaDestino,Valor,FechaOrigen,FechaPago,DNI,Tipo,Estado])
                    print([NroCheque,CodigoBanco,CodigoScurusal,NumeroCuentaOrigen,NumeroCuentaDestino,Valor,FechaOrigen,FechaPago,DNI,Tipo,Estado])
                    info.append([NroCheque,CodigoBanco,CodigoScurusal,NumeroCuentaOrigen,NumeroCuentaDestino,Valor,FechaOrigen,FechaPago,DNI,Tipo,Estado])

with open("info.csv","w",newline="") as file:
    writer=csv.writer(file,delimiter=";")
    writer.writerows(info)

NombreCSV="cheques.csv"
DNIcliente=int(input("Ingrese su DNI:"))
TipoCheque=input("Ingrese Tipo Cheque (EMITIDO O DEPOSITADO):")
buscadorCheques(NombreCSV,DNIcliente,TipoCheque)
# buscadorCheques("cheques.csv",23665789,"EMITIDO")
print(info)






                






