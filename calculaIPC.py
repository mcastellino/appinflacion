#import openpyxl
#doc = openpyxl.load_workbook('ipc.xlsx')
#print(doc.get_sheet_names())
#print(doc.get_sheet_by_name('Hoja1'))
#hoja = doc.get_sheet_by_name('Hoja1')
#hoja.title
print("Este programa calcula la inflación acumulada en un período determinado entre dos meses, usando el IPC de CABA")
print("INSTRUCCIONES: primero ingrese el INDICE del último mes del período (es decir el más cercano a la fecha actual")
print("y luego ingrese cualquier INDICE de los meses anteriores a este, para obtener la inflación acumulado del período señalado") 
print("ADVERTENCIA: el INDICE debe exprsarse con el siguiente formato ->  xxx.xx  (usar punto . para los decimales)")
print (" ")

print ("Ingrese el índice del ULTIMO MES del período a analizar (más actual): ")
IndiceMesMayor = input()

print ("Ingrese el índice del MES anterior al ULTIMO del período a analizar: ")
IndiceMesMenor = input()

#Calculos: Formula -> Ejemplo: (DIC-2017 % DIC-2016) - 1 = (*100)
IndiceMesMenor = float(IndiceMesMenor)
IndiceMesMayor = float(IndiceMesMayor)
resultado = IndiceMesMayor/IndiceMesMenor
resultado = resultado-1
resultado = resultado*100

print ("La inflación acumulada es: % ",resultado)
