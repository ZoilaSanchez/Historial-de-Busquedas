mex <- c('Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul','Ago','Sep','Oct','Nov','Dic')
ventas <- c(11, 13, 11, 8, 12, 11, 12, 8, 10,11,12,13)




# Definimos el vector ventas con 5 valores.


# Grafica las ventas usando puntos azules.
plot(ventas, type="o", col="blue", axes = FALSE, ann = FALSE, ylim = range(ventas))

# Crea un cuadrado como contorno del gráfico. 
box()

# Etqueta los valores del Eje x con los meses.
axis(1, at=1:12, lab=mex)

# Etiqueta los valores del Eje Y.
axis(2, las= 1)

# Crea un título de color rojo.
title(main="Resumen de ventas en 5 meses", col.main="red")

# Nombramos con un texto a los ejes de  color verde.
title(xlab="Meses", col.lab=rgb(0,0.5,0))
title(ylab="Ventas en miles de dólares", col.lab=rgb(0,0.5,0))





















# este es un apartaod bueno


#cargar el .csv con ruta relativa
ruta = getwd()
ruta = paste(ruta, "AGraficar/graficaMes.txt", sep="/")
print(ruta)


data01 <- read.table(file = ruta, sep="\n")
print(data01)


titulo <- c(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
Ene <- c(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
feb <- c(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
mar <- c(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
abr <- c(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
may <- c(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
jun <- c(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
jul <- c(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
ags <- c(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
sep <- c(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
oct <-c(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
nov <-c(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
dic <- c(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)

contador=1

contadorm=1
for (r in 1:nrow(data01))  {
  
    if(r%%2!=0){
      
      #print(paste("titulo", data01[r,1], " es columna impar no. ",r))
      titulo[contador] <- data01[r,1]
      contador=contador+1
    
      
    } 
    else{
      
      leerfrecuencia <- data01[r,1]
      texto=c(leerfrecuencia)
      
      texto_split = strsplit(texto, split=",")
      texto_columnas = data.frame(unlist(texto_split))
      print(nrow(texto_columnas)-1)
      #print(contadorm)
    #for (rr in 1:nrow(texto_columnas)-1)  {
        #print(paste("titulo", data01[r,c], " es columna impar no. ",r))
        #print(texto_columnas[rr,1])
      print(paste("cotnador es ", contadorm, "dato es ",leerfrecuencia))
      
          #if(rr!=0){
            #print(paste(texto_columnas[2,1], "  . ",r))
            Ene[contadorm] <- texto_columnas[1,1]
            feb[contadorm] <- texto_columnas[2,1] # esto es lo que debo hacer ahora solo debo fijar el contador y que llegue a 17
            mar[contadorm] <- texto_columnas[3,1]
            abr[contadorm] <- texto_columnas[4,1]
            may[contadorm] <- texto_columnas[5,1]
            jun[contadorm] <- texto_columnas[6,1]
            jul[contadorm] <- texto_columnas[7,1]
            ags[contadorm] <- texto_columnas[8,1]
            sep[contadorm] <- texto_columnas[9,1]
            oct[contadorm] <- texto_columnas[10,1]
            nov[contadorm] <- texto_columnas[11,1]
            dic[contadorm] <- texto_columnas[12,1]
          
           
            contadorm=contadorm+1
          #}
        
      #}
     
    }
  
}
library(ggplot2)
library(scales)




print(contador)
print(titulo)

laTabla = data.frame (cbind(titulo,Ene,feb,mar,abr,may,jun,jul,ags,sep,oct,nov,dic))
print(laTabla)

resumen_datos <- tapply(titulo, list(cilindros = titulo,
                                     Ene = Ene,feb = feb,mar = mar,abr = abr,may = may,jun = jun,jul = jul,ags = ags,sep = sep,oct = oct,nov = nov,dic = dic)
                        ,
                        FUN = mean, na.rm = TRUE)

print(resumen_datos)
par(mar = c(5, 5, 10, 10))

barplot(resumen_datos, xlab = "Tipo de transmisión",
        main = "Media CV",
        col = rainbow(3),
        beside = TRUE,
        legend.text = rownames(resumen_datos),
        args.legend = list(title = "Cilindros", x = "topright",
                           inset = c(-0.20, 0)))














