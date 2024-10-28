## Get parameters
```shell
aws ssm get-parameters --names /my-app/dev/database-url /my-app/dev/database-password
```

## Get parameters with decryption
```shell
aws ssm get-parameters --names /my-app/dev/database-url /my-app/dev/database-password --with-decryption
```

## Get prameters by path
```shell
aws ssm get-parameters-by-path --path /my-app/dev/
```

## ## Get prameters by path in recursive manner
```shell
aws ssm get-parameters-by-path --path /my-app/ --recursive
```

## ## Get prameters by path in recursive manner, with decryption
```shell
aws ssm get-parameters-by-path --path /my-app/ --recursive --with-decryption
```