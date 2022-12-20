from pyspark.sql import SparkSession

# Define a nossa aplicação Spark
spark = SparkSession.builder.appName("StreamingApp").getOrCreate()

# Nome do arquivo para schema
arquivo = "landing/2010-summary.json"

# Diretório com os arquivos json
diretorio = "landing"

# Ler o arquivo para definir schema
df = spark.read.json(arquivo)
schema_df = df.schema

# Imprime o schema do dataframe
df.printSchema()

# lendo os arquivos e cria o dataframe em streaming
# maxFilesPerTrigger informa que le apenas um arquivo por trigger (leitura)
df_streaming = spark.readStream.schema(schema_df).option("maxFilesPerTrigger", "1").json(diretorio)

# processa os dados em streaming
resultado = df_streaming.groupBy("ORIGIN_COUNTRY_NAME").count()

# Escreve a saida do processamento para o console
# saida = resultado.writeStream.outputMode("complete").format("console").start()
saida = resultado.writeStream.outputMode("update").format("console").start()

# imprime o resultado até que a aplicação seja encerrada
saida.awaitTermination()
