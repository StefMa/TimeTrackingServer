# Create a user

Create a new user and get a token:

**Route:**
```
/rest/create
```
**Body:**
```
{
  "username" : "John Doe"
}
```
**Response:**
```
{
  "username" : "John Doe",
  "result" : "Ok|Already exist",
  "token" : "1234567890abc"
}
```
