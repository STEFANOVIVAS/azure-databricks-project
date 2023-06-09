# Databricks notebook source
# MAGIC %md
# MAGIC #### Step 1 - Set schema and load data

# COMMAND ----------

dbutils.widgets.text("param_data_source","")
var_data_source=dbutils.widgets.get("param_data_source")

# COMMAND ----------

dbutils.widgets.text("param_file_date","2021-03-21")
var_file_date=dbutils.widgets.get("param_file_date")

# COMMAND ----------

# MAGIC %run "../Includes/Configuration"

# COMMAND ----------

# MAGIC %run "../Includes/Commom_functions"

# COMMAND ----------

from pyspark.sql.types import StructType,StructField,IntegerType,StringType,DateType


# COMMAND ----------

pit_stops_schema=StructType(fields=[StructField("raceId",IntegerType(),False),
                                    StructField("driverId",IntegerType(),True),
                                    StructField("stop",StringType(),True),
                                    StructField("lap",IntegerType(),True),
                                    StructField("time",StringType(),True),
                                    StructField("duration",StringType(),True),
                                    StructField("milliseconds",IntegerType(),True)                               
                                    
                                    ])

# COMMAND ----------

pit_stops_df=spark.read.schema(pit_stops_schema).option("multiline",True).json(f"{raw_folder_path}/{var_file_date}/pit_stops.json")

# COMMAND ----------

pit_stops_df.printSchema()

# COMMAND ----------

display(pit_stops_df)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Step 2 - Rename columns and create ingestion date column

# COMMAND ----------

from pyspark.sql.functions import lit

# COMMAND ----------

pit_stops_final_df=add_ingestion_date(pit_stops_df).withColumnRenamed("driverId","driver_id").withColumnRenamed("raceId","race_id").withColumn("data_source",lit(var_data_source)).withColumn("file_date",lit(var_file_date))

# COMMAND ----------

# MAGIC %md
# MAGIC #### Step 4 - write results files to data lake

# COMMAND ----------

merge_condition="oldData.race_id=newData.race_id and oldData.driver_id=newData.driver_id and oldData.stop=newData.stop"
merge_delta_data('f1_processed','pit_stops',processed_folder_path,pit_stops_final_df,'race_id',merge_condition)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT race_id,count(*)
# MAGIC FROM f1_processed.pit_stops
# MAGIC GROUP BY race_id
# MAGIC ORDER BY race_id DESC

# COMMAND ----------

dbutils.notebook.exit("Success")
