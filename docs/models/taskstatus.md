# TaskStatus

## Example Usage

```python
from flexprice.models import TaskStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: TaskStatus = "PENDING"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"PENDING"`
- `"PROCESSING"`
- `"COMPLETED"`
- `"FAILED"`
