import os
from postal.expand import expand_address
from postal.parser import parse_address
from sanic import Sanic
from sanic.response import json


app = Sanic()
app.config.ACCESS_LOG = os.environ.get('ACCESS_LOG', 'True').lower() == 'true'


@app.route('/')
async def home(request):
    return json({'libpostal': ['expand', 'parser']})


@app.route('/expand')
async def expand(request):
    address = request.args.get('address', None)
    language = request.args.get('language', None)
    strip_accents = request.args.get('strip_accents', None)
    lowercase = request.args.get('lowercase', None)
    delete_apostrophes = request.args.get('delete_apostrophes', None)

    if not address:
        return json({'error': 'No address'})

    req = {
        'address': address,
        # FIXME fails
        'strip_accents': strip_accents == '1',
        'lowercase': lowercase == '1',
        'delete_apostrophes': delete_apostrophes == '1',
    }
    if language:
        req['languages'] = language.split(',')

    res = expand_address(**req)

    return json(res)


@app.route('/parser')
async def parser(request):
    address = request.args.get('address', None)
    language = request.args.get('language', None)
    country = request.args.get('language', None)
    if not address:
        return json({'error': 'No address'})

    req = {'address': address}
    if language:
        req['language'] = language
    if country:
        req['country'] = country

    res = parse_address(**req)

    return json(res)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
