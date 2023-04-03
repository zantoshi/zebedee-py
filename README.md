# zebedee-python-lib
A python library that makes building with the ZBD API easy and fast. To sign-up for the ZBD API, use https://dashboard.zebedee.io .

To get started, you'll need to create a project using using the Developer Dashboard. Once you have a project, grab the API key from the API key tab. We will now assume that you have an API Key.

## example usage
```
from zbd import *

# create a new ZBD object with callback URL to get updates after there is a status update.
project_a = ZBD("api_key_goes_here", "https://your-website.com/zbd/webhook/")

# test charge with an internal id.
new_charge_a = project_a.create_charge(600, "10000", "Test Charge", "user:1")
print(new_charge_a)

# create a new ZBD object with without a callback URL for test purposes.
project_b = ZBD("api_key_goes_here")
print(project_b)

# test charge with no internal id
new_charge_b = project_b.create_charge(600, "10000", "Test Charge")
print(new_charge_b)
```