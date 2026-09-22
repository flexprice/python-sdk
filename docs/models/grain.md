# Grain

## Example Usage

```python
from flexprice.models import Grain

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Grain = "hour"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"hour"`
- `"day"`
- `"week"`
- `"month"`
