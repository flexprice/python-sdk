# TransactionStatus

## Example Usage

```python
from flexprice.models import TransactionStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: TransactionStatus = "pending"
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `PENDING`   | pending     |
| `COMPLETED` | completed   |
| `FAILED`    | failed      |