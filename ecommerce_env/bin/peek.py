#!/Users/inp0t/Desktop/django/ecommerce/ecommerce_env/bin/python3.9
import sys
from jwkest import jwe
from jwkest import jws

__author__ = 'roland'

jwt = sys.argv[1]

_jw = jwe.factory(jwt)
if _jw:
    print("jwe")
else:
    _jw = jws.factory(jwt)
    if _jw:
        print("jws")
        print(_jw.jwt.headers)
        print(_jw.jwt.part[1])
