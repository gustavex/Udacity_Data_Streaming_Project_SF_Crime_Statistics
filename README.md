# Udacity_Data_Streaming_SF_Crime_Statistics
## Beginning the Project
This project requires creating topics, starting Zookeeper and Kafka servers, and your Kafka bootstrap server. You’ll need to choose a port number (e.g., 9092, 9093..) for your Kafka topic, and come up with a Kafka topic name and modify the `zookeeper.properties` and `server.properties` appropriately.

## Workspace Environment
Modify the `zookeeper.properties` and `producer.properties` given to suit your topic and port number of your choice. Start up these servers in the terminal using the commands: \
\
`/usr/bin/zookeeper-server-start zookeeper.properties` \
`/usr/bin/kafka-server-start server.properties` \
\
You’ll need to open up two terminal tabs to execute each command.

Install requirements using the provided `./start.sh` script. This needs to be done every time you re-open the workspace, or anytime after you've refreshed, or woken up, or reset data, or used the `"Get New Content"` button in this workspace.

In the terminal, to install other packages that you think are necessary to complete the project, use `conda install <package_name>`. You may need to reinstall these packages every time you re-open the workspace, or anytime after you've refreshed, or woken up, or reset data, or used the `"Get New Content"` button in this workspace.

## Step 1
Complete the code for the server in `producer_server.py` and `kafka_server.py`.

Run producer: To run producer run `python kafka_server.py`.

Start kafka-consumer-console by running the following command:

`kafka-console-consumer --bootstrap-server localhost:9093 --topic police.department.calls --from-beginning`

Output:
![01](/01.png)

## Step 2
Run consumer `python consumer_server.py`. \
Output:
![02](/02.png) \
\
Implement all the TODO items in `data_stream.py`. Do a spark-submit using this command: \
\
`spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.4 --master local[*] data_stream.py`
\
Output:
![03](/03.png) 
## Step 3

### 1) How did changing values on the SparkSession property parameters affect the throughput and latency of the data?

`spark.executor.memory : Amount of memory to use per executor process. Increasing this values increases throughput and decreases latency.`

`spark.executor.cores : The number of cores to use on each executor. Increasing this values increases throughput and decreases latency.`

`spark.driver.memory : Amount of memory to use for the driver process. Increasing this values increases throughput and decreases latency.`

By changing the settings above, the following values were significantlly improved:\
`numInputRecords : Number of records processed in a trigger. `

`inputRowsPerSecond : The rate of data arriving. `

`processedRowsPerSecond : The rate at which Spark is processing data. `

### 2) What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?\

In my experience, the most optimal values where the following. It should be possible to find optimal values by plotting values of (for example) spark.default.parallelism against a SparkSession property, so we could easily find the values wich give maximum performance.

`spark.default.parallelism : 2`

`spark.streaming.kafka.maxRatePerPartition : 8`


