## Setup AWS CLI with root account access keys. Create new profile here
```shell
aws configure --profile mfa-delete-demo
```

## Enable mfa delete for a bucket
```shell
aws s3api put-bucket-versioning --bucket your-bucket-name --versioning-configuration Status=Enabled,MFADelete=Enabled --mfa "arn-of-mfa-device mfa-code" --profile mfa-delete-demo
```
## Delete an object/file from MFA Delete enabled S3 bucket
```shell
aws s3api delete-object --bucket your-bucket-name --key your-file-key --version-id your-version-id --mfa "arn-of-mfa-device mfa-code" --profile mfa-delete-demo
```

## Disable mfa delete for the bucket
```shell
aws s3api put-bucket-versioning --bucket your-bucket-name --versioning-configuration Status=Enabled,MFADelete=Disabled --mfa "arn-of-mfa-device mfa-code" --profile mfa-delete-demo
```

## Once done, DELETE ROOT ACCOUNT ACCESS KEYS