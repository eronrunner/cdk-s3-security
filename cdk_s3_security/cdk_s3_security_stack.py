from aws_cdk import Stack, aws_s3 as s3
from aws_cdk.aws_s3 import Bucket, CfnAccessPoint
from aws_cdk.aws_s3objectlambda import CfnAccessPoint as lambda_ac
from aws_cdk.aws_lambda import Function, Runtime, Code
from constructs import Construct
from dotenv import load_dotenv


load_dotenv()

class CdkS3SecurityStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self, "s3-security-options", bucket_name="s3-security-options")
        access_point = CfnAccessPoint(
            self, "s3-security-access-point",
            bucket=bucket.bucket_name,  # Attach the access point to the bucket
            name="s3-security-access-point",  # Name of the access point
            public_access_block_configuration={
                "BlockPublicAcls": True,
                "IgnorePublicAcls": True,
                "BlockPublicPolicy": True,
                "RestrictPublicBuckets": True
            }
        )
        function = Function(
            self,
            "s3-security-option-function",
            function_name="s3-security-option-function",
            runtime=Runtime.PYTHON_3_12,
            handler="s3_security_option.s3_access_point",
            code=Code.from_asset("handler")
        )
        # access_point = s3objectlambda.CfnAccessPoint(
        #     self, "s3-security-access-point",
        #     bucket=bucket.bucket_name,
        #     name="s3-security-access-point",
            # object_lambda_configuration=s3objectlambda.CfnAccessPoint.ObjectLambdaConfigurationProperty(
            #     supporting_access_point=,
            #     transformation_configurations=[
            #         s3objectlambda.CfnAccessPoint.TransformationConfigurationProperty(
            #             actions=["GetObject"],
            #             content_transformation={
            #                 "AwsLambda": {
            #                     "FunctionArn": f"arn:aws:lambda:{os.getenv("CDK_DEFAULT_REGION")}:{os.getenv("CDK_DEFAULT_ACCOUNT")}:function:{function.function_name}"
            #                 }
            #             },
            #         )
            #     ],
                # the properties below are optional
            #     allowed_features=["GetObject-Range"],
            #     cloud_watch_metrics_enabled=False
            # ),
        # )
        # bucket_policies = CfnBucketPolicy(
        #     self,
        #     "s3-bucket-security-policy",
        #     bucket=bucket.bucket_name,
        #     policy_document={
        #         "Version": "2012-10-17",
        #         "Statement": [
        #             {
        #                 "Effect": "Allow",
        #                 "Principal": "*",
        #                 "Action": "s3:GetObject",
        #                 "Resource": f"arn:aws:s3:{os.getenv("CDK_DEFAULT_REGION")}:{os.getenv("CDK_DEFAULT_ACCOUNT")}:accesspoint/{access_point.name}/object/*"
        #             },
        #             {
        #                 "Effect": "Deny",
        #                 "Principal": "*",
        #                 "Action": "s3:PutObject",
        #                 "Resource": f"arn:aws:s3:{os.getenv("CDK_DEFAULT_REGION")}:{os.getenv("CDK_DEFAULT_ACCOUNT")}:accesspoint/{access_point.name}/object/*"
        #             }
        #         ]
        #     }
        # )
