


#cargar el .csv con ruta relativa
ruta = getwd()
ruta = paste(ruta, "AGraficar/graficaMes.txt", sep="/")
print(ruta)


# en este apartado se ven los titulos de las paginas
data01 <- read.table(file = ruta, sep=\n)
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



print(contador)
print(titulo)

laTabla = data.frame (cbind(titulo,Ene,feb,mar,abr,may,jun,jul,ags,sep,oct,nov,dic))
print(laTabla)





