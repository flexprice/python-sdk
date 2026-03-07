# InvoiceStatus

## Example Usage

```python
from flexprice.models import InvoiceStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: InvoiceStatus = "DRAFT"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"DRAFT"`
- `"FINALIZED"`
- `"VOIDED"`
