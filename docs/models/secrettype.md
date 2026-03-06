# SecretType

## Example Usage

```python
from flexprice.models import SecretType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: SecretType = "private_key"
```


## Values

| Name              | Value             |
| ----------------- | ----------------- |
| `PRIVATE_KEY`     | private_key       |
| `PUBLISHABLE_KEY` | publishable_key   |
| `INTEGRATION`     | integration       |