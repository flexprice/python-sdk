# DefaultShape

## Example Usage

```python
from flexprice.models import DefaultShape

# Open enum: unrecognized values are captured as UnrecognizedStr
value: DefaultShape = "timeseries"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"timeseries"`
- `"breakdown"`
- `"scalar"`
