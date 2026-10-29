# AmortizationMethod

## Example Usage

```python
from flexprice.models import AmortizationMethod

# Open enum: unrecognized values are captured as UnrecognizedStr
value: AmortizationMethod = "daily"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"daily"`
- `"period_even"`
- `"period_even_prorated"`
