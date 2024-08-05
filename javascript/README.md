# Solana Swap API Example (JavaScript)

This example demonstrates how to use the Solana Swap API with JavaScript.


## Installation

1. Clone this repository:
   ```
   git clone https://github.com/solxtence/solana-swap-examples.git
   cd solana-swap-examples
   cd javascript
   ```

2. Install the dependencies:
   ```
   npm install
   ```

## Usage

1. Replace `"YOUR_PRIVATE_KEY"` in the `performSwap` function with your actual Solana wallet secret key.

2. Run the example:
   ```
   node example.js
   ```

## Note

This example supports both legacy and versioned transactions. You can change the `txType` parameter in the `params` object to switch between them:

- For legacy transactions: `txType: "legacy"`
- For versioned transactions: `txType: "v0"`

## Disclaimer

This is a basic example for educational purposes. In a production environment, never hardcode your secret key in the source code. Use proper key management and security practices.

If you find this example helpful, please consider giving it a star on GitHub!