# Solana Token Swap Examples 🚀

This repo contains code samples for performing token swaps on the Solana blockchain using the SolXtence API. I created these examples to simplify the process of integrating token swaps into Solana-based projects.

## What This Does 🔄

These examples demonstrate how to:

1. Prepare swap parameters
2. Fetch a serialized swap transaction from the SolXtence API
3. Deserialize and sign the transaction
4. Send the transaction to the Solana network

The SolXtence API handles the complexities of routing swaps through various AMMs (Automated Market Makers) on Solana, including Moonshot, Raydium, and Jupiter.

## Available Examples 📚

Currently, this repo includes examples in:

- JavaScript (Node.js)
- Python

Each example is contained in its own directory with a dedicated README for setup and usage instructions.

## Getting Started 📘

1. Clone this repository
2. Choose the example in your preferred language
3. Follow the README in that example's directory for setup and usage instructions


For example, for JavaScript:

```javascript
import {
  Connection,
  Keypair,
  Transaction,
  VersionedTransaction,
  sendAndConfirmTransaction,
} from "@solana/web3.js";
import axios from "axios";
import bs58 from "bs58";

async function performSwap() {
  // Initialize connection and keypair
  const connection = new Connection("https://api.mainnet-beta.solana.com");
  const keypair = Keypair.fromSecretKey(bs58.decode("YOUR_PRIVATE_KEY"));

  // Swap parameters
  const params = new URLSearchParams({
    from: "So11111111111111111111111111111111111111112", // SOL
    to: "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v", // USDC
    amount: 0.5, // From amount
    slip: 10, // Slippage
    payer: keypair.publicKey.toBase58(),
    fee: 0.00009, // Priority fee
    txType: "v0", // Change to "legacy" for legacy transactions
  });

  try {
    // Get swap transaction
    const response = await axios.get(
      `https://swap.solxtence.com/swap?${params}`
    );
    const { serializedTx, txType } = response.data.transaction;

    // Fetch the latest blockhash
    const { blockhash } = await connection.getLatestBlockhash();

    // Deserialize and sign the transaction
    let transaction;
    if (txType === "v0") {
      transaction = VersionedTransaction.deserialize(
        Buffer.from(serializedTx, "base64")
      );
      transaction.message.recentBlockhash = blockhash;
      transaction.sign([keypair]);
    } else {
      transaction = Transaction.from(Buffer.from(serializedTx, "base64"));
      transaction.recentBlockhash = blockhash;
      transaction.sign(keypair);
    }

    // Send and confirm the transaction
    const signature = await sendAndConfirmTransaction(connection, transaction);
    console.log("Swap successful! Transaction signature:", signature);
  } catch (error) {
    console.error("Error performing swap:", error);
  }
}

performSwap();
```

## Notes

- These examples are for educational purposes. Always handle private keys securely in production environments.
- The API is accessed at `https://swap.solxtence.com/swap`. Check their documentation for the most up-to-date endpoint information.
- You'll need a Solana wallet and some SOL for transaction fees to run these examples.

## Contributing

Feel free to add examples in other languages or improve the existing ones. Pull requests are welcome! ✨
