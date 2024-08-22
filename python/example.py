import asyncio
import base64

import aiohttp
from solana.rpc.async_api import AsyncClient
from solders.keypair import Keypair  # type: ignore
from solders.transaction import Transaction  # type: ignore


async def perform_swap():
    # Initialize connection and keypair
    async with AsyncClient("https://api.mainnet-beta.solana.com") as client:
        keypair = Keypair.from_base58_string(
            "YOUR_PRIVATE_KEY")

        # Swap parameters
        params = {
            "from": "So11111111111111111111111111111111111111112",  # SOL
            "to": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",  # USDC
            "amount": 0.007,  # From amount
            "slip": 10,  # Slippage
            "payer": str(keypair.pubkey()),
            "fee": 0.00009,  # Priority fee
            "txType": "legacy",  # Change to "v0" for versioned transactions
        }

        try:
            async with aiohttp.ClientSession() as session:
                # Get swap transaction
                async with session.get(f"https://swap.solxtence.com/swap", params=params) as response:
                    data = await response.json()

                    serialized_tx = base64.b64decode(
                        data["transaction"]["serializedTx"])
                    tx_type = data["transaction"]["txType"]

            # Fetch the latest blockhash
            recent_blockhash = await client.get_latest_blockhash()
            blockhash = recent_blockhash.value.blockhash

            # Deserialize and sign the transaction
            if tx_type == "legacy":
                transaction = Transaction.from_bytes(serialized_tx)
                transaction.sign([keypair], blockhash)
            else:
                return print("TX type not supported :/")

            signature = await client.send_raw_transaction(bytes(transaction))
            # Send and confirm the transaction
            print("Swap successful! Transaction signature:", signature.value)

        except Exception as error:
            print(error)
            print("Error performing swap:", error)

# Run the async function
asyncio.run(perform_swap())
