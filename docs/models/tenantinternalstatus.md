# TenantInternalStatus

## Example Usage

```python
from flexprice.models import TenantInternalStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: TenantInternalStatus = "trialing"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"trialing"`
- `"active"`
- `"suspended"`
