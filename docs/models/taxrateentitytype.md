# TaxRateEntityType

## Example Usage

```python
from flexprice.models import TaxRateEntityType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: TaxRateEntityType = "customer"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"customer"`
- `"subscription"`
- `"invoice"`
- `"tenant"`
