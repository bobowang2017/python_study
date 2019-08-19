import functools
import traceback

from setup.helper.exceptions import *


def standard_resp(func):
    """
    Creates a standardized response. This function should be used as a decorator.
    :function: The function decorated should return a dict with one of the keys  bellow:
        success -> GET, 200
        error -> Bad Request, 400
        created -> POST, 200
        updated -> PUT, 200
        deleted -> DELETE, 200
        no-data -> No Content, 204
        not-exist -> Not Exist 404
        no-access -> NoAccessError 403
        internal-error -> InternalError 500
        ……
    :returns: json.dumps(response), status code
    """

    @functools.wraps(func)
    def make_response(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except (ReturnDataError, InputError) as e:
            return resp_error(400, str(e), data=e.data)
        except AuthFailureError as e:
            return resp_error(401, str(e), data=e.data)
        except NoAccessError as e:
            return resp_error(403, str(e), data=e.data)
        except (NotExistError, NotFoundError) as e:
            return resp_error(404, str(e), data=e.data)
        except (InternalError, NeedRecordError, K8sError, GitError, DevopsBusyError) as e:
            return resp_error(500, str(e), data=e.data)
        except Exception as e:
            return resp_error(500, str(e))
        return "success"

    return make_response


def resp_error(status, msg, data=None):
    traceback.print_exc()
    return {'status': status, 'msg': msg, 'data': data}, status
