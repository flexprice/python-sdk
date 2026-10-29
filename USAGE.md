<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from flexprice import Flexprice


with Flexprice(
    api_key_auth="<YOUR_API_KEY_HERE>",
) as f_client:

    res = f_client.accounting_periods.query_accounting_period()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from flexprice import Flexprice

async def main():

    async with Flexprice(
        api_key_auth="<YOUR_API_KEY_HERE>",
    ) as f_client:

        res = await f_client.accounting_periods.query_accounting_period_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->