# SecretProvider

## Example Usage

```python
from flexprice.models import SecretProvider

# Open enum: unrecognized values are captured as UnrecognizedStr
value: SecretProvider = "flexprice"
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `FLEXPRICE`  | flexprice    |
| `STRIPE`     | stripe       |
| `S3`         | s3           |
| `HUBSPOT`    | hubspot      |
| `RAZORPAY`   | razorpay     |
| `CHARGEBEE`  | chargebee    |
| `QUICKBOOKS` | quickbooks   |
| `NOMOD`      | nomod        |
| `MOYASAR`    | moyasar      |