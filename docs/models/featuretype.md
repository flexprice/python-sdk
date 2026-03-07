# FeatureType

## Example Usage

```python
from flexprice.models import FeatureType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: FeatureType = "metered"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"metered"`
- `"boolean"`
- `"static"`
