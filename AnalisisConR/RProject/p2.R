


#y <- read.table ("graficaMes.txt", header = TRUE) # lee un archivo txt
ruta = getwd()
ruta = paste(ruta, "AGraficar/graficaMes.txt", sep="/")
print(ruta)

#y <- read.table (ruta, header = TRUE) # lee un archivo txt


data2 <- read.table(file = ruta)

