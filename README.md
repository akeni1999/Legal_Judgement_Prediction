## Step 1: Create Virtual Environment

## Step 2: Install dependencies
- Command: pip install -r requirements.txt

## Step 3: Create/Update Model.pkl file
- Command: python navie_model.py

## Step 4: Run the webserver
- Command: uvicorn webserver:app --reload


## Step 5: Make an API call

Curl Request
```
curl --location --request POST 'http://127.0.0.1:8000/demo/' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=um4PwtSQIlPLe5IsDERXGDVRL13rPpMLWtP2XesVxRFpdiQBkFgSntfIKlYfjWpw' \
--data-raw '{
    "name": [1,2,3,4]
}'
```

NodeJS Code
```
var request = require('request');
var options = {
  'method': 'POST',
  'url': 'http://127.0.0.1:8000/demo/',
  'headers': {
    'Content-Type': 'application/json',
    'Cookie': 'csrftoken=um4PwtSQIlPLe5IsDERXGDVRL13rPpMLWtP2XesVxRFpdiQBkFgSntfIKlYfjWpw'
  },
  body: JSON.stringify({"name":[1,2,3,4,5]})

};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

OUTPUT
```
{
    "message": {
        "201": {
            "title": "Causing disappearance of evidence of offence, or giving false information to screen offender",
            "description": "A, knowing that B has murdered Z, assists B to hide the body with the intention of screening B from punishment. A is liable to imprisonment of either description for seven years, and also to fine."
        },
        "302": {
            "title": "Punishment for murder",
            "description": "Whoever commits murder shall be punished with death, or [imprisonment for life], and shall also be liable to fine."
        },
        "363": {
            "title": "Punishment for kidnapping",
            "description": "Whoever kidnaps any person from India or from lawful guardianship, shall be punished with imprisonment of either description for a term which may extend to seven years, and shall also be liable to fine."
        },
        "366": {
            "title": "Kidnapping, abducting or inducing woman to compel her marriage, etc.",
            "description": "Whoever kidnaps or abducts any woman with intent that she may be compelled, or knowing it to be likely that she will be compelled, to marry any person against her will, or in order that \nshe may be forced or seduced to illicit intercourse, or knowing it to be likely that she will be forced or seduced to illicit intercourse, shall be punished with imprisonment of either \ndescription for a term which may extend to ten years, and shall also be liable to fine;And whoever,by means of criminal intimidation as defined in this Code or of abuse of authority or \nany other method of compulsion, induces any woman to go from any place with intent that she may be, or knowing that it is likely that she will be, forced or seduced to illicit intercourse\n with another person shall also be punishable aaforesaid."
        },
        "376": {
            "title": "Punishment for Rape",
            "description": "Whoever, commits rape, shall be punished with rigorous imprisonment of either description for a term which shall not be less than ten years, but which may extend to imprisonment for life, and shall also be liable to fine.Rape by a police officer or a public servant or member of armed forces or a person being on the management or on the staff of a jail, remand home or other place of custody or women’s or children’s institution or by a person on the management or on the staff of a hospital, and rape committed by a person in a position of trust or authority towards the person raped or by a near relative of the person raped, Rigorous Imprisonment for 10 years to Imprisonment for Natural-Life + Fine. Persons committing offence of rape on a woman under sixteen years of age, Rigorous Imprisonment for 20 years to Imprisonment for Natural-Life + Fine."
        }
    }
}
```

