# RevenueGranularity

## Example Usage

```python
from flexprice.models import RevenueGranularity

# Open enum: unrecognized values are captured as UnrecognizedStr
value: RevenueGranularity = "day"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"day"`
- `"period"`
- `"total"`
