# S3EncryptionType

## Example Usage

```python
from flexprice.models import S3EncryptionType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: S3EncryptionType = "AES256"
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `AES256`       | AES256         |
| `AWS_KMS`      | aws:kms        |
| `AWS_KMS_DSSE` | aws:kms:dsse   |