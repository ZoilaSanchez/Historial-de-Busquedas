options(max.print=999999)
#cargar el .csv con ruta relativa
ruta = getwd()
ruta = paste(ruta, "AGraficar/historial.csv", sep="/")
print(ruta)
csv_data <- read.csv(ruta)
test <- csv_data[,c(2,4)]#Aquí elimino columnas que no me sirven para el analisis
#Las siguientes dos funciones sirven para contar Conexiones por dia y mes
ContarConexionesSemana <- function(nombre) {
  listaDiasSemana <- list(0,0,0,0,0,0,0)
  for (r in 1:nrow(test))   
    for (c in 1:ncol(test))
      if(c == 2){
        if(grepl(nombre, test[r,c]) == TRUE){
          #print(paste("Row", r, "and column",c, "have values of", test[r,c]))
          df = strftime(test[r,1],'%A')
          if(df == 'lunes'){
            listaDiasSemana[1] <- listaDiasSemana[[1]] + 1
          }else if(df == 'martes'){
            listaDiasSemana[2] <- listaDiasSemana[[2]] + 1
          }else if(df == 'miércoles'){
            listaDiasSemana[3] <- listaDiasSemana[[3]] + 1
          }else if(df == 'jueves'){
            listaDiasSemana[4] <- listaDiasSemana[[4]] + 1
          }else if(df == 'viernes'){
            listaDiasSemana[5] <- listaDiasSemana[[5]] + 1
          }else if(df == 'sábado'){
            listaDiasSemana[6] <- listaDiasSemana[[6]] + 1
          }else if(df == 'domingo'){
            listaDiasSemana[7] <- listaDiasSemana[[7]] + 1
          }
        }
      }
  return (listaDiasSemana)
}
ContarConexionesMes <- function(nombre) {
  listaMeses <- list(0,0,0,0,0,0,0,0,0,0,0,0)
  for (r in 1:nrow(test))   
    for (c in 1:ncol(test))
      if(c == 2){
        if(grepl(nombre, test[r,c]) == TRUE){
          #print(paste("Row", r, "and column",c, "have values of", test[r,c]))
          df = strftime(test[r,1],'%B')
          #print(strftime(test[r,1],'%B'))
          if(df == 'enero'){
            listaMeses[1] <- listaMeses[[1]] + 1
          }else if(df == 'febrero'){
            listaMeses[2] <- listaMeses[[2]] + 1
          }else if(df == 'marzo'){
            listaMeses[3] <- listaMeses[[3]] + 1
          }else if(df == 'abril'){
            listaMeses[4] <- listaMeses[[4]] + 1
          }else if(df == 'mayo'){
            listaMeses[5] <- listaMeses[[5]] + 1
          }else if(df == 'junio'){
            listaMeses[6] <- listaMeses[[6]] + 1
          }else if(df == 'julio'){
            listaMeses[7] <- listaMeses[[7]] + 1
          }else if(df == 'agosto'){
            listaMeses[8] <- listaMeses[[8]] + 1
          }else if(df == 'septiembre'){
            listaMeses[9] <- listaMeses[[9]] + 1
          }else if(df == 'octubre'){
            listaMeses[10] <- listaMeses[[10]] + 1
          }else if(df == 'noviembre'){
            listaMeses[11] <- listaMeses[[11]] + 1
          }else if(df == 'diciembre'){
            listaMeses[12] <- listaMeses[[12]] + 1
          }
        }
      }
  return (listaMeses)
}
listaLinks <- list("www.facebook.com","www.youtube.com","www.google.com",
                   "mail.google.com","docs.google.com","moodleurl.url.edu.gt",
                   "url.edu.gt","github.com","outlook.office.com/mail",
                   "hangouts.google.com","translate.google.com","calendar.google.com",
                   "stackoverflow.com","accounts.google.com","meet.google.com",
                   "drive.google.com","web.microsoftstream.com")
#Creando documento de visita por Día
# dias <- data.frame(listaLinks 
# )
ruta = getwd()
rutaGuardar = paste(ruta, "AGraficar/graficaSemanas.txt", sep="/")
sink(rutaGuardar)
for (i in 1:length(listaLinks)) {
  #print(listaLinks[i])
  cat(listaLinks[[i]])
  cat("\n")
  #aux <- data.frame(ContarConexionesSemana(listaLinks[i]))
  url = ContarConexionesSemana(listaLinks[i])
  #print(url)
  for(j in 1:length(url)){
    #print(url[j])
    cat(url[[j]])
    cat(", ")
  }
  cat("\n")
}
sink()

ruta = getwd()
rutaGuardar = paste(ruta, "AGraficar/graficaMes.txt", sep="/")
sink(rutaGuardar)
for (i in 1:length(listaLinks)) {
  #print(listaLinks[i])
  cat(listaLinks[[i]])
  cat("\n")
  url = ContarConexionesMes(listaLinks[i])
  #print(url)
  for(j in 1:length(url)){
    #print(url[j])
    cat(url[[j]])
    cat(", ")
  }
  cat("\n")
}
sink()
