import json
import os

service_descriptor = json.loads(os.environ['VCAP_SERVICES'])

for k, v in service_descriptor:
    print(k + ' --> ' + v)