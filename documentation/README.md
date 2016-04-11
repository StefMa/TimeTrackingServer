## Get all saved working days in a specific month

```
{
  "token" : "token_id"
  "year" : 2015,
  "month" : 12
}
```

## Save a specific working day in the datastore

```
{
  "token" : "token_id"
  "working_day" : {
    "year" : 2015,
    "month" : 12,
    "day" : 24
  },
  "work" : [
    {
      "start_time" : {
        "hour" : 5,
        "minute" : 15
      },
      "end_time" : {
        "hour" : 10,
        "minute" : 30
      },
      "break_time" : false
    }
  ]
}
```
