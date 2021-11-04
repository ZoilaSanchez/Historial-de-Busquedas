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
ruta = paste(ruta, "AGraficar/enlacesmasbuscados.txt", sep="/")
print(ruta)


data01 <- read.table(file = ruta, sep="\n")
print(data01)


titulo <- c()
contador=1
for (r in 1:nrow(data01))  {
  if(is.null(data01[r,1])){
    print("vacio")
  }
  if(r%%2==0){
    #print(paste("titulo", data01[r,1], " es columna impar no. ",r))
    
   
      titulo[contador] <- data01[r,1]
      contador=contador+1
   
  }
  } 

titulo


























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


#laTabla = data.frame(rbind(titulo,Ene,feb,mar,abr,may,jun,jul,ags,sep,oct,nov,dic)) # converir rn filas

#print(laTabla)

#laTabla = data.frame(cbind(titulo,Ene,feb,mar,abr,may,jun,jul,ags,sep,oct,nov,dic)) # converir en col

#print(laTabla)
laTabla = data.frame(titulo=titulo,ene=Ene,feb=feb,mar=mar,abr=abr,may=may,jun=jun,jul=jul,ags=ags,sep=sep,oct=oct,nov=nov,dic=dic) # converir rn filas

print(laTabla)


library(ggplot2)
library(scales)

dev.off()
df <- data.frame(
  group = c("Male", "Female", "Child"),
  value = c(25, 25, 50)
)
head(df)
library(ggplot2) # Cargar la librería gráfica "ggplot2"
library(dplyr) # Cargar la librería de manipulación de dataframes "dplyr"




datos <- data.frame(titulo=titulo,ene=Ene,feb=feb,mar=mar,abr=abr,may=may,jun=jun,jul=jul,ags=ags,sep=sep,oct=oct,nov=nov,dic=dic)
datos


a =ggplot(datos, aes("" ,Ene , fill = titulo)) +
  geom_bar(stat = "identity", position = "dodge") +
  scale_x_discrete()+ labs(title =" Paginas", x = "Mes Enero", y = "Fecuencia")
a
b = ggplot(datos, aes("" ,feb , fill = titulo)) +
  geom_bar(stat = "identity", position = "dodge") +
  scale_x_discrete()+ labs(title =" Paginas", x = "Mes feb", y = "Fecuencia")
b
c = ggplot(datos, aes("" ,sep , fill = titulo)) +
  geom_bar(stat = "identity", position = "dodge") 
c



library(ggplot2) # Cargar la librería gráfica "ggplot2"
library(dplyr) # Cargar la librería de manipulación de dataframes "dplyr"

sexo <- c(rep("man",20),rep("woman",20),rep("man",20),rep("woman",20))
valor <- 1:80
grupo <- c(rep("spain",25),rep("italy",25),rep("portugal",30))

datos <- data.frame(sexo=sexo, valor=valor, grupo=grupo)
datos
datos <- datos %>%
  group_by(grupo, sexo) %>%
  summarise(valor = sum(valor, na.rm = TRUE)) %>%
  ungroup() %>%
  mutate(grupo = factor(grupo, levels = .$grupo))

ggplot(datos, aes(grupo, valor, fill = sexo)) +
  geom_bar(stat = "identity", position = "dodge") +
  scale_x_discrete()









meses <- c("ene","feb","mar","abr","may","jun","jul","ags","sep","oct","nov","dic")
ggplot(data=laTabla, aes(x=titulo, y=Ene, fill=titulo)) + 
  geom_bar(stat="identity", position="dodge")







#a<-ggplot(laTabla,aes(x=titulo)) + geom_bar(fill="red2") + coord_flip()

#a + theme_classic()

#b<-ggplot(laTabla,aes(y=oct,x=titulo))+geom_bar(aes(fill=titulo))
#b

#ggplot(laTabla,aes(x=Ene))+geom_bar()+facet_wrap(~titulo,nrow =3 ) # escribe uno es por categoria 
 
attach(laTabla)
 
ggplot(laTabla,aes(x=titulo,y=Ene,Feb))+geom_bar(stat="identity",fill="lightblue")
 
 
 