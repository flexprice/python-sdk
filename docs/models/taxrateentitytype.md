# TaxRateEntityType

## Example Usage

```python
from flexprice.models import TaxRateEntityType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: TaxRateEntityType = "customer"
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `CUSTOMER`     | customer       |
| `SUBSCRIPTION` | subscription   |
| `INVOICE`      | invoice        |
| `TENANT`       | tenant         |