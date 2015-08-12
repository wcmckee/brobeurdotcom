# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1439347319.522648
_enable_loop = True
_template_filename = u'themes/monospace/templates/base.tmpl'
_template_uri = u'base.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'extra_head', u'extra_js', u'belowtitle']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'base', context._clean_inheritance_tokens(), templateuri=u'base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'base')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        body_end = _import_ns.get('body_end', context.get('body_end', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        license = _import_ns.get('license', context.get('license', UNDEFINED))
        def belowtitle():
            return render_belowtitle(context._locals(__M_locals))
        search_form = _import_ns.get('search_form', context.get('search_form', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        content_footer = _import_ns.get('content_footer', context.get('content_footer', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        set_locale = _import_ns.get('set_locale', context.get('set_locale', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        base = _mako_get_namespace(context, 'base')
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(unicode(set_locale(lang)))
        __M_writer(u'\n')
        __M_writer(unicode(base.html_headstart()))
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer(u'\n')
        __M_writer(unicode(template_hooks['extra_head']()))
        __M_writer(u'\n</head>\n<body class="home blog">\n    <div id="wrap" style="width:850px">\n        <div id="container" style="width:560px">\n            ')
        __M_writer(unicode(template_hooks['page_header']()))
        __M_writer(u'\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n        </div>\n        <div id="sidebar">\n            <!--Sidebar content-->\n            <h1 id="blog-title">\n                <a href="')
        __M_writer(unicode(abs_link('/')))
        __M_writer(u'" title="')
        __M_writer(unicode(blog_title))
        __M_writer(u'">')
        __M_writer(unicode(blog_title))
        __M_writer(u'</a>\n            </h1>\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'belowtitle'):
            context['self'].belowtitle(**pageargs)
        

        __M_writer(u'\n            <ul class="unstyled">\n            <li>')
        __M_writer(unicode(license))
        __M_writer(u'</li>\n            ')
        __M_writer(unicode(base.html_navigation_links()))
        __M_writer(u'\n            <li>')
        __M_writer(unicode(search_form))
        __M_writer(u'</li>\n            ')
        __M_writer(unicode(template_hooks['menu']()))
        __M_writer(u'\n            ')
        __M_writer(unicode(template_hooks['menu_alt']()))
        __M_writer(u'\n            </ul>\n        </div>\n        <div id="footer">\n            ')
        __M_writer(unicode(content_footer))
        __M_writer(u'\n            ')
        __M_writer(unicode(template_hooks['page_footer']()))
        __M_writer(u'\n        </div>\n    </div>\n    ')
        __M_writer(unicode(base.late_load_js()))
        __M_writer(u'\n    <script type="text/javascript">jQuery("a.image-reference").colorbox({rel:"gal",maxWidth:"100%",maxHeight:"100%",scalePhotos:true});</script>\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer(u'\n    ')
        __M_writer(unicode(body_end))
        __M_writer(u'\n    ')
        __M_writer(unicode(template_hooks['body_end']()))
        __M_writer(u'\n</body>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        def extra_js():
            return render_extra_js(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_belowtitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        def belowtitle():
            return render_belowtitle(context)
        base = _mako_get_namespace(context, 'base')
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        if len(translations) > 1:
            __M_writer(u'            <small>\n                ')
            __M_writer(unicode(messages("Also available in:")))
            __M_writer(u'&nbsp;\n                ')
            __M_writer(unicode(base.html_translations()))
            __M_writer(u'\n            </small>\n')
        __M_writer(u'            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"134": 5, "140": 44, "22": 2, "153": 21, "25": 0, "165": 21, "166": 22, "167": 23, "168": 24, "169": 24, "170": 25, "171": 25, "172": 28, "178": 172, "53": 2, "54": 3, "55": 3, "56": 4, "57": 4, "62": 7, "63": 8, "64": 8, "65": 13, "66": 13, "71": 14, "72": 19, "73": 19, "74": 19, "75": 19, "76": 19, "77": 19, "82": 28, "83": 30, "84": 30, "85": 31, "86": 31, "87": 32, "88": 32, "89": 33, "90": 33, "91": 34, "92": 34, "93": 38, "94": 38, "95": 39, "96": 39, "97": 42, "98": 42, "103": 44, "104": 45, "105": 45, "106": 46, "107": 46, "113": 14, "126": 5}, "uri": "base.tmpl", "filename": "themes/monospace/templates/base.tmpl"}
__M_END_METADATA
"""
