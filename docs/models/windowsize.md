# WindowSize

## Example Usage

```python
from flexprice.models import WindowSize

# Open enum: unrecognized values are captured as UnrecognizedStr
value: WindowSize = "MONTH"
```


## Values

| Name          | Value         |
| ------------- | ------------- |
| `MONTH`       | MONTH         |
| `MINUTE`      | MINUTE        |
| `FIFTEEN_MIN` | 15MIN         |
| `THIRTY_MIN`  | 30MIN         |
| `HOUR`        | HOUR          |
| `THREE_HOUR`  | 3HOUR         |
| `SIX_HOUR`    | 6HOUR         |
| `TWELVE_HOUR` | 12HOUR        |
| `DAY`         | DAY           |
| `WEEK`        | WEEK          |