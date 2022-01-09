# spark-submit /home/cloudera/exemplo.py
# To run in the command line later

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
#threads e nome no contexto
sc = SparkContext("local[2]", "Contagem")
#contexto e intervalo do batch
ssc = StreamingContext(sc, 10)
#pasta a monitorar
pesquisa = ssc.textFileStream("/Users/bf/Workspace/Cloudera/data")
#contagem
contagem = pesquisa.flatMap(lambda palavra: palavra.split(" ")) 
contagem = contagem.map(lambda pal: (pal, 1)) 
contagem = contagem.reduceByKey(lambda a, b: a + b)
#imprime
contagem.pprint()
ssc.start()             
ssc.awaitTermination()  