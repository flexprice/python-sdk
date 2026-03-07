# EntityType

## Example Usage

```python
from flexprice.models import EntityType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: EntityType = "EVENTS"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"EVENTS"`
- `"PRICES"`
- `"CUSTOMERS"`
- `"FEATURES"`
