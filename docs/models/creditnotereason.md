# CreditNoteReason

## Example Usage

```python
from flexprice.models import CreditNoteReason

# Open enum: unrecognized values are captured as UnrecognizedStr
value: CreditNoteReason = "DUPLICATE"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"DUPLICATE"`
- `"FRAUDULENT"`
- `"ORDER_CHANGE"`
- `"UNSATISFACTORY"`
- `"SERVICE_ISSUE"`
- `"BILLING_ERROR"`
- `"SUBSCRIPTION_CANCELLATION"`
