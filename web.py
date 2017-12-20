#!/usr/bin/env python3

@asyncio.coroutine
def handle_curl_xxx(request):
    pass

url_param = request.match_info['key']
query_params = parse_qs(request.query_string)

text = render('template', data)
return web.Response(text.encode('utf-8'))

@get('/blog/{id}')
def get_blog(id):
    pass

return {
    '__template__':  'index.html',
    'data': '...'
}


def get(path):
    '''
    Define decorator @get('/path')
    '''

    def decorator(func)
        @functools.wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw)

        wrapper.__method__ = 'GET'
        wrapper.__route__ = path
        return wrapper

    return decorator

# 定义 RequestHandler
class RequestHandler(object):

    def __init__(self, app, fn):
        self._app = app
        self._func = fn
        ...
    @asyncio.coroutine
    def __call__(self, request):
        kw = ... 获取参数
        r = yield from self._func(**kw):
        return r

# add_route
def add_route(app, fn):
    method = getattr(fn, '__method__', None)
    path = getattr(fn, '__route__', None)
    if path is None or method is None:
        raise ValueError('@get or @post not defined in %s.' % str(fn))
    if not asyncio.iscoroutinefunction(fn) and not inspect.isgeneratorfunction(fn):
        fn = asyncio.corouttine(fn)
    logging.info('add route %s %s => %s(%s)' % method, path, fn.__name__, ','.join(inspect.signature(fn).parameters.keys()))
    app.router.add_route(method, path, RequestHandler(app, fn))

add_route(app, handles.index)
add_route(app, handles.blog)
add_route(app, handles.create_comment)

# 自动把handler模块的所有符合条件的函数注册了:
add_route(app, 'handlers')

def add_routes(app, module_name):
    n = module_name.rfind('.')
    if n == (-1):
        mod = __import__(module_name, globals(), )
