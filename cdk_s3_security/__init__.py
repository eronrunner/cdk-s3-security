# from aws_cdk import core as cdk
# from aws_cdk.aws_s3 import Bucket, CfnBucketPolicy
# from aws_cdk.aws_s3objectlambda import CfnAccessPoint
# from dotenv import load_dotenv
#
# class MyStack(cdk.Stack):
#     def __init__(self, scope: cdk.Construct, id: str, **kwargs) -> None:
#         super().__init__(scope, id, **kwargs)
#
#         # Create an S3 Bucket
#         bucket = Bucket(self, "MyBucket", bucket_name="example-bucket")
#
#         # Create a CfnAccessPoint (Object Lambda Access Point)
#         access_point = CfnAccessPoint(
#             self,
#             "MyAccessPoint",
#             name="MyObjectLambdaAccessPoint",
#             object_lambda_configuration={
#                 "supportingAccessPoint": bucket.bucket_arn,
#                 "cloudWatchMetricsEnabled": True,
#                 "transformationConfigurations": [
#                     {
#                         "actions": ["GetObject"],
#                         "contentTransformation": {
#                             "awsLambda": {
#                                 "functionArn": "arn:aws:lambda:us-west-2:123456789012:function:my-transform-lambda"
#                             }
#                         }
#                     }
#                 ]
#             }
#         )
#
#         # Attach a Bucket Policy to define permissions
#         CfnBucketPolicy(
#             self,
#             "BucketPolicy",
#             bucket=bucket.bucket_name,
#             policy_document={
#                 "Version": "2012-10-17",
#                 "Statement": [
#                     {
#                         "Effect": "Allow",
#                         "Principal": "*",
#                         "Action": "s3:GetObject",
#                         "Resource": f"arn:aws:s3:us-west-2:123456789012:accesspoint/{access_point.name}/object/*"
#                     },
#                     {
#                         "Effect": "Deny",
#                         "Principal": "*",
#                         "Action": "s3:PutObject",
#                         "Resource": f"arn:aws:s3:us-west-2:123456789012:accesspoint/{access_point.name}/object/*"
#                     }
#                 ]
#             }
#         )
