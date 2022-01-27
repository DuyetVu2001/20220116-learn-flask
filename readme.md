```js
POINT:

- GET: /point
response:
{
  "id": 1,
  "name": "point,
}

- POST: /point
body:
{
  "name": "point",
}

- PUT: /point/1
body:
{
  "name": "point edit",
}

- DELETE: /point/1
```

```js
MISSION:

- GET: /mission
response:
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
body:
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
body:
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

```js
ROBOT:

- GET: /robot
response:
{
  "id": 1,
  "name": "agv 1"
  "robot_id": 1,
}
=> check robot is in group?

- POST: /robot
body:
{
  "name": "agv 1",
  "group_id": 1
}

- PUT: /robot/1
body:
{
  "name": "agv 1 edit",
}

- DELETE: /robot/1
```

```js
GROUP:

- GET: /group
response:
{
  "id": 1,
  "name": "group 1",
  "robots": [
    {
      "id": 1,
      "name": "agv 1"
    },
    {
      "id": 2,
      "name": "agv 2"
    }
  ],
  "mission": {
    "id": 1,
    "name": "mission 1"
  }
}

- POST: /group
body:
{
  "name": "group 1",
  "robots_id": [1, 2],
  "mission_id": 1
}

- PUT: /group/1
body:
{
  "name": "group 1 edit",
  "robots_id": [1, 2],
  "mission_id": 1
}

- DELETE: /group/1
```

```js
ORDER:

- GET: /order
response:
{
  "id": 1,
  "name": "order 1",
  "robot": {
    "id": 1,
    "name": "agv 1"
  },
  "mission": {
    "id": 1,
    "name": "mission 1"
  }
}

- POST: /group
body:
{
  "name": "order 1",
  "robot_id": 1,
  "mission_id": 1
}

- PUT: /group/1
body:
{
  "name": "order 1 edit",
  "robot_id": 1,
  "mission_id": 1
}

- DELETE: /group/1
```
