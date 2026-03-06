# SubscriptionStatus

## Example Usage

```python
from flexprice.models import SubscriptionStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: SubscriptionStatus = "active"
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `ACTIVE`     | active       |
| `PAUSED`     | paused       |
| `CANCELLED`  | cancelled    |
| `INCOMPLETE` | incomplete   |
| `TRIALING`   | trialing     |
| `DRAFT`      | draft        |