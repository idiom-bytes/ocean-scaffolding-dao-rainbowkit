# venv
# ocean-lib
# publish data

import ocean from ocean.lib.pseudo
import wallet from web3.lib.pseudo
import USDC, OCEAN from tokens.lib.pseudo

PRIVATE_KEY = "0x01"
# bootstrap treasury
dao_treasury = wallet.load(PRIVATE_KEY)

#clothing shop asset 1
asset_1_name = "Tuxedo Suit"
asset_1_url = "https://clothing-shop.com/tuxedo-suit.png"
asset_1_token = "USDC"
asset_1_price = "9.99"
asset_1_num_tokens = 1000

#clothing shop asset 2
asset_2_name = "Fez"
asset_2_url = "https://clothing-shop.com/fez.png"
asset_2_token = "USDC"
asset_2_price = "29.99"
asset_2_num_tokens = -1

# create asset_1
(data_NFT_1, Datatoken_1, ddo_1) = ocean.assets.create_url_asset(asset_1_name, asset_1_url, dao_treasury.address, wait_for_aqua=False)
print(f"Published jpeg 1 with data_NFT.address={data_NFT_1.address}")

# create exchange_1
exchange_1 = Datatoken_1.create_exchange(to_wei(asset_1_price), asset_1_token.address, {"from": dao_treasury.address})

# make datatokens_1 available on exchange_1
Datatoken_1.min(dao_treasury.address, to_wei(asset_1_num_tokens), {"from": dao_treasury.address})
Datatoken_1.approve(exchange_1.address, to_wei(asset_1_num_tokens), {"from": dao_treasury.address})
Datatoken_1.fre(reward_add=dao_treasury.address)

# create asset_2
(data_NFT_2, Datatoken_2, ddo_2) = ocean.assets.create_url_asset(asset_2_name, asset_2_url, dao_treasury.address, wait_for_aqua=False)
print(f"Published jpeg 2 with data_NFT.address={data_NFT_2.address}")

# create exchange_2
exchange_2 = Datatoken_2.create_exchange(to_wei(asset_2_price), asset_2_token.address, {"from": dao_treasury.address})

# make datatokens_2 available on exchange_2
Datatoken_2.min(dao_treasury.address, to_wei(asset_2_num_tokens), {"from": dao_treasury.address})
Datatoken_2.approve(exchange_2.address, to_wei(asset_2_num_tokens), {"from": dao_treasury.address})
Datatoken_2.fre(reward_add=dao_treasury.address)

# finally all fundamentall important information exported
