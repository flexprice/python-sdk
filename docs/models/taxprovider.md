# TaxProvider

## Example Usage

```python
from flexprice.models import TaxProvider

# Open enum: unrecognized values are captured as UnrecognizedStr
value: TaxProvider = "flexprice"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"flexprice"`
- `"stripe"`
