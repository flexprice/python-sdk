# FXRateSource

## Example Usage

```python
from flexprice.models import FXRateSource

# Open enum: unrecognized values are captured as UnrecognizedStr
value: FXRateSource = "fixed"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"fixed"`
- `"market"`
