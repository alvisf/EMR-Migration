# EMR Migration AWS

## Run on EMR

1. Plan and Configure an Amazon EMR Cluster
   Create a pySpark cluster and you can leave everything else default

2. Prepare Storage for Cluster Input and Output
   Create S3 bucket for both
   Upload vendor_migration.py to Amazon S3 into the bucket

3. In Cluster List, select the name of your cluster. Make sure the cluster is in a Waiting state.

4. Choose Steps, and then choose Add step.

5. For Step type, choose Spark application. You should see additional fields for Deploy Mode, Spark-submit options, and Application location appear.

6. For Name, leave the default value or type a new name.

7. Choose Deploy mode, leave the default value Cluster.

8. Leave the Spark-submit options field blank.

9. For Application location, enter the location of your vendor_migration.py script in Amazon S3. ie, s3://DOC-EXAMPLE-BUCKET/vendor_migration.py.

In the Arguments field, enter the following arguments and values:

```
--data_source1 s3://my-website-alvisf/Vendor1.csv
--data_source2 s3://my-website-alvisf/Vendor2.csv
--output_uri s3://athena-dest/emrout
```
# aws-emr-migration
