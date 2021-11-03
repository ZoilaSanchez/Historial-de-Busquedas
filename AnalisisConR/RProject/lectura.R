

#cargar el .csv con ruta relativa
ruta = getwd()
ruta = paste(ruta, "AGraficar/graficaMes.txt", sep="/")
print(ruta)


data01 <- read.table(file = ruta, sep=\n)
print(data01)
array <- c(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)

contador=0
for (r in 1:nrow(data01))  
  for (c in 1:ncol(data01)){
    if(r%%2!=0){
    
      #print(paste("titulo", data01[r,c], " es columna impar no. ",r))
      array[contador] <- data01[r,c]
      contador=contador+1
     
    } 
    else{
      #print(paste("titulo", data01[r,c], " es columna par no. ",r))
    }
  }

print(contador)
print(array)



















barplot(table(disney),xlab="Region",main="Happiness level by region", col=rainbow(10))


dfLetters <- data.frame(Titulo =letters, En =  1:26, Feb =  1:26, Mar =  1:26, Abr =  1:26, May =  1:26, Jun =  1:26, Jul =  1:26, Ago =  1:26, Sep =  1:26, Oct =  1:26, Nov =  1:26, Dic =  1:26)
print(dfLetters)

dfLetters <- data.frame(En, Feb , Mar )

mi_lista_4 <- list(c(1, 7, 3), c(9, 8, 1))

data.frame(matrix(unlist(mi_lista_4), nrow = length(mi_lista_4), byrow = TRUE))
do.call(rbind.data.frame, mi_lista_4) # Similar
          

