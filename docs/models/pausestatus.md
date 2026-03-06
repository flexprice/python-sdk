# PauseStatus

## Example Usage

```python
from flexprice.models import PauseStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: PauseStatus = "none"
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `NONE`      | none        |
| `ACTIVE`    | active      |
| `SCHEDULED` | scheduled   |
| `COMPLETED` | completed   |
| `CANCELLED` | cancelled   |