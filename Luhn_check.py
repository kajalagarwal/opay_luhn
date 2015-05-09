import falcon
import json
from datetime import datetime

class LuhnResource(object):

    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        resp.body = 'Hello world!'

    def on_post(self, req, resp):
        """Handles POST requests"""
        def digits_of( n):
            return [int(d) for d in str(n)]

        def luhn_checksum(card_number):
            digits = digits_of(card_number)
            odd_digits = digits[-1::-2]
            even_digits = digits[-2::-2]
            checksum = 0
            checksum += sum(odd_digits)
            for d in even_digits:
                checksum += sum(digits_of(d*2))
            return checksum % 10

        def calculate_luhn(partial_card_number):
            check_digit = luhn_checksum(int(partial_card_number) * 10)
            return str(check_digit) if check_digit == 0 else 10 - check_digit
        
        # read the input json in a hash-map
        raw_input = req.stream.read()
        input = json.loads(raw_input.decode('utf-8'))

        # calculate the last digit using the Luhn Algorithm.
        input_digits=input["iin"] + input["bin"] + input["sponsor"] + input["account"]
        last_digit = str(calculate_luhn(input_digits))

        # prepare and return the response.
        resp.status = falcon.HTTP_200
        resp.body=str({"cardnumber": input_digits+last_digit, \
                       "generated": str(datetime.utcnow())})


wsgi_app = api = falcon.API()
card_number = LuhnResource()
 
# things will handle all requests to the '/card_number' URL path
api.add_route('/card_number', card_number)

# run command curl -X POST --data @input.json http://localhost:8020/card_number --header "Content-Type:application/json
# run server gunicorn file_name:api
