# Databricks notebook source
print('Hello World!')

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT "Hello World from SQL!"

# COMMAND ----------

# MAGIC %run ./includes/Setup

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.ls('/databricks-datasets')

# COMMAND ----------

files=dbutils.fs.ls('/databricks-datasets')
display(files)

# COMMAND ----------


