from zbd import *

# create a new ZBD object with callback URL to get updates after there is a status update.
project_a = ZBD("api_key_goes_here", "https://your-website.com/zbd/webhook/")

# test charge with an internal id.
new_charge = project_a.create_charge(600, "10000", "Test Charge", "user:1")

# create a new ZBD object with without a callback URL for test purposes.
project_b = ZBD("api_key_goes_here")

# test charge with no internal id or description
new_charge = project_b.create_charge(600, "10000")