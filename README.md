<div align="center">
   <h2 align="center">Py-pass</h2>
   A Python-based tool that allows users to securely store and manage their passwords.
  <br><br><p align="center">
    <a
      href="https://github.com/Shirshakhtml/Py-pass/issues/new?assignees=&labels=bug">Report
      Bug</a>
      .
                 <a href="https://github.com/Shirshakhtml/Py-pass/issues">Request Feature</a>
  </p>

  <img alt="Recontool" src="https://img.shields.io/github/stars/Shirshakhtml/Py-pass">
  <img alt="Recontool" src="https://img.shields.io/github/issues/Shirshakhtml/Py-pass">
  <img alt="Recontool" src="https://img.shields.io/github/license/Shirshakhtml/Py-pass">
  <img alt="Recontool" src="https://img.shields.io/github/languages/code-size/Shirshakhtml/Py-pass"> <br />  <br />

</div>

# Description

*When a user creates an account or changes their password, the password is passed through the encrypt_password() function, which hashes the password using PBKDF2 encryption and a random salt value.The salt and the hashed password are then stored in the database, along with the user's account information. When a user attempts to log in, the password they enter is passed through the check_password() function, which hashes the entered password using the same salt value as before and compares it to the stored hashed password.If the two hashed passwords match, the password entered by the user is correct and the user is granted access. If the two hashed passwords do not match, the password entered by the user is incorrect, and access is denied.*

# Where to use ? 

- The script can be used to hash and verify customer passwords when they log in to their online banking accounts.
- The script can be used to hash and verify customer passwords when they create accounts or log in to their accounts on the retailer's website.
- To ensure that patient information is secure and cannot be easily accessed by unauthorized individuals.
- The script can be used toverify employee and citizen passwords.

# Usage

```
python3 pypass.py
```
