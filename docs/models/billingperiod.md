# BillingPeriod

## Example Usage

```python
from flexprice.models import BillingPeriod

# Open enum: unrecognized values are captured as UnrecognizedStr
value: BillingPeriod = "MONTHLY"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"MONTHLY"`
- `"ANNUAL"`
- `"WEEKLY"`
- `"DAILY"`
- `"QUARTERLY"`
- `"HALF_YEARLY"`
- `"ONETIME"`
