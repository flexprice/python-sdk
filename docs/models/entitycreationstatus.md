# EntityCreationStatus

## Example Usage

```python
from flexprice.models import EntityCreationStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: EntityCreationStatus = "created"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"created"`
- `"superseded"`
- `"failed_already_exists"`
