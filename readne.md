```js
POINT:

- GET: /point
{
  "id": 1,
  "name": "point,
}

- POST: /point
{
  "name": "point",
}

- PUT: /point/1
{
  "name": "point edit",
}

- DELETE: /point/1
```

```js
MISSION:

- GET: /mission
{
  "id": 1,
  "name": "mission",
  "steps": [
    {
      "id": 1,
      "start_point": {
        "id": 1,
        "name": "point1",
      },
      "end_point": {
        "id": 2,
        "name": "point2",
      }
    },
    {
      "id": 2,
      "start_point": {
        "id": 1,
        "name": "point1",
      },
      "end_point": {
        "id": 2,
        "name": "point2",
      }
    }
  ]
}

- POST: /mission
{
  "name": "mission",
  "steps": [
    {
      "start_point_id": 1,
      "end_point_id": 2
    },
    {
      "start_point_id": 1,
      "end_point_id": 2
    }
  ]
}

- PUT: /mission/1
{
  "name": "mission edit",
  "steps": [
    {
      "start_point_id": 2,
      "end_point_id": 3
    },
    {
      "start_point_id": 4,
      "end_point_id": 5
    }
  ]
}

- DELETE: /mission/1
=> Delete mission and all steps
```
