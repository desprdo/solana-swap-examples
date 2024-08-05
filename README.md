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

## Notes

- These examples are for educational purposes. Always handle private keys securely in production environments.
- The API is accessed at `https://swap.solxtence.com/swap`. Check their documentation for the most up-to-date endpoint information.
- You'll need a Solana wallet and some SOL for transaction fees to run these examples.

## Contributing

Feel free to add examples in other languages or improve the existing ones. Pull requests are welcome! ✨
