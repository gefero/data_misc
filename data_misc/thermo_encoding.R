####################################################
############### Thermometer encoding ###############
####################################################


term2<-function(z,name="",media=T){
        z<-as.character(z)
        z<-model.matrix(~z-1)
        z<-1-t(apply(z,1,cumsum))
        if(media==TRUE){
                z<-z[,-ncol(z)]
        }else{
                z<-cbind(z[,ncol(z)]+1,z[,-ncol(z)])
        }
        colnames(z)<-gsub("z",name,colnames(z))
        return(z)
}



## Use expample
x = cbind(c(1,2,3,4,5,6,7),c(3,1,2,1,2,3,1))

term2(x[,1],"voto",media=T)
apply(x,2,term2,media=F)

