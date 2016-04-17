# Get working days

Get all working days in a month.

**Route:**
```
/rest/get
```
**Body:**
```
{
  "token" : "token_id"
  "year" : 2015,
  "month" : 12
}
```
**Successfully response:**
```
{
  "working_month" : {
    "year" : 2015,
    "month" : 12
  },
  "work" : [
      {
        "working_day" : {
          "year" : 2015,
          "month" : 12,
          "day" : 3
        },
        "start_time" : {
          "hour" : 5,
          "minute" : 15
        },
        "end_time" : {
          "hour" : 10,
          "minute" : 30
        },
        "break_time" : false
      },
      {
        "working_day" : {
          "year" : 2015,
          "month" : 12,
          "day" : 3
        },
        "start_time" : {
          "hour" : 16,
          "minute" : 30
        },
        "end_time" : {
          "hour" : 20,
          "minute" : 0
        },
        "break_time" : true
      }
  ]
}
```

# Save a working day

Save a working day:

**Route:**
```
/rest/save
```
**Body:**
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
