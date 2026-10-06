# RecurringPaymentStatus

## Example Usage

```python
from flexprice.models import RecurringPaymentStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: RecurringPaymentStatus = "PENDING"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"PENDING"`
- `"ACTIVE"`
- `"PAUSED"`
- `"REJECTED"`
- `"CANCELLED"`
- `"EXPIRED"`
- `"UNKNOWN"`
