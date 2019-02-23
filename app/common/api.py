import traceback
from collections import OrderedDict
from flask_restful import Api


def _get_error_details():
    trace = str(traceback.format_exc())
    return OrderedDict(("l{0:02d}".format(n), l) for n, l in enumerate(trace.split('\n'), 1))


class BaseApi(Api):
    def handle_error(self, e):
        code = getattr(e, 'code', 500)
        if code == 500:
            return self.make_response(
                dict(message=str(e), details=_get_error_details()), 500
            )
        return super().handle_error(e)
