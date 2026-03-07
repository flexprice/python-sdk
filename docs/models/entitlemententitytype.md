# EntitlementEntityType

## Example Usage

```python
from flexprice.models import EntitlementEntityType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: EntitlementEntityType = "PLAN"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"PLAN"`
- `"SUBSCRIPTION"`
- `"ADDON"`
