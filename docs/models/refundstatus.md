# RefundStatus

## Example Usage

```python
from flexprice.models import RefundStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: RefundStatus = "PENDING"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"PENDING"`
- `"PROCESSING"`
- `"SUCCEEDED"`
- `"FAILED"`
- `"CANCELLED"`
