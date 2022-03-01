# FLiPN-NFT

Reading OpenSea NFT with Apache NiFi, Apache Pulsar and Friends.   Meetup.  StreamNative

### Upcoming Meetup Demo

https://www.meetup.com/new-york-city-apache-pulsar-meetup/events/283837865/

### Example NFT JSON Record

````

{
  "date" : "Thu, 24 Feb 2022 22:26:41 GMT",
  "short_description" : "",
  "featured" : "false",
  "image_thumbnail_url" : "https://lh3.googleusercontent.com/-dsYkPkvAQW6KvP0Nnbjecb4Pqo1RsLvTlKKDdSPiUR4LFGqTp3mvf2uOkLtF5p1c1eLIZi6S6WhqvOX4dY-MPhCy8zg8E5_PIUTrA=s128",
  "asset_contract_created_date" : "2022-02-21T01:50:07.184731",
  "asset_contract_owner" : "240677413",
  "image_preview_url" : "https://lh3.googleusercontent.com/-dsYkPkvAQW6KvP0Nnbjecb4Pqo1RsLvTlKKDdSPiUR4LFGqTp3mvf2uOkLtF5p1c1eLIZi6S6WhqvOX4dY-MPhCy8zg8E5_PIUTrA=s250",
  "asset_contract_symbol" : "Bunny Buddies",
  "twitter_username" : "",
  "description" : "The Bunny Buddies are 8888 NFTs created by Ryan Robinson. With this collection, the 3D artist explores duality and looks for the right balance between darkness and light.",
  "asset_contract_address" : "0x91cc3844b8271337679f8c00cb2d238886917d40",
  "external_url" : "https://bunny-buddies.com/",
  "token_id" : "4640",
  "asset_contract_name" : "Bunny Buddies",
  "asset_contract_nft_version" : "3.0",
  "asset_contract_description" : "The Bunny Buddies are a collection of 8888 collectibles designed by Ryan Robinson aka Rhabbitz (Yobritish). These bunnies with crazy aesthetics and strong personalities are on their way to take over the metaverse. \nTo know more about the project, visit our website : https://bunny-buddies.com",
  "asset_contract_external_link" : "https://bunny-buddies.com/",
  "id" : "304361312",
  "featured_image_url" : "https://lh3.googleusercontent.com/xE_aoM0UA6n1-Y5_eaI5YOq3EHJA8S7AKsQrGSminMv0kuWcg2ifdz0riEdpiusV6ZPWXEE_HY1JL7QksrpLlVpORVasp5HewjgBvQ=s300",
  "slug" : "bunny-buddies",
  "token_metadata" : "https://bunnybuddies.mypinata.cloud/ipfs/QmRRavBvkQLEd1F64QxtQoeUzPvUZFJo6dhmtT5wWbvnQR/4640",
  "asset_contract_schema_name" : "ERC721",
  "animation_url" : "https://storage.opensea.io/files/482cae8fbabbff6c1d208426ed8ad961.mp4",
  "num_sales" : "0",
  "image_url" : "https://lh3.googleusercontent.com/wqWbyWmm2jrGHmuCoudc96Cikocao2L4XE1NxHSdl87I9rWC_wvA2l0ubxtQqDBpeSibZbrOuJiWK0dNTOIMDaBRIWvIkoDraMb8PWM=s120",
  "asset_contract_default_to_fiat" : "false",
  "external_link" : "",
  "image_original_url" : "https://bunnybuddies.mypinata.cloud/ipfs/QmZ8xSD7Dt48FYinQ2SKK95q2boJk7QZHsWDCKfTXUYm3J/reveal.mp4",
  "asset_contract_payout_address" : "0xfde43ebd4f75960cdac70971b731e0bab144c8f2",
  "animation_original_url" : "https://bunnybuddies.mypinata.cloud/ipfs/QmZ8xSD7Dt48FYinQ2SKK95q2boJk7QZHsWDCKfTXUYm3J/reveal.mp4",
  "background_color" : "",
  "asset_contract_asset_contract_type" : "non-fungible",
  "name" : "#4641",
  "asset_contract_image_url" : "https://lh3.googleusercontent.com/wqWbyWmm2jrGHmuCoudc96Cikocao2L4XE1NxHSdl87I9rWC_wvA2l0ubxtQqDBpeSibZbrOuJiWK0dNTOIMDaBRIWvIkoDraMb8PWM=s120",
  "asset_contract_total_supply" : "0"
}

````
