# FLiPN-NFT

![FLiPNFriends](https://github.com/tspannhw/FLiPN-NFT/raw/main/PulsarNiFiFriends.png)

Reading OpenSea NFT with Apache NiFi, Apache Pulsar and Friends.   Meetup.  StreamNative

![FLiPN](https://github.com/tspannhw/FLiPN-NFT/raw/main/FLiPNNFT1.png)
![FLiPN](https://github.com/tspannhw/FLiPN-NFT/raw/main/FLiPNNFT2.png)

### Upcoming Meetup Demo

https://www.meetup.com/new-york-city-apache-pulsar-meetup/events/283837865/

### Pulsar Build

````
bin/pulsar-admin topics delete persistent://public/default/nft
bin/pulsar-admin topics delete persistent://public/default/crypto

bin/pulsar-admin topics create persistent://public/default/nft
bin/pulsar-admin topics create persistent://public/default/crypto

bin/pulsar-client consume "persistent://public/default/crypto" -s "nftreadercrypto" -n 0
bin/pulsar-client consume "persistent://public/default/nft" -s "nftyreader" -n 0

bin/pulsar-admin schemas get "persistent://public/default/nft"
````

### Apache NiFi Flows

![FLiPN](https://github.com/tspannhw/FLiPN-NFT/raw/main/NiFiFlow1.jpg)
![FLiPN](https://github.com/tspannhw/FLiPN-NFT/raw/main/nififlow2.jpg)
![FLiPN](https://github.com/tspannhw/FLiPN-NFT/raw/main/NiFiFlow3.jpg)

### NiFi -> Pulsar Flow

![FLiPN](https://github.com/tspannhw/FLiPN-NFT/raw/main/PublishPulsarRecord.jpg)
![FLiPN](https://github.com/tspannhw/FLiPN-NFT/raw/main/PulsarClientOauthAuthService.jpg)
![FLiPN](https://github.com/tspannhw/FLiPN-NFT/raw/main/StandardPulsarClientService.jpg)

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
![FLiPN](https://github.com/tspannhw/FLiPN-NFT/blob/main/nftdata.jpg)


### StreamNative Cloud

![StreamNative](https://github.com/tspannhw/FLiPN-NFT/raw/main/sncloud.jpg)

### Example OpenSea NFT

* https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/100991634640497770476815612179593989963737896818233128255983143429914595688449
* https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/100991634640497770476815612179593989963737896818233128255983143431014107316225


![NFT1](https://lh3.googleusercontent.com/dGiERvM2GSIRNSDiulWtIsCSox6DM-xO1E4LgJ5BEhpxSSH3KvuQj3sMxIBifyzHEq60O-XvRtnn_MAO5AdM67Jl-lWzWxcXoZmJLQ=w600)
![NFT2](https://lh3.googleusercontent.com/IDTU_8Z2zjCKHzAsvZOn5_eLWvAGiXj2tIGD7FKjDc9dgFNl7CL1a044nxZRHO27FOYM2zoOGsk5lffnYSTenjRnAc4xsnV4kQhmbg=w600)

![NFTTable](https://github.com/tspannhw/FLiPN-NFT/raw/main/nfttable.jpg)

### Resources

* https://github.com/tspannhw/FLiPN-Demos
* https://www.datainmotion.dev/2021/11/producing-and-consuming-pulsar-messages.html
* https://github.com/streamnative/pulsar-nifi-bundle
* https://dzone.com/articles/pulsar-in-python-on-pi
* https://www.linkedin.com/newsletters/flip-stack-weekly-6861715928728576000/
* https://github.com/tspannhw/SpeakerProfile/tree/main/2022/talks
* https://www.slideshare.net/bunkertor/devfest-uk-ireland-using-apache-nifi-with-apache-pulsar-for-fast-data-onramp-2022
* https://www.slideshare.net/bunkertor/data-science-online-camp-using-the-flipn-stack-for-edge-ai-flink-nifi-pulsar
* https://www.slideshare.net/bunkertor/api-world-apache-nifi-101
* https://www.slideshare.net/bunkertor/ai-dev-world-utilizing-apache-pulsar-apache-ni-fi-and-minifi-for-edgeai-iot-at-scale
* https://github.com/tspannhw/EverythingApacheNiFi
* https://www.slideshare.net/bunkertor/apachecon-2021-apache-nifi-101-introduction-and-best-practices
* https://www.pulsardeveloper.com/
* https://arcade.sqlbits.com/session-details/?id=298240
