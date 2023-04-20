# non-functional-ransomware
Ransomware that does everything except encrypt the files. It uses twilio API to send a text message including the decryption key.
## Required installations
```bash
pip install twilio
```
## configuring SMS
- Start an account at https://www.twilio.com/try-twilio
- on the left under develop, click on phone numbers> manage> active numbers
- Create a number.
- Select Verify Caller ID and do as follows
- on the top right click on acoount and open API keys and tokens
- you will be able to se your account SID and auth token, you will need these
- you will need to edit this section:
```python
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)
message = client.messages.create(
    body=f'Encryption key: {key}\nID number: {id_number}',
    from_='your_twilio_phone_number',
    to='recipient_phone_number'
    ```
