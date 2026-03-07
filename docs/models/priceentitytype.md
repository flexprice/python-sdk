# PriceEntityType

## Example Usage

```python
from flexprice.models import PriceEntityType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: PriceEntityType = "PLAN"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"PLAN"`
- `"SUBSCRIPTION"`
- `"ADDON"`
- `"PRICE"`
- `"COSTSHEET"`
