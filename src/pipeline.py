from pyspark.sql import DataFrame, functions as F

def transform_orders(df: DataFrame) -> DataFrame:
 required={"order_id","customer_id","order_ts","amount"}
 missing=required-set(df.columns)
 if missing: raise ValueError(f"missing columns: {sorted(missing)}")
 return (df.filter(F.col("amount")>=0).dropDuplicates(["order_id"])
   .withColumn("order_date",F.to_date("order_ts"))
   .withColumn("ingested_at",F.current_timestamp()))