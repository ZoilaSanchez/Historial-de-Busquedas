library(htmlwidgets)
head(historial)

#----------------------------------------------------------------------------------
# Código para hallar las 10 página más utilizadas
#----------------------------------------------------------------------------------

listurl<-c()
canturl<-c()
for (i in 1:length(historial$url)) {
  #View(separado[[1]][3])
  if (length(listurl) < 1){
    urlactual <- historial[i,4]
   
    my_data_char <- as.character(urlactual)    # Convert numeric to character

    separado<-strsplit(my_data_char,                   # Applying strsplit to character
             split = "/")
    regURL<-c(grep(separado[[1]][3], historial$url, value = TRUE))
    listurl <- c(separado[[1]][3]) 
    canturl <-c(length(regURL))
  }
  else{
    x<-2
    existe <- FALSE
    urlactual <- historial[i,4]
    my_data_char <- as.character(urlactual)    # Convert numeric to character
    
    separado<-strsplit(my_data_char,                   # Applying strsplit to character
                       split = "/")

    
    for(j in 1:length(listurl))
    { 
      if(listurl[[j]][1]==separado[[1]][3])
      {
        existe <- TRUE
        j<-length(listurl)
      }else{
        existe<-FALSE
      }
    }
    
    if(existe==TRUE){
      i=i+1
    }else{
      regURL<-c(grep(separado[[1]][3], historial$url, value = TRUE))
      listurl <- c(listurl, separado[[1]][3]) 
      canturl <-c(canturl,length(regURL))
    }
  }
  
}

canturl
listurl

losdatos <- as.data.frame(cbind(canturl,listurl))
filtrardatosunicos<-unique(losdatos)
ruta = getwd()
rutaGuardar = paste(ruta, "AGraficar/enlacesmasbuscados1.txt", sep="/")
sink(rutaGuardar)
#mayores=subset(filtrardatosunicos,(as.numeric(canturl))>=0)
for(i in 1:length(filtrardatosunicos$listurl)){

 # cat(mayores$canturl[i][1],",", mayores$listurl[i][1],'\n')
  cat(filtrardatosunicos$canturl[i][1],",", filtrardatosunicos$listurl[i][1],'\n')
}
sink()
#----------------------------------------------------------------------------------
# Código para hallar las 10 página más utilizadas
#----------------------------------------------------------------------------------
View(historial)
View(separado)
View(regURL)
View(losdatos)
View(filtrardatosunicos)
View(mayores)
