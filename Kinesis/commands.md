## Check version of AWS CLI as the commands vary according to CLI version
```shell
aws --version
```

## V2 is the current/latest version of AWS CLI and there are high chances that this is the version you will see on the CloudShell   


## Producer 
### Command for AWS CLI v2.
```shell
aws kinesis put-record --stream-name test --partition-key user1 --data "my test record-1" --cli-binary-format raw-in-base64-out
```
### Command for AWS CLI v1
```shell
aws kinesis put-record --stream-name test --partition-key user1 --data "my test record-1"
```

## Consumer

### Describe the stream
```shell
aws kinesis describe-stream --stream-name test
```
### Consume the data from the stream
```shell
aws kinesis get-shard-iterator --stream-name test --shard-id shardId-000000000000 --shard-iterator-type TRIM_HORIZON
```
### Ger records using shard iterator
```shell
aws kinesis get-records --shard-iterator <input-iterator-here>
```

### Once done, DELETE the Kinesis data stream, as it is chargeable.