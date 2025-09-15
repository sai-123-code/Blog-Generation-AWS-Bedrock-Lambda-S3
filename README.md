# Blog Generation Using AWS Bedrock

An end-to-end generative AI application for automated blog generation using AWS serverless architecture with Lambda, Bedrock foundation models, API Gateway, and S3 storage.

## Application Architecture Overview

<img width="1536" height="1024" alt="36e2ff59-b421-4d30-8a1b-bdb4d0b45d4f" src="https://github.com/user-attachments/assets/bdc92e2b-6600-45cd-b313-7554b9962ca0" />

The entire project executes in the AWS cloud environment, providing a scalable and cost-effective solution for AI-powered content generation.

This application creates an API for blog generation where:
- **API Gateway** receives requests with blog topics
- **Lambda function** processes the request and interfaces with Bedrock
- **Amazon Bedrock** generates blog content using foundation models (Llama 3, Claude, Titan, etc.)
- **S3** stores the generated blog as timestamped text files

## Prerequisites

- AWS account with appropriate permissions
- Access to Amazon Bedrock foundation models in your region
- Basic knowledge of AWS services (Lambda, API Gateway, S3, IAM)

## Setting Up Environment

### 1. Configure Amazon Bedrock Access
- Navigate to AWS Bedrock console
- Request access to foundation models for your region
- Ensure the models you plan to use are available and accessible

### 2. Create S3 Bucket
- Create a new S3 bucket with a unique name (e.g., `aws-bedrock-blog-generation`)
- Update the bucket name in `app.py`
- **Note:** Bucket names must be globally unique within the region

### 3. Set Up AWS Lambda Function
- **Runtime:** Python 3.13 (latest)
- **Timeout Configuration:** 3 minutes (required for model invocation)
- **Memory:** Configure based on your needs (512 MB recommended)
- Copy code from `app.py` to the Lambda function
- **Critical:** Add `AdministratorAccess` permission to the Lambda execution role

### 4. Update boto3 Layer
AWS Lambda comes with an older version of boto3. To use the latest features:

```bash
# Create python directory and install latest boto3
pip install boto3 -t python/

# Zip the python folder
zip -r boto3_layer.zip python/
```

- Upload `boto3_layer.zip` as a Lambda layer
- Attach the layer to your Lambda function
- Ensure compatibility with Python 3.13

### 5. Configure API Gateway
- Create an HTTP API in API Gateway
- Create route: `/blog-generation` (POST method)
- Integrate the route with your Lambda function
- Create deployment stage: `dev`
- Note the API endpoint URL for testing

## Lambda Function Code Structure

The Lambda function includes:
- **Blog generation function** using Bedrock foundation models
- **S3 integration** for storing generated content with timestamps
- **Error handling** and CloudWatch logging
- **JSON response formatting** for API Gateway

## Executing the Project

### Testing with Postman
1. Use the API Gateway endpoint URL
2. Set request method to **POST**
3. Configure request body as JSON:
   ```json
   {
     "blog_topic": "machine learning and generative AI"
   }
   ```
4. Send the request
5. Check response for completion confirmation

## Monitoring and Debugging

- **AWS CloudWatch:** Use Log Groups for detailed execution logs
- **API Gateway:** Monitor request/response metrics
- **S3:** Track file creation and storage usage
- **Bedrock:** Monitor model invocation metrics and costs

## Resources

- [Amazon Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/)
- [API Gateway HTTP API Guide](https://docs.aws.amazon.com/apigateway/)
- [Foundation Models on Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html)
