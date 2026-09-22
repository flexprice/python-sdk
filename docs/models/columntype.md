# ColumnType

## Example Usage

```python
from flexprice.models import ColumnType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ColumnType = "string"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"string"`
- `"decimal"`
- `"datetime"`
