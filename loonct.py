#!/usr/bin/env python
import zillow
import argparse 

# parse the arguments 
parser = argparse.ArgumentParser(description='Query zillow for price')
parser.add_argument("--key", dest='key', required=True, help='the zillow web services ID')
args = parser.parse_args()

key = args.key

# hardcode the house
zpid = "15611999"

api = zillow.ValuationApi()
detail_data = api.GetZEstimate(key, zpid)

print detail_data.zestimate.amount
