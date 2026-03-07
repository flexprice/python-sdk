# BillingCadence

## Example Usage

```python
from flexprice.models import BillingCadence

# Open enum: unrecognized values are captured as UnrecognizedStr
value: BillingCadence = "RECURRING"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"RECURRING"`
- `"ONETIME"`
