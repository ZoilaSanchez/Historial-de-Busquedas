

#----------------------------------------------------------------------------------
# PROYECTO NO.2 FILTRADO DE DATOS - HISTORIAL DE BUSQUEDAS
#----------------------------------------------------------------------------------

#----------------------------------------------------------------------------------
# Código para filtrado de Datos
#----------------------------------------------------------------------------------
ruta = getwd()
ruta = paste(ruta, "AGraficar/historial.csv", sep="/")
print(ruta)
historial <- read.csv(ruta)
listurl<-c()
canturl<-c()
listaLinks<-c()
for (i in 1:length(historial$url)) {
  if (length(listurl) < 1){
    urlactual <- historial[i,4]
    my_data_char <- as.character(urlactual)
    separado<-strsplit(my_data_char, split = "/")
    regURL<-c(grep(separado[[1]][3], historial$url, value = TRUE))
    listurl <- c(separado[[1]][3]) 
    canturl <-c(length(regURL))
  }
  else{
    x<-2
    existe <- FALSE
    urlactual <- historial[i,4]
    my_data_char <- as.character(urlactual) 
    separado<-strsplit(my_data_char,split = "/")
    
    for(j in 1:length(listurl)) { 
        if(listurl[[j]][1]==separado[[1]][3] ) {
          existe <- TRUE
          j<-length(listurl)
        }else{
          existe<-FALSE
        }

    }# fin del for
    
    if(existe==TRUE){
      i=i+1
    }else{
      regURL<-c(grep(separado[[1]][3], historial$url, value = TRUE))
      listurl <- c(listurl, separado[[1]][3]) 
      canturl <-c(canturl,length(regURL))
    }
  }# segundo else
  
}# primer for

canturl
listurl


