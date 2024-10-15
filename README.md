# ATM Simulation

This is a simple Python-based ATM simulation that allows users to perform basic banking operations such as checking balance, depositing, and withdrawing money after successful authentication.

## Features

- **User Authentication**: Requires username and password for access.
- **Check Balance**: Displays the current balance.
- **Deposit Money**: Allows the user to deposit money.
- **Withdraw Money**: Allows the user to withdraw money.
- **Limited Attempts**: The user has 3 attempts to enter the correct credentials. After 3 failed attempts, the system locks them out for 24 hours.

## Getting Started

### Prerequisites

- Python 3.x must be installed on your machine.

### Running the Script

1. Clone this repository or download the script file `Atm.py`.
2. Open your terminal or command prompt.
3. Navigate to the folder where `Atm.py` is located.
4. Run the following command:

    ```bash
    python Atm.py
    ```

### Usage

1. **Login**: Enter the username and password when prompted.
    - Default credentials:
        - Username: `Pawan@`
        - Password: `1234`
2. After a successful login, you will be presented with the following options:
    - **a)** Balance check
    - **b)** Deposit amount
    - **c)** Withdraw amount
3. Follow the prompts to complete the desired operation.
4. After the operation is completed, the system will either prompt you to continue or exit.

### Example

```bash
enter username: Pawan@
enter password: 1234
welcome what you want
('a) balance check', 'b) deposit amount', 'c) withdraw amount')
press: a
5000
('a) exit', 'b) continue')
press: a
thank you
```

## Limitations

- This is a basic simulation and does not persist data across multiple sessions.
- The balance starts at a fixed value (5000) and does not save changes.
- The script uses hardcoded credentials.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
