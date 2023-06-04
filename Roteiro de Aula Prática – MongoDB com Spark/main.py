from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.streaming import StreamingContext
import pandas as pd

# MongoDB configuration
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db = client['discentes2022']
collection = db['discentes2022.Alunos']

# Create SparkSession
spark = SparkSession.builder.appName("Discentes-2022").getOrCreate()

# Create StreamingContext
ssc = StreamingContext(spark.sparkContext, 1)

# Read CSV data into DataFrame
discentes = pd.read_csv('discentes-2022.csv', sep=';')
df_discentes = spark.createDataFrame(discentes)
df_discentes.show()

# Define the processing logic for the streaming data
def process_stream_data(rdd):
    # Process each RDD in the stream
    if not rdd.isEmpty():
        # Perform your desired operations on the RDD
        # Here you can save the RDD data to MongoDB or perform any other transformations

# Create a stream from the file input
stream_data = ssc.textFileStream("pasta_checkpoint")


# Apply processing logic to the stream
stream_data.foreachRDD(process_stream_data)

# Start the streaming context
ssc.start()
ssc.awaitTermination()
