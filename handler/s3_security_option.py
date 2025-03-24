import boto3


def s3_access_point(event, context):
    print("EVENT", event)
    # Extract the S3 object details from the event
    object_key = event['getObjectContext']['inputS3Url']
    output_url = event['getObjectContext']['outputRoute']
    output_token = event['getObjectContext']['outputToken']

    # Fetch the object from S3
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket='s3-security-options', Key=object_key)
    object_data = response['Body'].read()

    # Apply transformations (e.g., modify content)
    transformed_data = object_data.upper()  # Example transformation

    # Write the transformed data back to S3 Object Lambda
    s3.write_get_object_response(
        Body=transformed_data,
        RequestRoute=output_url,
        RequestToken=output_token
    )

    return {'statusCode': 200}