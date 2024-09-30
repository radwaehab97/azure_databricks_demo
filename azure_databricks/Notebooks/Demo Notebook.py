# Databricks notebook source
print('Hello Radwa')

# COMMAND ----------

# MAGIC %sql
# MAGIC select 'Hello from the other side' as Text

# COMMAND ----------

# MAGIC %run ./test_notebook

# COMMAND ----------

print(name, '\n', age, '\n', work)

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------


