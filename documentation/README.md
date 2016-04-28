# Get working days

Get all working days in a month sort by day.

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
**Response:**

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
        "work_in_day" : [        
          {
            "name" : "Early shift"
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
  ]
}
```
> **Note:** You will get always your working_month back. But work should be empty or null

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
      "name" : "Early shift"
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
