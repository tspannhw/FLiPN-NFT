from time import sleep
from math import isnan
import time
import sys
import datetime
import subprocess
import sys
import os
from subprocess import PIPE, Popen
import traceback
import math
import base64
import json
from time import gmtime, strftime
import random, string
import psutil
import base64
import uuid
import socket 
import time
import logging
import pulsar
from pulsar.schema import *

class nft (Record):
    date = String()
    short_description = String()
    featured = Boolean()
    image_thumbnail_url = String()
    asset_contract_created_date  = String()
    asset_contract_owner = Integer()
    image_preview_url = String()
    asset_contract_symbol = String()
    twitter_username = String()
    description = String()
    asset_contract_address = String()
    external_url = String()
    token_id = String()
    asset_contract_name = String()
    asset_contract_nft_version = String()
    asset_contract_description = String()
    asset_contract_external_link = String()
    id = Integer()
    featured_image_url = String()
    slug = String()
    token_metadata = String()
    asset_contract_schema_name = String()
    animation_url = String()
    num_sales = Integer()
    image_url = String()
    asset_contract_default_to_fiat = Boolean()
    external_link = String()
    image_original_url = String()
    asset_contract_payout_address = String()
    animation_original_url = String()
    background_color = String()
    asset_contract_asset_contract_type = String()
    name = String()
    asset_contract_image_url = String()
    asset_contract_total_supply = String()
    # problematic fields id, date, name

nftRecord = nft()

nftRecord.date = "Tue, 01 Mar 2022 19:10:46 GMT"
nftRecord.id = int(319618579)
nftRecord.name = "Neon Ape Creative #271857771"
nftRecord.image_thumbnail_url = "https://lh3.googleusercontent.com/RPR_wEbCC5rXDc9rkYrBrTy-nhViHhiuQSra_mYw8ZD2yo9rqqDdWtvR00eUv2FBMm1-yUkTi8tDTJVFH23GXsw4mope7bni-8RZ=s128"
nftRecord.asset_contract_created_date = "2020-12-02T17:40:53.232025"
nftRecord.featured = bool("false")
nftRecord.asset_contract_address = "0x495f947276749ce646f68ac8c248420045cb7b5e"
nftRecord.asset_contract_name = "OpenSea Collection"
nftRecord.asset_contract_schema_name = "ERC1155"
nftRecord.image_url = "https://lh3.googleusercontent.com/1kAMlW2fFlzNAhRZ0qVhdj67TVaS7EocZAIlyhqTpXWwi5LwMcRQj6JKhgiFHZ3Ls-_aABv3IcPjDELfltjFH_DyFCwWV7h_sZCm=s120"
nftRecord.asset_contract_owner = int(102384)
nftRecord.asset_contract_created_date = "2020-12-02T17:40:53.232025"

print(nftRecord)

client = pulsar.Client('pulsar://pulsar1:6650')
producer = client.create_producer(topic='persistent://public/default/nft' ,schema=JsonSchema(nft),properties={"producer-name": "nft-py-sensor","producer-id": "nft-sensor" })

# {"date":"Tue, 01 Mar 2022 19:10:46 GMT","short_description":"","featured":"false",
#"image_thumbnail_url":"https://lh3.googleusercontent.com/RPR_wEbCC5rXDc9rkYrBrTy-nhViHhiuQSra_mYw8ZD2yo9rqqDdWtvR00eUv2FBMm1-yUkTi8tDTJVFH23GXsw4mope7bni-8RZ=s128",
#"asset_contract_created_date":"2020-12-02T17:40:53.232025",
#"asset_contract_owner":"102384","image_preview_url":
#"https://lh3.googleusercontent.com/RPR_wEbCC5rXDc9rkYrBrTy-nhViHhiuQSra_mYw8ZD2yo9rqqDdWtvR00eUv2FBMm1-yUkTi8tDTJVFH23GXsw4mope7bni-8RZ=s250",
#"asset_contract_symbol":"OPENSTORE","twitter_username":"","description":"","asset_contract_address":"0x495f947276749ce646f68ac8c248420045cb7b5e",
#"external_url":"","token_id":"83559484826446007500873262317208353680116406054037409321310589688280464228353",
#"asset_contract_name":"OpenSea Collection",
#"asset_contract_nft_version":"","asset_contract_description":"","asset_contract_external_link":"",
#"id":"319618579",
#"featured_image_url":"","slug":"neonapecreative","token_metadata":"",
#"asset_contract_schema_name":"ERC1155","animation_url":"","num_sales":"0",
#"image_url":"https://lh3.googleusercontent.com/1kAMlW2fFlzNAhRZ0qVhdj67TVaS7EocZAIlyhqTpXWwi5LwMcRQj6JKhgiFHZ3Ls-_aABv3IcPjDELfltjFH_DyFCwWV7h_sZCm=s120",
#"asset_contract_default_to_fiat":"false","external_link":"","image_original_url":"","asset_contract_payout_address":"","animation_original_url":"",
#"background_color":"","asset_contract_asset_contract_type":"semi-fungible","name":"Neon Ape Creative #271857771","asset_contract_image_url":"",
#"asset_contract_total_supply":""}

producer.send(nftRecord,partition_key=str("343434322"))
