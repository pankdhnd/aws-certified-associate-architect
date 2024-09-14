# setup AWS CLI with root account access keys. Create new profile here
aws configure --profile mfa-delete-demo

# enable mfa delete for a bucket
aws s3api put-bucket-versioning --bucket mfa-delete-demo --versioning-configuration Status=Enabled,MFADelete=Enabled --mfa "arn-of-mfa-device mfa-code" --profile mfa-delete-demo

# disable mfa delete for the bucket
aws s3api put-bucket-versioning --bucket mfa-delete-demo --versioning-configuration Status=Enabled,MFADelete=Disabled --mfa "arn-of-mfa-device mfa-code" --profile mfa-delete-demo

# One done, DELETE ROOT ACCOUNT ACCESS KEYS