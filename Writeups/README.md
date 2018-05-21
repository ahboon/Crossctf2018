# Crossctf 2018 Qualifier Writeups

## Web
QruirkyScript 1 - 5 were do-able by referncing the truthy table from: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness

### QuirkyScript 1
```
var flag = require("./flag.js");
var express = require('express')
var app = express()

app.get('/flag', function (req, res) {
    if (req.query.first) {
        if (req.query.first.length == 8 && req.query.first == ",,,,,,," ) {
            res.send(flag.flag);
            return;
        }
    }
    res.send("Try to solve this.");
});

app.listen(31337)
```

The following condition must be met: Length = 8 and variable must be ',,,,,,,'. To achieve this, an empty array of size 8 will match the length 8, and the empty commas in the array will be treated as a string of commas when the following is passed in: [,,,,,,,]

Therefore, to achieve this, the following get request will fulfill the conditions: ```http://target/flag?first=&first=&first=&first=&first=&first=&first=&first=&first=```
