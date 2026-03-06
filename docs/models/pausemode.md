# PauseMode

## Example Usage

```python
from flexprice.models import PauseMode

# Open enum: unrecognized values are captured as UnrecognizedStr
value: PauseMode = "immediate"
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `IMMEDIATE`  | immediate    |
| `SCHEDULED`  | scheduled    |
| `PERIOD_END` | period_end   |