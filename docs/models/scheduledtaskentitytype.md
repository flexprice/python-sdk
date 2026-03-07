# ScheduledTaskEntityType

## Example Usage

```python
from flexprice.models import ScheduledTaskEntityType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ScheduledTaskEntityType = "events"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"events"`
- `"invoice"`
- `"credit_topups"`
- `"credit_usage"`
