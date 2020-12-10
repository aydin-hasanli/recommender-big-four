#!/bin/bash
SCRIPTPATH=$( cd $(dirname $0) ; pwd -P )
export SPARK_CONF_DIR="${SCRIPTPATH}/conf/"

${SPARK_HOME}/bin/spark-submit \
--master local[4] \
--executor-memory 3G \
--driver-memory 3G \
--conf spark.sql.warehouse.dir="file:///tmp/spark-warehouse" \
--packages com.databricks:spark-csv_2.11:1.5.0 \
--packages com.amazonaws:aws-java-sdk-pom:1.10.34 \
--packages org.apache.hadoop:hadoop-aws:2.7.3 \
$@
