# CreditNoteReason

## Example Usage

```python
from flexprice.models import CreditNoteReason

# Open enum: unrecognized values are captured as UnrecognizedStr
value: CreditNoteReason = "DUPLICATE"
```


## Values

| Name                        | Value                       |
| --------------------------- | --------------------------- |
| `DUPLICATE`                 | DUPLICATE                   |
| `FRAUDULENT`                | FRAUDULENT                  |
| `ORDER_CHANGE`              | ORDER_CHANGE                |
| `UNSATISFACTORY`            | UNSATISFACTORY              |
| `SERVICE_ISSUE`             | SERVICE_ISSUE               |
| `BILLING_ERROR`             | BILLING_ERROR               |
| `SUBSCRIPTION_CANCELLATION` | SUBSCRIPTION_CANCELLATION   |