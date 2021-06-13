import argparse


from pyspark.sql import SparkSession


def clear_data(data_source1, data_source2, output_uri):
    with SparkSession.builder.appName("Vendor Migration").getOrCreate() as spark:
        # Load the CSV data
        if data_source1 is not None:
            vendor1 = spark.read.option(
                "header", "true").csv(data_source1)
            vendor2 = spark.read.option(
                "header", "true").csv(data_source2)

        # Create an in-memory DataFrame to query
        vendor1.createOrReplaceTempView("vendor_one")
        vendor2.createOrReplaceTempView("vendor_two")

        # Create a DataFrame of not imported details
        vendor1_unique = spark.sql("SELECT ProductId " +
                                   "FROM vendor_one " +
                                   "LEFT JOIN vendor_two " +
                                   "ON vendor_one.ProductId = vendor_two.ClassicId " +
                                   "WHERE vendor_two.ClassicId IS NULL"
                                   )

#         SELECT column_name(s)
#         FROM table1 A
#         LEFT JOIN table2 B
#         ON A.key = B.key
#         WHERE B.key IS NULL

        # Write the results to the specified output URI
        vendor1_unique.write.option(
            "header", "true").mode("overwrite").csv(output_uri)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_source1')
    parser.add_argument('--data_source2')
    parser.add_argument('--output_uri')
    args = parser.parse_args()

    clear_data(
        args.data_source1, args.data_source2, args.output_uri)
