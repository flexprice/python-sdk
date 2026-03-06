# PaymentStatus

## Example Usage

```python
from flexprice.models import PaymentStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: PaymentStatus = "INITIATED"
```


## Values

| Name                 | Value                |
| -------------------- | -------------------- |
| `INITIATED`          | INITIATED            |
| `PENDING`            | PENDING              |
| `PROCESSING`         | PROCESSING           |
| `SUCCEEDED`          | SUCCEEDED            |
| `OVERPAID`           | OVERPAID             |
| `FAILED`             | FAILED               |
| `REFUNDED`           | REFUNDED             |
| `PARTIALLY_REFUNDED` | PARTIALLY_REFUNDED   |