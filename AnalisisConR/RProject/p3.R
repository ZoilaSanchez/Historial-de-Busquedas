
#cargar el .csv con ruta relativa
ruta = getwd()
ruta = paste(ruta, "AGraficar/graficaMes.txt", sep="/")
print(ruta)


data01 <- read.table(file = ruta, sep="\n")
print(data01)


meses <- c("ene","feb","mar","abr","may","jun","jul","ags","sep","oct","nov","dic")
ap1 <-  c(0,0,0,0,0,0,0,0,0,0,0,0)
ap2 <-  c(0,0,0,0,0,0,0,0,0,0,0,0)
ap3 <- c(0,0,0,0,0,0,0,0,0,0,0,0)
ap4 <-  c(0,0,0,0,0,0,0,0,0,0,0,0)
ap5 <- c(0,0,0,0,0,0,0,0,0,0,0,0)
ap6 <- c(0,0,0,0,0,0,0,0,0,0,0,0)
ap7 <- c(0,0,0,0,0,0,0,0,0,0,0,0)
ap8 <-  c(0,0,0,0,0,0,0,0,0,0,0,0)
ap9 <-  c(0,0,0,0,0,0,0,0,0,0,0,0)
ap10 <- c(0,0,0,0,0,0,0,0,0,0,0,0)
ap11 <- c(0,0,0,0,0,0,0,0,0,0,0,0)
ap12 <-  c(0,0,0,0,0,0,0,0,0,0,0,0)
ap13 <- c(0,0,0,0,0,0,0,0,0,0,0,0)
ap14 <-  c(0,0,0,0,0,0,0,0,0,0,0,0)
ap15 <-  c(0,0,0,0,0,0,0,0,0,0,0,0)
ap16 <-  c(0,0,0,0,0,0,0,0,0,0,0,0)
ap17 <-  c(0,0,0,0,0,0,0,0,0,0,0,0)


contador=1

contadorm=1
for (r in 1:nrow(data01))  {
  
  if(r%%2!=0){
    
    print(paste("titulo", data01[r,1], " es columna impar no. ",r))
    #titulo[contador] <- data01[r,1]
    #contador=contador+1
    
    
  } 
  else{
    
    #leerfrecuencia <- data01[r,1]
    #texto=c(leerfrecuencia)
    
    #texto_split = strsplit(texto, split=",")
    #texto_columnas = data.frame(unlist(texto_split))
    #print(nrow(texto_columnas)-1)
    #print(contadorm)
    #for (rr in 1:nrow(texto_columnas)-1)  {
    print(paste(data01[r,1], " es columna par no. ",r))
    #print(texto_columnas[rr,1])
    #print(paste("cotnador es ", contadorm, "dato es ",leerfrecuencia))
    
    #if(rr!=0){
    print(paste(texto_columnas[2,1], "  . ",r))
    #Ene[contadorm] <- texto_columnas[1,1]
    #feb[contadorm] <- texto_columnas[2,1] # esto es lo que debo hacer ahora solo debo fijar el contador y que llegue a 17
    #mar[contadorm] <- texto_columnas[3,1]
    #abr[contadorm] <- texto_columnas[4,1]
    #may[contadorm] <- texto_columnas[5,1]
    #jun[contadorm] <- texto_columnas[6,1]
    #jul[contadorm] <- texto_columnas[7,1]
    #ags[contadorm] <- texto_columnas[8,1]
    #sep[contadorm] <- texto_columnas[9,1]
    #oct[contadorm] <- texto_columnas[10,1]
    #nov[contadorm] <- texto_columnas[11,1]
    #dic[contadorm] <- texto_columnas[12,1]
    
    

    #}
    
    #}
    
  }
  
}

print(contador)
print(meses)







laTabla = data.frame (cbind(meses,ap1,ap2,ap3,ap4,ap5,ap6,ap7,ap8,ap9,ap10,ap11,ap12,ap13,ap14,ap15,ap16,ap17))
print(laTabla)



groupTest <- sample(1:3, size = 100, replace = TRUE) 
valueTest <- sample(1:7, size = 100, replace = TRUE)
tableTest <- table(groupTest, valueTest)
barplot(tableTest, 
        col = Tango_gpl, axes = FALSE, beside = TRUE)


