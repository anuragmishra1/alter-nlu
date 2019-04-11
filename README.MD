# AlterNLU - Open Source NLU Engine (beta)

AlterNLU is an open source tool for building chatbot and AI assistant. It gives the developer a minimal approach to build an assistant or bot.

It converts natural language to structured data. Eg:

Input:
```
{"text":"I want to buy a dell laptop below $500K and get it delivered to my address in Texas, 75457."}
```

Output:
```
{
  "intent": "purchase-request",
  "confidence": 0.9484,
  "entities": [
    {
      "name": "brand",
      "parsed_value": "dell",
      "value": "dell"
    },
    {
      "name": "item",
      "parsed_value": "laptop",
      "value": "laptop"
    },
    {
      "name": "criteria",
      "parsed_value": "below",
      "value": "below"
    },
    {
      "name": "price",
      "parsed_value": "500k",
      "value": "price range"
    },
    {
      "name": "location",
      "parsed_value": "texas",
      "value": "city"
    },
    {
      "name": "location",
      "parsed_value": "75457",
      "value": "pincode"
    }
  ]
}
```

## Getting Started -

Once AlterNLU is set up [see Setting Up](#setting-Up--), you can try it out in 4 simple steps.

* Get Training Data. [Recommended : Use Kontiki Console](https://console.kontikilabs.com)

* Run AlterNLU Engine.
    ```
    python3 server.py
    ```
* Rest API training.
    ```
    http://<ip_address>:5001/train
    Method : POST
    Accept / Content_type : application/json
    Data : training_data file from Kontiki Platform.
    ```
    ```
    curl -H "Content-Type: application/json" --data @<file path> http://localhost:5001/train
    ```
* Rest API parse query.
    ```
	http://<ip_address>:5001/parse
	Method : POST
	Accept / Content_type : application/json
	Data : {"text": "<your_query>"}
    ```

## Continuous Deployment - 

Latest Model will be deployed automatically once training get completed and ready for serving.


## Setting Up -

* Install Python3 & pip
    ```
    apt-get update

    apt-get install python3.6

    apt-get install python3-pip
    ```
* Setup Virtual Environment
    ```
    pip3 install virtualenv

    virtualenv nlu

    cd nlu

    source bin/activate
    ```
* Install AlterNLU
    ```
    git clone https://github.com/Kontikilabs/alter-nlu.git -b v1.0.0-beta

    cd alter-nlu

    python3 setup.py install
    ```
* Run Server
    ```
    python3 server.py
    ```
