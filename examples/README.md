# FlexPrice Python SDK

This is the Python client library for the FlexPrice API.

## Installation

```bash
pip install flexprice-client
```

## Usage

```python
import os
import time
import datetime
import flexprice_client
from flexprice_client.api import customers_api, events_api
from flexprice_client.model.dto_create_customer_request import DtoCreateCustomerRequest
from flexprice_client.model.dto_ingest_event_request import DtoIngestEventRequest

# Optional: Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Configure the API client
api_key = os.getenv("FLEXPRICE_API_KEY")
api_host = os.getenv("FLEXPRICE_API_HOST", "api.flexprice.io")

if not api_key:
    raise ValueError("FLEXPRICE_API_KEY environment variable is required")

# Configure API key authorization
configuration = flexprice_client.Configuration(
    host=f"https://{api_host}"
)

# Add API key header
configuration.api_key['ApiKeyAuth'] = api_key
configuration.api_key_prefix['ApiKeyAuth'] = ''

# Set the X-API-Key header name (required specifically for FlexPrice API)
configuration.api_key['x-api-key'] = api_key

# Create API client
with flexprice_client.ApiClient(configuration) as api_client:
    # Create API instances
    customers_api_instance = customers_api.CustomersApi(api_client)
    events_api_instance = events_api.EventsApi(api_client)

    # Generate a unique customer ID for this example
    customer_id = f"sample-customer-{int(time.time())}"
    
    # Step 1: Create a customer
    print(f"Creating customer with ID: {customer_id}...")
    
    customer_request = DtoCreateCustomerRequest(
        external_id=customer_id,
        email=f"example-{customer_id}@example.com",
        name="Example Customer",
        metadata={
            "source": "python-sdk-example",
            "created_at": datetime.datetime.now().isoformat()
        }
    )
    
    customers_api_instance.customers_post(dto_create_customer_request=customer_request)
    print("Customer created successfully!")

    # Step 2: Create an event
    print("Creating event...")
    
    event_request = DtoIngestEventRequest(
        event_name="Sample Event",
        external_customer_id=customer_id,
        properties={
            "source": "python_sample_app",
            "environment": "test",
            "timestamp": datetime.datetime.now().isoformat()
        },
        source="python_sample_app",
        timestamp=datetime.datetime.now().isoformat()
    )
    
    event_result = events_api_instance.events_post(dto_ingest_event_request=event_request)
    print(f"Event created successfully! ID: {event_result.get('event_id')}")

    # Step 3: Retrieve events for this customer
    print(f"Retrieving events for customer {customer_id}...")
    
    events = events_api_instance.events_get(external_customer_id=customer_id)
    
    print(f"Found {len(events.events)} events:")
    
    for i, event in enumerate(events.events):
        print(f"Event {i+1}: {event.id} - {event.event_name}")
        print(f"Properties: {event.properties}")
```

## Running the Example

To run the provided example:

1. Clone the repository:
   ```bash
   git clone https://github.com/flexprice/python-sdk.git
   cd python-sdk/examples
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your API credentials:
   ```bash
   cp .env.sample .env
   # Edit .env with your API key
   ```

4. Run the example:
   ```bash
   python example.py
   ```

## Features

- Complete API coverage
- Strong type hints
- Detailed documentation
- Error handling
- Asynchronous support

## Documentation

For detailed API documentation, refer to the code comments and the official FlexPrice API documentation.

## Advanced Usage

### Handling Errors

The SDK provides detailed error information through exceptions:

```python
try:
    # API call
    result = client.some_api_call()
except flexprice_client.ApiException as e:
    print(f"API exception: {e}")
    print(f"Status code: {e.status}")
    print(f"Response body: {e.body}")
except Exception as e:
    print(f"General exception: {e}")
```

### Asynchronous Usage

The SDK can be used asynchronously with libraries like `asyncio`:

```python
import asyncio
import flexprice_client
from flexprice_client.api import customers_api

async def get_customer(customer_id):
    configuration = flexprice_client.Configuration(
        host="https://api.flexprice.io"
    )
    configuration.api_key['x-api-key'] = "your-api-key"
    
    async with flexprice_client.ApiClient(configuration) as api_client:
        api = customers_api.CustomersApi(api_client)
        return await api.customers_id_get(id=customer_id)

# Run with asyncio
customer = asyncio.run(get_customer("customer-123"))
print(customer)
``` 