# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1439353972.639718
_enable_loop = True
_template_filename = u'themes/monospace/templates/post.tmpl'
_template_uri = u'post.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'extra_head']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'pheader', context._clean_inheritance_tokens(), templateuri=u'post_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'pheader')] = ns

    ns = runtime.TemplateNamespace(u'comments', context._clean_inheritance_tokens(), templateuri=u'comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'comments')] = ns

    ns = runtime.TemplateNamespace(u'helper', context._clean_inheritance_tokens(), templateuri=u'post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'helper')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        pheader = _mako_get_namespace(context, 'pheader')
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        helper = _mako_get_namespace(context, 'helper')
        date_format = context.get('date_format', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        comments = _mako_get_namespace(context, 'comments')
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        pheader = _mako_get_namespace(context, 'pheader')
        date_format = context.get('date_format', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        messages = context.get('messages', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        def content():
            return render_content(context)
        comments = _mako_get_namespace(context, 'comments')
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    <div class="post">\n    ')
        __M_writer(unicode(pheader.html_title()))
        __M_writer(u'\n        <div class="meta" style="background-color: rgb(234, 234, 234); ">\n        <span class="authordate">\n            ')
        __M_writer(unicode(messages("Posted:")))
        __M_writer(u' <time class="published" datetime="')
        __M_writer(unicode(post.date.isoformat()))
        __M_writer(u'">')
        __M_writer(unicode(post.formatted_date(date_format)))
        __M_writer(u'</time>\n')
        if not post.meta('password'):
            __M_writer(u'               [<a href="')
            __M_writer(unicode(post.source_link()))
            __M_writer(u'" id="sourcelink">')
            __M_writer(unicode(messages("Source")))
            __M_writer(u'</a>]\n')
        __M_writer(u'        </span>\n        <br>\n')
        if post.tags:
            __M_writer(u'                <span class="tags">')
            __M_writer(unicode(messages("Tags")))
            __M_writer(u':&nbsp;\n')
            for tag in post.tags:
                __M_writer(u'                    <a class="tag" href="')
                __M_writer(unicode(_link('tag', tag)))
                __M_writer(u'"><span>')
                __M_writer(unicode(tag))
                __M_writer(u'</span></a>\n')
            __M_writer(u'                </span>\n                <br>\n')
        __M_writer(u'        <span class="authordate">\n            ')
        __M_writer(unicode(pheader.html_translations(post)))
        __M_writer(u'\n        </span>\n        </div>\n    ')
        __M_writer(unicode(post.text()))
        __M_writer(u'\n    ')
        __M_writer(unicode(helper.html_pager(post)))
        __M_writer(u'\n')
        if not post.meta('nocomments'):
            __M_writer(u'        ')
            __M_writer(unicode(comments.comment_form(post.permalink(absolute=True), post.title(), post.base_path)))
            __M_writer(u'\n')
        __M_writer(u'    ')
        __M_writer(unicode(helper.mathjax_script(post)))
        __M_writer(u'\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_head():
            return render_extra_head(context)
        post = context.get('post', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(unicode(helper.twitter_card_information(post)))
        __M_writer(u'\n')
        if post.meta('keywords'):
            __M_writer(u'    <meta name="keywords" content="')
            __M_writer(filters.html_escape(unicode(post.meta('keywords'))))
            __M_writer(u'"/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"128": 6, "136": 6, "137": 7, "138": 7, "139": 8, "140": 9, "141": 9, "142": 9, "148": 142, "22": 3, "25": 4, "28": 2, "34": 0, "50": 2, "51": 3, "52": 4, "53": 5, "58": 11, "63": 42, "69": 12, "82": 12, "83": 14, "84": 14, "85": 17, "86": 17, "87": 17, "88": 17, "89": 17, "90": 17, "91": 18, "92": 19, "93": 19, "94": 19, "95": 19, "96": 19, "97": 21, "98": 23, "99": 24, "100": 24, "101": 24, "102": 25, "103": 26, "104": 26, "105": 26, "106": 26, "107": 26, "108": 28, "109": 31, "110": 32, "111": 32, "112": 35, "113": 35, "114": 36, "115": 36, "116": 37, "117": 38, "118": 38, "119": 38, "120": 40, "121": 40, "122": 40}, "uri": "post.tmpl", "filename": "themes/monospace/templates/post.tmpl"}
__M_END_METADATA
"""
