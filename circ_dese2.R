countdata <- read.table("counts_all.txt", header=TRUE, row.names=1)  
countdata <- countdata[ ,6:ncol(countdata)]  
colnames(countdata) <- gsub("\\.[sb]am$", "", colnames(countdata))  
condition <- factor(c(rep("Mock", 3), rep("SA", 3), rep("MeJa", 3))) 
numbering <- c(1:9) 
coldata <- data.frame(row.names=colnames(countdata), condition, numbering)  
dds <- DESeqDataSetFromMatrix(countData=countdata, colData=coldata, design=~condition)  
dds <- dds[rowSums(counts(dds))>1, ]   
dds$condition <- relevel(dds$condition, ref="Mock")  
dds <- DESeq(dds)  
rld <- rlog(dds, blind = F)  
data <- plotPCA(rld, intgroup="condition", returnData =T)  
percentVar <- round(100*attr(data, "percentVar"))  
ggplot(data, aes(PC1, PC2, color=group, shape=condition)) + geom_point(size=9) + geom_text(aes(label=group), size =3, vjust=-1.75,colour = "black") + xlab(paste0("PC1: ", percentVar[2], "% variance")) + ylab(paste0("PC2: ", percentVar[1], "% variance")) + ggtitle("PCA plot of circRNA libraries") + theme(legend.position="none")