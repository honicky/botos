#!/usr/bin/env python3

import json
import random
import requests


url = "https://apps.beam.cloud/z9j1i"
payload = {
  "prompt": f"Talia the brown haired little girl in the blue shirt and her golden retriever dog Noa went to the kitchen to make some yummy pasta for dinner",
  "bucket_name": "botos-generated-images",
  "object_key": f"output-{random.randint(0, 1000000)}.png"
}

headers = {
  "Accept": "*/*",
  "Accept-Encoding": "gzip, deflate",
  "Authorization": "Basic YTA2NmU5MjIzMmIzMGQ5NmUwM2Y5MjQ2NDNlNmRmNDI6ODc4YWVlNmQ1MDVkMTYxNDlkZTZiNjJhMTY2ZDFmZGY=",
  "Connection": "keep-alive",
  "Content-Type": "application/json"
}

response = requests.request("POST", url, 
  headers=headers,
  data=json.dumps(payload)
)
