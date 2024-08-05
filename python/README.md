# Solana Swap API Example (Python)

This example demonstrates how to use the Solana Swap API with Python.

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/solxtence/solana-swap-examples.git
   cd solana-swap-examples
   cd python
   ```

2. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Replace `"YOUR_PRIVATE_KEY"` in the `perform_swap` function with your actual Solana wallet secret key (base64 encoded).

2. Run the example:
   ```
   python example.py
   ```

## Note

This example supports both legacy and versioned transactions. You can change the `txType` parameter in the `params` dictionary to switch between them:

- For legacy transactions: `"txType": "legacy"`
- For versioned transactions: `"txType": "v0"`

## Disclaimer

This is a basic example for educational purposes. In a production environment, never hardcode your secret key in the source code. Use proper key management and security practices.

If you find this example helpful, please consider giving it a star on GitHub!