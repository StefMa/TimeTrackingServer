# Update user settings

Update settings (or create if not exists jet):

**Route:**
```
/rest/settings/update
```
**Body:**
```
{
  "token" : "token_id",
  "settings" : {
      "default_worktime" : 7.5
  }
}
```

# Get user settings

Update settings (or create if not exists jet):

**Route:**
```
/rest/settings/get
```
**Body:**
```
{
  "token" : "token_id",
}
```
**Response:**
```
{
  "default_worktime" : 7.5
}
```
