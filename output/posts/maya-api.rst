<html><body><p>[prettify=python]
import maya.cmds as cmds

cmd.files(f=True, new=True)

# Error: line 1: NameError: file <maya console> line 1: name 'cmd' is not defined # 

cmds.files(f=True, new=True)

# Error: line 1: AttributeError: file <maya console> line 1: 'module' object has no attribute 'files' # 

cmds.file(f=True, new=True)

# Result: untitled # 

window = cmds.window()

cmds.paneLayout()

# Result: window1|paneLayout3 # 

cmds.modelPanel()

# Result: modelPanel5 # 

cmds.showWindow(window)

import numpy

# Error: line 1: ImportError: file <maya console> line 1: No module named numpy # 

import math

help math()

# Error: line 1: invalid syntax # 

help('math')

Help on built-in module math:



NAME
    math


FILE
    (built-in)


DESCRIPTION
    This module is always available.  It provides access to the
    mathematical functions defined by the C standard.


FUNCTIONS
    acos(...)
        acos(x)
        
        Return the arc cosine (measured in radians) of x.
    
    acosh(...)
        acosh(x)
        
        Return the hyperbolic arc cosine (measured in radians) of x.
    
    asin(...)
        asin(x)
        
        Return the arc sine (measured in radians) of x.
    
    asinh(...)
        asinh(x)
        
        Return the hyperbolic arc sine (measured in radians) of x.
    
    atan(...)
        atan(x)
        
        Return the arc tangent (measured in radians) of x.
    
    atan2(...)
        atan2(y, x)
        
        Return the arc tangent (measured in radians) of y/x.
        Unlike atan(y/x), the signs of both x and y are considered.
    
    atanh(...)
        atanh(x)
        
        Return the hyperbolic arc tangent (measured in radians) of x.
    
    ceil(...)
        ceil(x)
        
        Return the ceiling of x as a float.
        This is the smallest integral value &gt;= x.
    
    copysign(...)
        copysign(x, y)
        
        Return x with the sign of y.
    
    cos(...)
        cos(x)
        
        Return the cosine of x (measured in radians).
    
    cosh(...)
        cosh(x)
        
        Return the hyperbolic cosine of x.
    
    degrees(...)
        degrees(x)
        
        Convert angle x from radians to degrees.
    
    erf(...)
        erf(x)
        
        Error function at x.
    
    erfc(...)
        erfc(x)
        
        Complementary error function at x.
    
    exp(...)
        exp(x)
        
        Return e raised to the power of x.
    
    expm1(...)
        expm1(x)
        
        Return exp(x)-1.
        This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.
    
    fabs(...)
        fabs(x)
        
        Return the absolute value of the float x.
    
    factorial(...)
        factorial(x) -&gt; Integral
        
        Find x!. Raise a ValueError if x is negative or non-integral.
    
    floor(...)
        floor(x)
        
        Return the floor of x as a float.
        This is the largest integral value  bool
        
        Check if float x is infinite (positive or negative).
    
    isnan(...)
        isnan(x) -&gt; bool
        
        Check if float x is not a number (NaN).
    
    ldexp(...)
        ldexp(x, i)
        
        Return x * (2**i).
    
    lgamma(...)
        lgamma(x)
        
        Natural logarithm of absolute value of Gamma function at x.
    
    log(...)
        log(x[, base])
        
        Return the logarithm of x to the given base.
        If the base not specified, returns the natural logarithm (base e) of x.
    
    log10(...)
        log10(x)
        
        Return the base 10 logarithm of x.
    
    log1p(...)
        log1p(x)
        
        Return the natural logarithm of 1+x (base e).
        The result is computed in a way which is accurate for x near zero.
    
    modf(...)
        modf(x)
        
        Return the fractional and integer parts of x.  Both results carry the sign
        of x and are floats.
    
    pow(...)
        pow(x, y)
        
        Return x**y (x to the power of y).
    
    radians(...)
        radians(x)
        
        Convert angle x from degrees to radians.
    
    sin(...)
        sin(x)
        
        Return the sine of x (measured in radians).
    
    sinh(...)
        sinh(x)
        
        Return the hyperbolic sine of x.
    
    sqrt(...)
        sqrt(x)
        
        Return the square root of x.
    
    tan(...)
        tan(x)
        
        Return the tangent of x (measured in radians).
    
    tanh(...)
        tanh(x)
        
        Return the hyperbolic tangent of x.
    
    trunc(...)
        trunc(x:Real) -&gt; Integral
        
        Truncates x to the nearest Integral toward 0. Uses the __trunc__ magic method.


DATA
    e = 2.718281828459045
    pi = 3.141592653589793




import random

rand = random.randint(1,20)

cod = math.acos(rand)

# Error: line 1: ValueError: file <maya console> line 3: math domain error # 

import random

rand = random.randint(1,20)



cod = math.acos(rand)

# Error: line 1: ValueError: file <maya console> line 1: math domain error # 

import math

cod = math.acos(rand)

# Error: line 1: ValueError: file <maya console> line 2: math domain error # 

rand = random.randint(1,20)

cod = math.acos(rand)

# Error: line 1: ValueError: file <maya console> line 2: math domain error # 

x = cmds.polyCube()

print x

[u'pCube1', u'polyCube1']

x.translate(1.0,rand,0.0,0.0)

# Error: line 1: AttributeError: file <maya console> line 1: 'list' object has no attribute 'translate' # 

help('x')

no Python documentation found for 'x'



run = random.randint(1,10)

cmds.polyCreateFacet( p=[(0, run, 0), (0, -2, run), (run, -2, 0), (run, 2, 0)] )

cmds.polyPlane( n=’plg’, w=10, h=10 )



# Error: line 1: invalid syntax # 

cmds.move( 0, 0, 10, r=True )

cmds.move( 0, 0, -10, r=True )

cmds.polyCut( ‘pCylA.f[0:59]‘, cd=’Y', ch=1 )

# Error: line 1: invalid syntax # 

cmds.polyCut()

# Result: [u'polyCut1'] # 

x = 1 

if x = &gt; 10:    
    cmds.polyCut()
    x + 1
# Error: line 1: invalid syntax # 

x = 1 

if x =&gt; 10:    
    cmds.polyCut()
    x + 1
# Error: line 1: invalid syntax # 

x = 1 

if x =&gt; 10:
    cmds.polyCut()
    x + 1
# Error: line 1: invalid syntax # 

var1 = 100

if var1:
    print('testing123')
    print var1
else:
    print('no') 
testing123

100

if x = 20:
    print('hello')
    x + 1
# Error: line 1: invalid syntax # 

if x = 20:
    print('hello')
x + 1

# Error: line 1: invalid syntax # 

if x = 20:
    print('hello')
    x + 1
else:
    break
# Error: line 1: invalid syntax # 

x=1

if x = 20:
    print('hello')
    x + 1
else:
    break
# Error: line 1: invalid syntax # 

x=1

if x &gt;= 20:
    print('hello')
    x + 1
else:
    break
# Error: line 1: 'break' outside loop # 

if x &gt;= 20:
    print('hello')
    x + 1
if x &gt;= 20:
    print('hello')
    x + 1


def togVis(obj):
    cmds.setAttr (obj+'.visibility',
    not cmds.getAttr(obj+'.visibility'))
    toggleVisibility('pCube1')
print togVis

<function togvis at>

togVis

# Result: <function togvis at> # 

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print n, 'equals', x', '*', n/x
            break
    else:
        print n, 'is a prime number'
# Error: line 1: invalid syntax # 

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print n, 'equals', 'x', '*', n/x
            break
    else:
        print n, 'is a prime number'
2 is a prime number

3 is a prime number

4 equals x * 2

5 is a prime number

6 equals x * 3

7 is a prime number

8 equals x * 4

9 equals x * 3

teste = raw_input('name')



cmds.group(em=True,name=teste)

namedef dolt():
    cmds.group(em=True,name=(cmds.textField('userInput',q=True,
    tx=True)))
    
    cmds.window()
    
    cmds.columnLayout(adj=True)
    cmds.textField('userinput')
    cmds.button(l='group',c='dolt()')
    cmds.showWindow
dolt

# Result: <function dolt at> # 

print dolt()

# Error: line 1: RuntimeError: file <maya console> line 3: Object 'userInput' not found. # 

def createMaterial(name,color,type):
    cmds.sets(renderable=True, noSurfaceShader=True,
    empty=True, name=name + 'SG')
    
    cmds.shadingNode(type, asShader=True, name=name)
    
    cmds.setAttr(name+'.color',color[0],color[1],color[2],
    type='double3')
    cmds.connectAttr(name+'.outColor',
    name+'SG.surfaceShader')
def assignMaterial(name,object):
    cmds.sets(object,edit=True, forceElement=name+'SG')
def createCube():
    cmds.polyCube()
createCube()

cmds.polyBevel

# Result: <built-in method polybevel of module object at> # 

cmds.split()

# Error: line 1: AttributeError: file <maya console> line 1: 'module' object has no attribute 'split' # 

cmds.polySplit()

# Error: line 1: RuntimeError: file <maya console> line 1: Need at least one "-ep" or "-ip" flag (edge split point). # 

cmds.polyAppend( a=[0, (5, -5, 0)] )



# Warning: Can't perform polyAppend1 on selection # 

# Result: [u'polyAppend1'] # 

cmds.polyAppend( a=[0, (5, 5, 0)] )



# Warning: Can't perform polyAppend2 on selection # 

# Result: [u'polyAppend2'] # 

cmds.scale( 2, 2, 2 )

s = lambda x,y: x-y

print s

<function> at 0x0000000034B175F8&gt;

print s(ran,10)

# Error: line 1: NameError: file <maya console> line 1: name 'ran' is not defined # 

print s(22,10)

12

cmds.polyPlane( sx=3, sy=3 )

# Result: [u'pPlane1', u'polyPlane1'] # 

ranx = random.randint(3,6)

cmds.polyPlane( sx=ranx, sy=3 )

cmds.polyExtrudeFacet()

# Result: [u'polyExtrudeFace1'] # 

cmds.polyExtrudeFacet()

cmds.move(0,4,0)

def extrudenow:
    cmds.poyExtrudeFacet()
    cmds.move(0,2,0)
# Error: line 1: invalid syntax # 

def extrudenow:
    cmds.poyExtrudeFacet()
    cmds.move(0,2,0)
# Error: line 1: invalid syntax # 

def extrudenow:
    cmds.polyExtrudeFacet()
    cmds.move(0,2,0)
# Error: line 1: invalid syntax # 

def extrudenow():
    cmds.polyExtrudeFacet()
    cmds.move(0,2,0)
extrudeNow()

# Error: line 1: NameError: file <maya console> line 1: name 'extrudeNow' is not defined # 

extrudenow()

cmds..translate(1.0,2.5,0.0,0.0)

# Error: line 1: invalid syntax # 

cmds.translate(1.0,2.5,0.0,0.0)

# Error: line 1: AttributeError: file <maya console> line 1: 'module' object has no attribute 'translate' # 

import json

help('json')

Help on package json:



NAME
    json


FILE
    c:\python27\lib\json\__init__.py


DESCRIPTION
    JSON (JavaScript Object Notation) <http:> is a subset of
    JavaScript syntax (ECMA-262 3rd edition) used as a lightweight data
    interchange format.
    
    :mod:`json` exposes an API familiar to users of the standard library
    :mod:`marshal` and :mod:`pickle` modules. It is the externally maintained
    version of the :mod:`json` library contained in Python 2.6, but maintains
    compatibility with Python 2.4 and Python 2.5 and (currently) has
    significant performance advantages, even without using the optional C
    extension for speedups.
    
    Encoding basic Python object hierarchies::
    
        &gt;&gt;&gt; import json
        &gt;&gt;&gt; json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
        '["foo", {"bar": ["baz", null, 1.0, 2]}]'
        &gt;&gt;&gt; print json.dumps("\"foo\bar")
        "\"foo\bar"
        &gt;&gt;&gt; print json.dumps(u'\u1234')
        "\u1234"
        &gt;&gt;&gt; print json.dumps('\\')
        "\\"
        &gt;&gt;&gt; print json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True)
        {"a": 0, "b": 0, "c": 0}
        &gt;&gt;&gt; from StringIO import StringIO
        &gt;&gt;&gt; io = StringIO()
        &gt;&gt;&gt; json.dump(['streaming API'], io)
        &gt;&gt;&gt; io.getvalue()
        '["streaming API"]'
    
    Compact encoding::
    
        &gt;&gt;&gt; import json
        &gt;&gt;&gt; json.dumps([1,2,3,{'4': 5, '6': 7}], separators=(',',':'))
        '[1,2,3,{"4":5,"6":7}]'
    
    Pretty printing::
    
        &gt;&gt;&gt; import json
        &gt;&gt;&gt; s = json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4)
        &gt;&gt;&gt; print '\n'.join([l.rstrip() for l in  s.splitlines()])
        {
            "4": 5,
            "6": 7
        }
    
    Decoding JSON::
    
        &gt;&gt;&gt; import json
        &gt;&gt;&gt; obj = [u'foo', {u'bar': [u'baz', None, 1.0, 2]}]
        &gt;&gt;&gt; json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]') == obj
        True
        &gt;&gt;&gt; json.loads('"\\"foo\\bar"') == u'"foo\x08ar'
        True
        &gt;&gt;&gt; from StringIO import StringIO
        &gt;&gt;&gt; io = StringIO('["streaming API"]')
        &gt;&gt;&gt; json.load(io)[0] == 'streaming API'
        True
    
    Specializing JSON object decoding::
    
        &gt;&gt;&gt; import json
        &gt;&gt;&gt; def as_complex(dct):
        ...     if '__complex__' in dct:
        ...         return complex(dct['real'], dct['imag'])
        ...     return dct
        ...
        &gt;&gt;&gt; json.loads('{"__complex__": true, "real": 1, "imag": 2}',
        ...     object_hook=as_complex)
        (1+2j)
        &gt;&gt;&gt; from decimal import Decimal
        &gt;&gt;&gt; json.loads('1.1', parse_float=Decimal) == Decimal('1.1')
        True
    
    Specializing JSON object encoding::
    
        &gt;&gt;&gt; import json
        &gt;&gt;&gt; def encode_complex(obj):
        ...     if isinstance(obj, complex):
        ...         return [obj.real, obj.imag]
        ...     raise TypeError(repr(o) + " is not JSON serializable")
        ...
        &gt;&gt;&gt; json.dumps(2 + 1j, default=encode_complex)
        '[2.0, 1.0]'
        &gt;&gt;&gt; json.JSONEncoder(default=encode_complex).encode(2 + 1j)
        '[2.0, 1.0]'
        &gt;&gt;&gt; ''.join(json.JSONEncoder(default=encode_complex).iterencode(2 + 1j))
        '[2.0, 1.0]'
    
    
    Using json.tool from the shell to validate and pretty-print::
    
        $ echo '{"json":"obj"}' | python -m json.tool
        {
            "json": "obj"
        }
        $ echo '{ 1.2:3.4}' | python -m json.tool
        Expecting property name: line 1 column 2 (char 2)


PACKAGE CONTENTS
    decoder
    encoder
    scanner
    tests (package)
    tool


CLASSES
    __builtin__.object
        json.decoder.JSONDecoder
        json.encoder.JSONEncoder
    
    class JSONDecoder(__builtin__.object)
     |  Simple JSON <http:> decoder
     |  
     |  Performs the following translations in decoding by default:
     |  
     |  +---------------+-------------------+
     |  | JSON          | Python            |
     |  +===============+===================+
     |  | object        | dict              |
     |  +---------------+-------------------+
     |  | array         | list              |
     |  +---------------+-------------------+
     |  | string        | unicode           |
     |  +---------------+-------------------+
     |  | number (int)  | int, long         |
     |  +---------------+-------------------+
     |  | number (real) | float             |
     |  +---------------+-------------------+
     |  | true          | True              |
     |  +---------------+-------------------+
     |  | false         | False             |
     |  +---------------+-------------------+
     |  | null          | None              |
     |  +---------------+-------------------+
     |  
     |  It also understands ``NaN``, ``Infinity``, and ``-Infinity`` as
     |  their corresponding ``float`` values, which is outside the JSON spec.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, encoding=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, strict=True, object_pairs_hook=None)
     |      ``encoding`` determines the encoding used to interpret any ``str``
     |      objects decoded by this instance (utf-8 by default).  It has no
     |      effect when decoding ``unicode`` objects.
     |      
     |      Note that currently only encodings that are a superset of ASCII work,
     |      strings of other encodings should be passed in as ``unicode``.
     |      
     |      ``object_hook``, if specified, will be called with the result
     |      of every JSON object decoded and its return value will be used in
     |      place of the given ``dict``.  This can be used to provide custom
     |      deserializations (e.g. to support JSON-RPC class hinting).
     |      
     |      ``object_pairs_hook``, if specified will be called with the result of
     |      every JSON object decoded with an ordered list of pairs.  The return
     |      value of ``object_pairs_hook`` will be used instead of the ``dict``.
     |      This feature can be used to implement custom decoders that rely on the
     |      order that the key and value pairs are decoded (for example,
     |      collections.OrderedDict will remember the order of insertion). If
     |      ``object_hook`` is also defined, the ``object_pairs_hook`` takes
     |      priority.
     |      
     |      ``parse_float``, if specified, will be called with the string
     |      of every JSON float to be decoded. By default this is equivalent to
     |      float(num_str). This can be used to use another datatype or parser
     |      for JSON floats (e.g. decimal.Decimal).
     |      
     |      ``parse_int``, if specified, will be called with the string
     |      of every JSON int to be decoded. By default this is equivalent to
     |      int(num_str). This can be used to use another datatype or parser
     |      for JSON integers (e.g. float).
     |      
     |      ``parse_constant``, if specified, will be called with one of the
     |      following strings: -Infinity, Infinity, NaN.
     |      This can be used to raise an exception if invalid JSON numbers
     |      are encountered.
     |      
     |      If ``strict`` is false (true is the default), then control
     |      characters will be allowed inside strings.  Control characters in
     |      this context are those with character codes in the 0-31 range,
     |      including ``'\t'`` (tab), ``'\n'``, ``'\r'`` and ``'\0'``.
     |  
     |  decode(self, s, _w=<built-in method match of _sre.sre_pattern object>)
     |      Return the Python representation of ``s`` (a ``str`` or ``unicode``
     |      instance containing a JSON document)
     |  
     |  raw_decode(self, s, idx=0)
     |      Decode a JSON document from ``s`` (a ``str`` or ``unicode``
     |      beginning with a JSON document) and return a 2-tuple of the Python
     |      representation and the index in ``s`` where the document ended.
     |      
     |      This can be used to decode a JSON document from a string that may
     |      have extraneous data at the end.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class JSONEncoder(__builtin__.object)
     |  Extensible JSON <http:> encoder for Python data structures.
     |  
     |  Supports the following objects and types by default:
     |  
     |  +-------------------+---------------+
     |  | Python            | JSON          |
     |  +===================+===============+
     |  | dict              | object        |
     |  +-------------------+---------------+
     |  | list, tuple       | array         |
     |  +-------------------+---------------+
     |  | str, unicode      | string        |
     |  +-------------------+---------------+
     |  | int, long, float  | number        |
     |  +-------------------+---------------+
     |  | True              | true          |
     |  +-------------------+---------------+
     |  | False             | false         |
     |  +-------------------+---------------+
     |  | None              | null          |
     |  +-------------------+---------------+
     |  
     |  To extend this to recognize other objects, subclass and implement a
     |  ``.default()`` method with another method that returns a serializable
     |  object for ``o`` if possible, otherwise it should call the superclass
     |  implementation (to raise ``TypeError``).
     |  
     |  Methods defined here:
     |  
     |  __init__(self, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, sort_keys=False, indent=None, separators=None, encoding='utf-8', default=None)
     |      Constructor for JSONEncoder, with sensible defaults.
     |      
     |      If skipkeys is false, then it is a TypeError to attempt
     |      encoding of keys that are not str, int, long, float or None.  If
     |      skipkeys is True, such items are simply skipped.
     |      
     |      If ensure_ascii is true, the output is guaranteed to be str
     |      objects with all incoming unicode characters escaped.  If
     |      ensure_ascii is false, the output will be unicode object.
     |      
     |      If check_circular is true, then lists, dicts, and custom encoded
     |      objects will be checked for circular references during encoding to
     |      prevent an infinite recursion (which would cause an OverflowError).
     |      Otherwise, no such check takes place.
     |      
     |      If allow_nan is true, then NaN, Infinity, and -Infinity will be
     |      encoded as such.  This behavior is not JSON specification compliant,
     |      but is consistent with most JavaScript based encoders and decoders.
     |      Otherwise, it will be a ValueError to encode such floats.
     |      
     |      If sort_keys is true, then the output of dictionaries will be
     |      sorted by key; this is useful for regression tests to ensure
     |      that JSON serializations can be compared on a day-to-day basis.
     |      
     |      If indent is a non-negative integer, then JSON array
     |      elements and object members will be pretty-printed with that
     |      indent level.  An indent level of 0 will only insert newlines.
     |      None is the most compact representation.
     |      
     |      If specified, separators should be a (item_separator, key_separator)
     |      tuple.  The default is (', ', ': ').  To get the most compact JSON
     |      representation you should specify (',', ':') to eliminate whitespace.
     |      
     |      If specified, default is a function that gets called for objects
     |      that can't otherwise be serialized.  It should return a JSON encodable
     |      version of the object or raise a ``TypeError``.
     |      
     |      If encoding is not None, then all input strings will be
     |      transformed into unicode using that encoding prior to JSON-encoding.
     |      The default is UTF-8.
     |  
     |  default(self, o)
     |      Implement this method in a subclass such that it returns
     |      a serializable object for ``o``, or calls the base implementation
     |      (to raise a ``TypeError``).
     |      
     |      For example, to support arbitrary iterators, you could
     |      implement default like this::
     |      
     |          def default(self, o):
     |              try:
     |                  iterable = iter(o)
     |              except TypeError:
     |                  pass
     |              else:
     |                  return list(iterable)
     |              return JSONEncoder.default(self, o)
     |  
     |  encode(self, o)
     |      Return a JSON string representation of a Python data structure.
     |      
     |      &gt;&gt;&gt; JSONEncoder().encode({"foo": ["bar", "baz"]})
     |      '{"foo": ["bar", "baz"]}'
     |  
     |  iterencode(self, o, _one_shot=False)
     |      Encode the given object and yield each string
     |      representation as available.
     |      
     |      For example::
     |      
     |          for chunk in JSONEncoder().iterencode(bigobject):
     |              mysocket.write(chunk)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  item_separator = ', '
     |  
     |  key_separator = ': '


FUNCTIONS
    dump(obj, fp, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, encoding='utf-8', default=None, **kw)
        Serialize ``obj`` as a JSON formatted stream to ``fp`` (a
        ``.write()``-supporting file-like object).
        
        If ``skipkeys`` is true then ``dict`` keys that are not basic types
        (``str``, ``unicode``, ``int``, ``long``, ``float``, ``bool``, ``None``)
        will be skipped instead of raising a ``TypeError``.
        
        If ``ensure_ascii`` is false, then the some chunks written to ``fp``
        may be ``unicode`` instances, subject to normal Python ``str`` to
        ``unicode`` coercion rules. Unless ``fp.write()`` explicitly
        understands ``unicode`` (as in ``codecs.getwriter()``) this is likely
        to cause an error.
        
        If ``check_circular`` is false, then the circular reference check
        for container types will be skipped and a circular reference will
        result in an ``OverflowError`` (or worse).
        
        If ``allow_nan`` is false, then it will be a ``ValueError`` to
        serialize out of range ``float`` values (``nan``, ``inf``, ``-inf``)
        in strict compliance of the JSON specification, instead of using the
        JavaScript equivalents (``NaN``, ``Infinity``, ``-Infinity``).
        
        If ``indent`` is a non-negative integer, then JSON array elements and
        object members will be pretty-printed with that indent level. An indent
        level of 0 will only insert newlines. ``None`` is the most compact
        representation.
        
        If ``separators`` is an ``(item_separator, dict_separator)`` tuple
        then it will be used instead of the default ``(', ', ': ')`` separators.
        ``(',', ':')`` is the most compact JSON representation.
        
        ``encoding`` is the character encoding for str instances, default is UTF-8.
        
        ``default(obj)`` is a function that should return a serializable version
        of obj or raise TypeError. The default simply raises TypeError.
        
        To use a custom ``JSONEncoder`` subclass (e.g. one that overrides the
        ``.default()`` method to serialize additional types), specify it with
        the ``cls`` kwarg; otherwise ``JSONEncoder`` is used.
    
    dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, encoding='utf-8', default=None, **kw)
        Serialize ``obj`` to a JSON formatted ``str``.
        
        If ``skipkeys`` is false then ``dict`` keys that are not basic types
        (``str``, ``unicode``, ``int``, ``long``, ``float``, ``bool``, ``None``)
        will be skipped instead of raising a ``TypeError``.
        
        If ``ensure_ascii`` is false, then the return value will be a
        ``unicode`` instance subject to normal Python ``str`` to ``unicode``
        coercion rules instead of being escaped to an ASCII ``str``.
        
        If ``check_circular`` is false, then the circular reference check
        for container types will be skipped and a circular reference will
        result in an ``OverflowError`` (or worse).
        
        If ``allow_nan`` is false, then it will be a ``ValueError`` to
        serialize out of range ``float`` values (``nan``, ``inf``, ``-inf``) in
        strict compliance of the JSON specification, instead of using the
        JavaScript equivalents (``NaN``, ``Infinity``, ``-Infinity``).
        
        If ``indent`` is a non-negative integer, then JSON array elements and
        object members will be pretty-printed with that indent level. An indent
        level of 0 will only insert newlines. ``None`` is the most compact
        representation.
        
        If ``separators`` is an ``(item_separator, dict_separator)`` tuple
        then it will be used instead of the default ``(', ', ': ')`` separators.
        ``(',', ':')`` is the most compact JSON representation.
        
        ``encoding`` is the character encoding for str instances, default is UTF-8.
        
        ``default(obj)`` is a function that should return a serializable version
        of obj or raise TypeError. The default simply raises TypeError.
        
        To use a custom ``JSONEncoder`` subclass (e.g. one that overrides the
        ``.default()`` method to serialize additional types), specify it with
        the ``cls`` kwarg; otherwise ``JSONEncoder`` is used.
    
    load(fp, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
        Deserialize ``fp`` (a ``.read()``-supporting file-like object containing
        a JSON document) to a Python object.
        
        If the contents of ``fp`` is encoded with an ASCII based encoding other
        than utf-8 (e.g. latin-1), then an appropriate ``encoding`` name must
        be specified. Encodings that are not ASCII based (such as UCS-2) are
        not allowed, and should be wrapped with
        ``codecs.getreader(fp)(encoding)``, or simply decoded to a ``unicode``
        object and passed to ``loads()``
        
        ``object_hook`` is an optional function that will be called with the
        result of any object literal decode (a ``dict``). The return value of
        ``object_hook`` will be used instead of the ``dict``. This feature
        can be used to implement custom decoders (e.g. JSON-RPC class hinting).
        
        ``object_pairs_hook`` is an optional function that will be called with the
        result of any object literal decoded with an ordered list of pairs.  The
        return value of ``object_pairs_hook`` will be used instead of the ``dict``.
        This feature can be used to implement custom decoders that rely on the
        order that the key and value pairs are decoded (for example,
        collections.OrderedDict will remember the order of insertion). If
        ``object_hook`` is also defined, the ``object_pairs_hook`` takes priority.
        
        To use a custom ``JSONDecoder`` subclass, specify it with the ``cls``
        kwarg; otherwise ``JSONDecoder`` is used.
    
    loads(s, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
        Deserialize ``s`` (a ``str`` or ``unicode`` instance containing a JSON
        document) to a Python object.
        
        If ``s`` is a ``str`` instance and is encoded with an ASCII based encoding
        other than utf-8 (e.g. latin-1) then an appropriate ``encoding`` name
        must be specified. Encodings that are not ASCII based (such as UCS-2)
        are not allowed and should be decoded to ``unicode`` first.
        
        ``object_hook`` is an optional function that will be called with the
        result of any object literal decode (a ``dict``). The return value of
        ``object_hook`` will be used instead of the ``dict``. This feature
        can be used to implement custom decoders (e.g. JSON-RPC class hinting).
        
        ``object_pairs_hook`` is an optional function that will be called with the
        result of any object literal decoded with an ordered list of pairs.  The
        return value of ``object_pairs_hook`` will be used instead of the ``dict``.
        This feature can be used to implement custom decoders that rely on the
        order that the key and value pairs are decoded (for example,
        collections.OrderedDict will remember the order of insertion). If
        ``object_hook`` is also defined, the ``object_pairs_hook`` takes priority.
        
        ``parse_float``, if specified, will be called with the string
        of every JSON float to be decoded. By default this is equivalent to
        float(num_str). This can be used to use another datatype or parser
        for JSON floats (e.g. decimal.Decimal).
        
        ``parse_int``, if specified, will be called with the string
        of every JSON int to be decoded. By default this is equivalent to
        int(num_str). This can be used to use another datatype or parser
        for JSON integers (e.g. float).
        
        ``parse_constant``, if specified, will be called with one of the
        following strings: -Infinity, Infinity, NaN, null, true, false.
        This can be used to raise an exception if invalid JSON numbers
        are encountered.
        
        To use a custom ``JSONDecoder`` subclass, specify it with the ``cls``
        kwarg; otherwise ``JSONDecoder`` is used.


DATA
    __all__ = ['dump', 'dumps', 'load', 'loads', 'JSONDecoder', 'JSONEncod...
    __author__ = 'Bob Ippolito <bob>'
    __version__ = '2.0.9'


VERSION
    2.0.9


AUTHOR
    Bob Ippolito <bob>




import requests

# Error: line 1: ImportError: file <maya console> line 1: No module named requests # 

import urllib2

# Error: line 1: ImportError: file C:\Python27\Lib\socket.py line 47: DLL load failed: %1 is not a valid Win32 application. # 

import urllib

# Error: line 1: ImportError: file C:\Python27\Lib\socket.py line 47: DLL load failed: %1 is not a valid Win32 application. # 

cmds.polyCreateFacet( p=[(0, 0, 0), (10, 0, 0), (10, 10, 0), (0, 10, 0)] )

# Result: [u'polySurface2', u'polyCreateFace2'] # 

cmds.polySplit(3,3,3)

# Error: line 1: ValueError: file <maya console> line 1: No object matches name: 3 # 

cmds.polySplit()

# Error: line 1: RuntimeError: file <maya console> line 1: Need at least one "-ep" or "-ip" flag (edge split point). # 

cmds.polySplit()

# Error: line 1: RuntimeError: file <maya console> line 1: Need at least one "-ep" or "-ip" flag (edge split point). # 

cmds.polyCreateFacet( p=[(0, 2, 0), (0, -2, 0), (4, -2, 0), (4, 2, 0)] )

cmds.polySplit( ip=[(2, 0.1), (3, 0.5), (0, 2, -1, 0.0), (0, 0.9)] )



lisx = []

for i in range (10):
    lisx.append(random.randrange(1,101,1))
    print lisx
[21]

[21, 84]

[21, 84, 11]

[21, 84, 11, 99]

[21, 84, 11, 99, 7]

[21, 84, 11, 99, 7, 31]

[21, 84, 11, 99, 7, 31, 59]

[21, 84, 11, 99, 7, 31, 59, 5]

[21, 84, 11, 99, 7, 31, 59, 5, 22]

[21, 84, 11, 99, 7, 31, 59, 5, 22, 79]

lisx = []

for i in range (10):
    lisx.append(random.randrange(1,101,1))
print lisx

[80, 85, 86, 89, 45, 60, 55, 39, 54, 96]

shuLisx = random.shuffle(lisx)

print shuLisx

None

print lisx

[54, 89, 55, 85, 39, 80, 60, 86, 45, 96]

random.shuffle(lisx)

print random.shuffle(lisx)

None

lisx = []

for i in range (10):
    lisx.append(random.randrange(1,101,1))
    random.shuffle(lisx)
print lisx

[9, 5, 45, 52, 9, 21, 8, 43, 32, 93]

cmds.polyCube(5,5,5)

# Error: line 1: ValueError: file <maya console> line 1: No object matches name: 5 # 

cmds.polyCube()

# Result: [u'pCube3', u'polyCube3'] # 

help('cmds')

no Python documentation found for 'cmds'



import pip

# Error: line 1: ImportError: file <maya console> line 1: No module named pip # 

python

# Error: line 1: NameError: file <maya console> line 1: name 'python' is not defined # 

import sys

import maya.OpenMaya as OpenMaya

import maya.OpenMayaPx as OpenMayaPx

# Error: line 1: ImportError: file <maya console> line 2: No module named OpenMayaPx # 

import maya.OpenMaya as OpenMaya



import maya.OpenMayaMPx as OpenMayaMPx



kPluginCmdName = "spHelloWorld"



class scriptedCommand(OpenMayaMPx.MPxCommand):
    def __init__(self):
        OpenMayaMPx.MPxCommand.__init__(self)

    # Invoked when the command is run.
    def doIt(self,argList):
        print "Hello World!"


# Creator

def cmdCreator():
    return OpenMayaMPx.asMPxPtr( scriptedCommand() )


# Initialize the script plug-in

def initializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.registerCommand( kPluginCmdName, cmdCreator )
    except:
        sys.stderr.write( "Failed to register command: %s\n" % kPluginCmdName )
        raise


# Uninitialize the script plug-in

def uninitializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.deregisterCommand( kPluginCmdName )
    except:
        sys.stderr.write( "Failed to unregister command: %s\n" % kPluginCmdName )
(u"C:/Users/Luke/Documents/maya/2014-x64/prefs/scriptEditorTemp/myFirstPlugin.py").replace("\\","/");

# Result: C:/Users/Luke/Documents/maya/2014-x64/prefs/scriptEditorTemp/myFirstPlugin.py # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/AbcExport.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/AbcExport.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/AbcImport.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/AbcImport.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/ArubaTessellator.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/ArubaTessellator.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/AutodeskPacketFile.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/AutodeskPacketFile.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/DirectConnect.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/DirectConnect.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/Fur.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/Fur.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/MayaMuscle.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/MayaMuscle.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/OneClick.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/OneClick.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/OpenEXRLoader.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/OpenEXRLoader.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/Turtle.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/Turtle.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/VectorRender.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/VectorRender.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/animImportExport.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/animImportExport.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/atomImportExport.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/atomImportExport.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/autoLoader.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/autoLoader.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/bullet.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/bullet.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/cgfxShader.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/cgfxShader.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/cleanPerFaceAssignment.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/cleanPerFaceAssignment.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/clearcoat.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/clearcoat.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/ddsFloatReader.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/ddsFloatReader.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/dgProfiler.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/dgProfiler.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/dx11Shader.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/dx11Shader.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/fbxmaya.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/fbxmaya.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/fltTranslator.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/fltTranslator.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/ge2Export.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/ge2Export.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/gpuCache.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/gpuCache.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/hlslShader.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/hlslShader.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/ik2Bsolver.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/ik2Bsolver.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/ikSpringSolver.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/ikSpringSolver.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/matrixNodes.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/matrixNodes.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/mayaCharacterization.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/mayaCharacterization.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/mayaHIK.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/mayaHIK.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/melProfiler.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/melProfiler.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/modelingToolkit.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/modelingToolkit.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/nearestPointOnMesh.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/nearestPointOnMesh.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/objExport.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/objExport.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/openInventor.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/openInventor.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/quatNodes.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/quatNodes.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/retargeterNodes.py").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/retargeterNodes.py # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/rotateHelper.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/rotateHelper.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/rtgExport.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/rtgExport.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/sceneAssembly.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/sceneAssembly.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/stereoCamera.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/stereoCamera.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/studioImport.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/studioImport.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/testExamples.nll.dll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/testExamples.nll.dll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/tiffFloatReader.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/tiffFloatReader.mll # 

(u"C:/Program Files/Autodesk/Maya2014/bin/plug-ins/vrml2Export.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/bin/plug-ins/vrml2Export.mll # 

(u"C:/Program Files/Autodesk/mentalrayForMaya2014/plug-ins/Mayatomr.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/mentalrayForMaya2014/plug-ins/Mayatomr.mll # 

(u"C:/Program Files/Autodesk/Maya2014/substance/plug-ins/Substance.mll").replace("\\","/");

# Result: C:/Program Files/Autodesk/Maya2014/substance/plug-ins/Substance.mll # 

cmds.polyCube()

# Result: [u'pCube4', u'polyCube4'] # 

cmds.select('pCube4.e[0,31]')

cmds.polySplitRing(sma=180, wt=0.2)

# Error: line 1: TypeError: file <maya console> line 1: Object pCube4.e[0,31] is invalid # 

cmds.select('pCube4.e[0,31]')

# Error: line 1: TypeError: file <maya console> line 1: Object pCube4.e[0,31] is invalid # 

cmds.select('pCube1.e[0:3]')



cmds.polySplitRing( sma=180, wt=0.2)



# Result: [u'polySplitRing1'] # 

spiRan = random.choice(lisx)

cmds.polySplitRing( sma=180, wt=0.2)



# Warning: Can't perform polySplitRing2 on selection # 

cmds.select('pCube4.e[0,3]')



# Error: line 1: TypeError: file <maya console> line 1: Object pCube4.e[0,3] is invalid # 

cmds.polySplitRing( sma=180, wt=0.2)

# Warning: Can't perform polySplitRing3 on selection # 

# Result: [u'polySplitRing3'] # 

cmds.polyCube( n='plg', w=5, h=5, d=5 )



# Result: [u'plg', u'polyCube5'] # 

cmds.scale( 2, 2, 2 )



cmds.select( 'plg' )



cmds.polyOptions( ao=True, dv='true' )



# Error: line 1: TypeError: file <maya console> line 1: Invalid arguments for flag 'dv'.  Expected int, got str # 

cmds.polySubdivideEdge( dv=4 )



# Result: [u'polySubdEdge1'] # 

cmds.polySubdivideEdge( dv=4, s=1.5 )



# Result: [u'polySubdEdge2'] # 

cmds.polySubdivideEdge( dv=4, s=2, ws=True )



# Error: line 1: TypeError: file <maya console> line 1: Error retrieving default arguments # 

cmds.polySubdivideEdge( dv=4, s=2, ws=True )



# Result: [u'polySubdEdge3'] # 

cmds.polyPlane( name='p', ch=False )

# Result: [u'p'] # 

cmds.select(n='p')

# Error: line 1: TypeError: file <maya console> line 1: Invalid flag 'n' # 

cmds.select('p')

cmds.select('p')

cmds.select('p')

cmds.dataStructure( format='raw', asString='name=IdStruct:int32=ID' )



# Result: IdStruct # 

cmds.dataStructure( format='raw', asString='name=OffStruct:float=Offset' )



# Result: OffStruct # 

cmds.dataStructure( format='raw', asString='name=OrgStruct:float[3]=Origin Point' )



# Result: OrgStruct # 

cmds.addMetadata( query=True, channelType=True )



# Warning: The 'channelType' flag is obsolete. Use 'channelName' instead. # 

# Error: line 1: RuntimeError: file <maya console> line 1: Query mode only works with exactly one node selected or using the 'scene' flag. # 

cmds.select('p')

cmds.addMetadata( query=True, channelType=True )



# Warning: The 'channelType' flag is obsolete. Use 'channelName' instead. # 

cmds.addMetadata( query=True, channelName=True )



cmds.addMetadata( channelType='vertex', streamName='OffStream', query=True, structure=True )



# Warning: The 'channelType' flag is obsolete. Use 'channelName' instead. # 

cmds.addMetadata( channelName='vertex', streamName='OffStream', query=True, structure=True )



cmds.addMetadata( channelType='vertex', query=True, streamName=True )



# Warning: The 'channelType' flag is obsolete. Use 'channelName' instead. # 

cmds.addMetadata( query=True, streamName=True )



for stream in streams:
	indexType = cmds.addMetadata( channelType='vertex', streamName=stream, query=True, indexType=True )[0]
	print 'Index type on %s is %s' % (stream, indexType)
# Error: line 1: NameError: file <maya console> line 1: name 'streams' is not defined # 

streams = cmds.addMetadata( channelType='vertex', query=True, streamName=True )



# Warning: The 'channelType' flag is obsolete. Use 'channelName' instead. # 

for stream in streams:
	indexType = cmds.addMetadata( channelType='vertex', streamName=stream, query=True, indexType=True )[0]
	print 'Index type on %s is %s' % (stream, indexType)
	
# Error: line 1: TypeError: file <maya console> line 1: 'NoneType' object is not iterable # 

cmds.polyCreateFacet( p=[(0, 0, 0), (10, 0, 0), (10, 10, 0), (0, 10, 0)] )



# Result: [u'polySurface4', u'polyCreateFace4'] # 

cmds.select('polySurface4')

cmds.polyAppend(a=[0,(5,-5,0])

# Error: line 1: invalid syntax # 

cmds.polyAppend( a=[0, (5, -5, 0)] )



# Warning: Can't perform polyAppend3 on selection # 

# Result: [u'polyAppend3'] # 

currentPanel = cmds.getPanel(withFocus= True)

if currentPanel != '':
	cmds.modelEditor(currentPanel, edit=True, da='smoothShaded', dl='default')
cmds.polySphere(n= 'plg', sx= 15, sy= 10 )

# Error: line 1: RuntimeError: file <maya console> line 3: modelEditor: Object 'scriptEditorPanel1' not found. # 

cmds.polyPlane( sx=3, sy=3, name='polyPlane' )



# Result: [u'polyPlane', u'polyPlane3'] # 

cmds.select('polyPlane')

cmds.polyEvaluate( 'polyPlane', vertex=True )



# Result: 16 # 

(u"C:/Users/Luke/Documents/maya/projects/default/scenes/python.mb").replace("\\","/");

# Result: C:/Users/Luke/Documents/maya/projects/default/scenes/python.mb # 

(u"C:/Users/Luke/Documents/maya/projects/default/scenes/python.mb").replace("\\","/");

# Result: C:/Users/Luke/Documents/maya/projects/default/scenes/python.mb # 

(u"C:/Users/Luke/Documents/maya/projects/default/scenes/python.mb").replace("\\","/");

# Result: C:/Users/Luke/Documents/maya/projects/default/scenes/python.mb # 

cmds.polyCube()

# Result: [u'pCube5', u'polyCube6'] # 

cmds.select('pCube1.e[0:3]')



cmds.polySplitRing( sma=180, wt=0.2)



# Result: [u'polySplitRing4'] # 

cmds.select('pCube1.e[1:2]')



cmds.polySplitRing( sma=180, wt=0.2)



# Warning: Can't perform polySplitRing5 on selection # 

# Result: [u'polySplitRing5'] # 

lenCube = len(lisx)

print lenCube

10

ranNumz = random.randint(0,lenCube)

print ranNumz

3

ranCuca = len('pCube1')

print ranCuca

6

ranFinal = random.randint(0, ranCuca)

print ranFinal

6

cmds.select('pCube1.e[ranNumz:ranFinal]')



# Error: line 1: TypeError: file <maya console> line 1: Object pCube1.e[ranNumz:ranFinal] is invalid # 

cmds.select('pCube1.e[0:ranFinal]')



# Error: line 1: TypeError: file <maya console> line 1: Object pCube1.e[0:ranFinal] is invalid # 

cmds.select('pCube1.e[0:1')



# Error: line 1: TypeError: file <maya console> line 1: Object pCube1.e[0:1 is invalid # 

cmds.select('pCube1.e[0:1]')



cmds.polySplitRing( sma=180, wt=0.2)



# Result: [u'polySplitRing6'] # 

cmds.polyCube()



# Result: [u'pCube6', u'polyCube7'] # 

cmds.select('pCube6.e[0:3]')



import math

seleMath = math.pi

print seleMath

3.14159265359

shoCua = ranFinal - seleMath

print shoCua

2.85840734641

cmds.select('pCube6.e[shoCua:3]')



# Error: line 1: TypeError: file <maya console> line 1: Object pCube6.e[shoCua:3] is invalid # 

cmds.select('pCube6.e[shoCua:3]')



# Error: line 1: TypeError: file <maya console> line 1: Object pCube6.e[shoCua:3] is invalid # 

cmds.select('pCube6.e[0:3]')



cmds.polySplitRing( sma=90, wt=0.8)



# Result: [u'polySplitRing7'] # 

cmds.polySplitRing( sma=180, wt=0.6)



# Warning: Can't perform polySplitRing8 on selection # 

# Result: [u'polySplitRing8'] # 

cmds.select('pCube6.e[0:3]')



cmds.polySplitRing( sma=180, wt=0.6)

# Result: [u'polySplitRing9'] # 

cmds.select('pCube6.e[0:3]')



cmds.polySplitRing( sma=60, wt=0.4)



# Result: [u'polySplitRing10'] # 

cmds.select('pCube6.e[0:2]')



cmds.polySplitRing( sma=60, wt=0.4)



# Result: [u'polySplitRing11'] # 

import time

print ('hello')

time.sleep(5)

print ('world')

hello

world

x = 0



if x = 10:
    print ('I am 10')
else:
    print ('I am not 10')
    x + 1
# Error: line 1: invalid syntax # 

x = 0

if x = 10:
    print ('I am 10')
# Error: line 1: invalid syntax # 

if x = 10:
    print ('I am 10')
# Error: line 1: invalid syntax # 

if x == 10:
    print ('I am 10')
cmds.select('pCube1.e[4:6]')



0.

# Result: 0.0 # 

cmds.polySplitRing( sma=90, wt=0.2)



# Result: [u'polySplitRing12'] # 

cmds.select('pCube1.e[4:6]')



cmds.polySplitRing( sma=180, wt=0.6)



# Warning: Can't perform polySplitRing13 on selection # 

# Result: [u'polySplitRing13'] # 

cmds.polyCylinder( r=1, h=2, sx=20, sy=1, sz=1, ax=(0, 1, 0), cuv=1, ch=1, name='pCylA' )



# Result: [u'pCylA', u'polyCylinder1'] # 

cmds.select('pCylA')

cmds.select('pCylA')

cmds.polyCut( 'pCylA.f[0:59]', cd='Y', ch=1 )



# Result: [u'polyCut2'] # 

cmds.select( cl=True )



cmds.polyCylinder( r=1, h=2, sx=20, sy=1, sz=1, ax=(0, 1, 0), cuv=1, ch=1, name='pCylB' )



# Result: [u'pCylB', u'polyCylinder2'] # 

cmds.move( 3, 0, 0, r=True )



cmds.polyCut( 'pCylB.f[0:59]', cd='Y', df=1, ch=1 )



# Result: [u'polyCut3'] # 

cmds.polyCylinder( r=1, h=2, sx=4, sy=1, sz=1, ax=(0, 1, 0), cuv=1, ch=1, name='pCylB' )



# Result: [u'pCylB1', u'polyCylinder3'] # 

cmds.polyCut( 'pCylB.f[0:30]', cd='Y', df=1, ch=1 )



# Result: [u'polyCut4'] # 

cmds.polyCut( 'pCylB1.f[0:20]', cd='Y', df=1, ch=1 )



# Result: [u'polyCut5'] # 

cmds.polyCut( 'pCylB1.f[-10:0]', cd='Y', df=1, ch=1 )



# Result: [u'polyCut6'] # 

cmds.polyCut( 'pCylB1.f[0:10]', cd='X', df=1, ch=1 )



# Result: [u'polyCut6'] # 

cmds.polyCut( 'pCylB1.f[0:20]', cd='Z', df=1, ch=1 )



# Result: [u'polyCut6'] # 

cmds.polyCut( 'pCylB1.f[5:10]', cd='Z', df=1, ch=1 )



# Result: [u'polyCut6'] # 

cmds.polyCrease( value=0.9 )

# Error: line 1: RuntimeError: file <maya console> line 1: Maya command error # 

cmds.polyCrease( value=0.9 )

cmds.polyPlane( n='plg', w=5, h=5 )

# Result: [u'plg1', u'polyPlane4'] # 

cmds.delete( 'plg.f[20:29]' )



cmds.polyPlane( n='plg', w=5, h=5 )



# Result: [u'plg2', u'polyPlane5'] # 

cmds.delete( 'plg2.f[20:29]' )



cmds.polySelect( 'plg', edgeRing=1 )



# Result: [1, 229] # 

cmds.polySelect('pCube1', edgeRing=[0,50])



# Result: [0] # 

cmds.polySelect( 'plg', toggle=True, edgeRingPath=(1, 10) )



cmds.polySelect( 'plg', toggle=True, edgeRingPath=(1, 10) )



cmds.polySelect( 'pPlane1', shortestEdgePath=(10, 100) )



# Error: line 1: Input vertices are not present on the polygonal object. # 

cmds.polySelect( 'plc', shortestEdgePath=(10, 100) )



# Error: line 1: ValueError: file <maya console> line 1: No object matches name: plc # 

cmds.polySelect( 'plg', shortestEdgePath=(10, 100) )



# Result: [151, 213, 150, 46, 47, 10, 52, 53, 54, 55, 0, 12, 13] # 

cmds.polyPlane( n='plg1', sx=5, sy=5, w=5, h=5 )



# Result: [u'plg3', u'polyPlane6'] # 

cmds.select('plg3')

cmds.move(3,3,3)

cmds.polyMoveVertex( 'plg1.vtx[7]', 'plg1.vtx[10]', 'plg1.vtx[25]', 'plg1.vtx[28]', ltz=1 )



# Result: [u'polyMoveVertex1'] # 

cmds.polyTriangulate( 'plg1.f[0:1]', 'plg1.f[5:6]', 'plg1.f[3:4]', 'plg1.f[8:9]', 'plg1.f[15:16]', 'plg1.f[20:21]', 'plg1.f[18:19]', 'plg1.f[23:24]' )



# Result: [u'polyTriangulate1'] # 

cmds.polyTriangulate( 'plg1.f[0:50]', 'plg1.f[5:50]', 'plg1.f[3:50]', 'plg1.f[8:50]', 'plg1.f[15:50]', 'plg1.f[20:50]', 'plg1.f[18:50]', 'plg1.f[23:50]' )



# Result: [u'polyTriangulate2'] # 

cmds.polyTriangulate()



# Result: [u'polyTriangulate3'] # 

cmds.polyBoolOp()

# Error: line 1: TypeError: file <maya console> line 1: Error retrieving default arguments # 

cmds.polyBoolOp(op=1, n='result1' )

# Error: line 1: TypeError: file <maya console> line 1: Error retrieving default arguments # 

cmds.polyPlane( n='plg', w=10, h=10 )



# Result: [u'plg4', u'polyPlane7'] # 

cmds.polyChipOff( 'plg.f[71:72]', 'plg.f[81:82]', dup=True, ltz=1 )



# Result: [u'polyChipOff1'] # 

cmds.polyChipOff( 'plg.f[11:12]', 'plg.f[21:22]', dup=False, ty=1 )



# Result: [u'polyChipOff2'] # 

cmds.polyChipOff( 'plg.f[15:16]', 'plg.f[23:24]', dup=False, kft=False, ls=(.5, .5, 0) )



# Result: [u'polyChipOff3'] # 

cmds.polyChipOff( 'plg.f[0:74]', 'plg.f[0:84]', dup=False, kft=True, ls=(.5, .5, 0) )



# Result: [u'polyChipOff4'] # 

cmds.polyClipboard( copy=True, uv=True, color=True, shader=True )



# Warning: Incorrect number of items selected. Can only copy attributes from one face component item to the clipboard. # 

# Error: line 1: RuntimeError: file <maya console> line 1: Maya command error # 

cmds.polyClipboard()



# Warning: No action specified to perform with the clipboard. # 

# Error: line 1: RuntimeError: file <maya console> line 1: Maya command error # 

cmds.polyClipboard(copy=True)



# Warning: No attributes specified for clipboard operation. # 

# Error: line 1: RuntimeError: file <maya console> line 1: Maya command error # 

cmds.select( 'plg1.e[26]', 'plg1.e[28]', 'plg1.e[30]', 'plg1.e[32]', 'plg1.e[34]', 'plg1.e[36]', 'plg1.e[38]', 'plg1.e[47]', 'plg1.e[49]', 'plg1.e[51]', 'plg1.e[53]', 'plg1.e[55]', 'plg1.e[57]', 'plg1.e[59]' )





cmds.polyCut(cd='Y', ch=1 )



# Result: [u'polyCut7'] # 

cmds.polyCut(cd='Y', ch=1 )



# Result: [u'polyCut8'] # 

cmds.polyCut( 'pCylA.f[0:59]', cd='Z', ch=1 )



# Result: [u'polyCut9'] # 

cmds.polyCut( 'pCylA.f[0:59]', cd='Z', ch=1 )



# Result: [u'polyCut10'] # 

cmds.select('pCylA')



cmds.select('pCylA')



cmds.polyDuplicateEdge(of=0.5)

# Result: [u'polyDuplicateEdge1'] # 

cmds.polyDuplicateAndConnect

# Result: <built-in method polyduplicateandconnect of module object at> # 

cmds.polyDuplicateAndConnect()

# Result: [u'pCylA1'] # 

cmds.polyDuplicateEdge()

# Result: [u'polyDuplicateEdge2'] # 

cmds.polyDuplicateEdge(e[0,10], of=0.8)

# Error: line 1: NameError: file <maya console> line 1: name 'e' is not defined # 

cmds.select('pCylA')

cmds.select('pCylA1')

cmds.polyExtrudeFacet(kft=False, ltz=2, ls=(.5, .5, 0) )



# Result: [u'polyExtrudeFace5'] # 

cmds.polyExtrudeFacet(kft=False, ltz=.3, ls=(.2, .2, 0) )

# Result: [u'polyExtrudeFace6'] # 

cmds.polyExtrudeFacet(kft=False, ltz=.8, ls=(.5, .5, 0) )



# Result: [u'polyExtrudeFace7'] # 

e, ltz=.3, ls=(.2

# Error: line 1: invalid syntax # 

eFacet(kft

# Error: line 1: invalid syntax # 

cmds.polyExtrudeFacet(kft=False, ltz=.3, ls=(.2, .2, 0) )



# Result: [u'polyExtrudeFace9'] # 

cmds.polyExtrudeFacet(kft=False, ltz=.8, ls=(.2, .2, 0) )



# Result: [u'polyExtrudeFace10'] # 

cmds.polyExtrudeFacet(kft=False, ltz=.5, ls=(.2, .2, 0) )



# Result: [u'polyExtrudeFace10'] # 

cmds.polyExtrudeFacet(kft=False, ltz=.9, ls=(5, .5, 3) )



# Result: [u'polyExtrudeFace10'] # 

3

# Result: 3 # 

cmds.polyExtrudeFacet(kft=False, ltz=.8, ls=(.2, .2, 0) )



# Result: [u'polyExtrudeFace11'] # 

cmds.polyExtrudeFacet(kft=False, ltz=.3, ls=(.2, .2, 0) )



# Result: [u'polyExtrudeFace12'] # 

cmds.polyTriangulate()

# Result: [u'polyTriangulate4'] # 

cmds.scale(0,5,0)

cmds.scale(0.5,0,0)

cmds.scale(50,20,10)



cmds.scale(10,5,10)



cmds.scale(1,1,1)



cmds.scale(1,2,1)



cmds.scale(2,1,1)



cmds.scale(1,1,2)



cmds.scale(1,1,5)



cmds.scale(5,1,1)



cmds.scale(5,5,1)



cmds.scale(1,5,2)



cmds.polySelect(edgeBorder)

# Error: line 1: NameError: file <maya console> line 1: name 'edgeBorder' is not defined # 

cmds.polySelect(edgeBorder=[0,3])

cmds.polySelect(edgeRing=1)

# Result: [1, 38, 42, 8, 16, 19, 11, 58, 54, 3, 22, 26, 1] # 

cmds.polyExtrudeEdge(ch=1, kft=0, pvx=-5.5, pvy=0.0, pvz=6.0 )



# Result: [u'polyExtrudeEdge3'] # 

cmds.move(0, 0, -5, r=True)



cameraName = cmds.camera()



cameraShape = cameraName[1]

focalLength = cmds.camera(cameraShape, q=True, fl=True)



cmds.camera( cameraShape, e=True, ff='overscan' )



cmds.camera(cameraShape, rotation=[90,0,0])

# Error: line 1: RuntimeError: file <maya console> line 1: Too many objects or values. # 

cmds.camera(cameraShape, rotation=90,0,0)

# Error: line 1: non-keyword arg after keyword arg # 

cmds.camera(cameraShape, rotation=90)

# Error: line 1: TypeError: file <maya console> line 1: Invalid arguments for flag 'rotation'.  Expected ( angle, angle, angle ), got int # 

cmds.camera(cameraShape, shutterAngle=90)

# Error: line 1: RuntimeError: file <maya console> line 1: Too many objects or values. # 

cmds.camera(shutterAngle=90)

# Result: [u'camera2', u'cameraShape2'] # 

import mentalray.textureFileConversionUtils

homeName = cmds.cameraView(camera='persp')



cmds.cameraView( homeName, e=True, camera='persp', ab=True )



cmds.dolly( 'persp', distance=-30 )



cmds.panZoom( 'persp', r=0.6 )

cmds.cameraView( panZoomBookmark, e=True, camera='persp', sc=True )



# Error: line 1: NameError: file <maya console> line 1: name 'panZoomBookmark' is not defined # 

cmds.cameraView( panZoomBookmark, e=True, camera='persp', sc=True )



# Error: line 1: NameError: file <maya console> line 1: name 'panZoomBookmark' is not defined # 

cmds.cameraView( camera='persp', name='zoom', ab=True )



# Result: zoom # 

cmds.cameraView( homeName, e=True, camera='persp', sc=True )



cmds.dolly( 'persp', distance=-30 )



cmds.dolly( 'persp', distance=30 )



cmds.roll( 'persp', abs=True, d=0 )



cmds.roll( 'persp', d=90 )



cmds.setKeyframe()

# Error: line 1: TypeError: file <maya console> line 1: Error retrieving default arguments # 

cmds.setKeyframe()

# Result: 10 # 

cmds.currentTime( query=True )



# Result: 1.0 # 

cmds.currentTime( 32, edit=True )



# Result: 32.0 # 

cmds.move(0,5,0)

cmds.setKeyframe()



# Result: 10 # 

cmds.currentTime( 32*2, edit=True )

# Result: 64.0 # 

cmds.currentTime( 0, edit=True )

# Result: 0.0 # 

cmds.copyKey()

# Result: 10 # 

cmds.currentTime( 64, edit=True )



# Result: 64.0 # 

cmds.pasteKey()



# Result: 10 # 

cmds.currentTime( 1, edit=True )

# Result: 1.0 # 

cmds.copyKey()

# Result: 10 # 

cmds.currentTime( 64, edit=True )



# Result: 64.0 # 

cmds.pasteKey()

# Error: line 1: TypeError: file <maya console> line 1: Error retrieving default arguments # 

import time

cmds.recordDevice( device='clock', duration=30 )

# Error: line 1: RuntimeError: file C:\Program Files\Autodesk\Maya2014\Python\lib\site-packages\maya\app\commands.py line 19: No such device: clock # 

cmds.applyTake()

# Error: line 1: RuntimeError: file <maya console> line 1: No devices with recorded takes were found. # 

cmds.joint( p=(0, 0, 0) )

# Result: joint1 # 

cmds.joint( p=(0, 4, 0)  )



# Result: joint2 # 

cmds.joint( 'joint1', e=True, zso=True, oj='xyz' )



cmds.joint( p=(0, 8, -1) )



# Result: joint3 # 

cmds.joint( 'joint2', e=True, zso=True, oj='xyz' )



cmds.joint( lz=('-90deg', '90deg'), p=(0, 8, 4) )



# Result: joint4 # 

cmds.joint( edit=True, lz=('-90deg', '90deg'), lsz=False )



cmds.currentTime( 0 )

cmds.setKeyframe( 'joint3.rx' )

cmds.currentTime( 10 )

cmds.setKeyframe( 'joint3.rx', v=90 )

cmds.currentTime( 20 )

cmds.setKeyframe( 'joint3.rx', v=0 )

cmds.clip( 'arm', startTime=0, endTime=20, name='handWave' )



# Error: line 1: ValueError: file <maya console> line 1: No object matches name: arm # 

cmds.clip(startTime=0, endTime=20, name='handWave' )



# Error: line 1: RuntimeError: file <maya console> line 1: Must select a single character or a clip library. # 

cmds.character( name='arm' )



# Result: arm # 

cmds.clip( 'arm', startTime=0, endTime=20, name='handWave' )



# Error: line 1: RuntimeError: file <maya console> line 1: No clip created since character has no keys. # 



cmds.select( 'joint3', r=True )

cmds.currentTime( 0 )

cmds.setKeyframe( 'joint3.rx' )

cmds.currentTime( 10 )

cmds.setKeyframe( 'joint3.rx', v=90 )

cmds.currentTime( 20 )

cmds.setKeyframe( 'joint3.rx', v=0 )

cmds.clip( 'arm', startTime=0, endTime=20, name='handWave' )



# Error: line 1: RuntimeError: file <maya console> line 1: No clip created since character has no keys. # 

cmds.play( forward=True )



# Press the ESC key to stop playback. # 

cmds.play( state=False )

cmds.select('cameraShape')

# Error: line 1: ValueError: file <maya console> line 1: No object matches name: cameraShape # 

cameraName = cmds.camera()



cameraShape = cameraName[1]



cmds.move(1,0,1)

cmds.setKeyframe()

# Result: 18 # 

light = cmds.ambientLight(intensity=0.8)

cmds.ambientLight( light, e=True, intensity=0.5 )



# Result:  # 

import mentalray.textureFileConversionUtils

import mentalray.textureFileConversionUtils

[/prettify]</maya></maya></maya></maya></maya></maya></maya></maya></maya></maya></maya></maya></maya></maya></maya></built-in></maya></maya></maya></maya></maya></maya></maya></maya></maya></maya></maya></maya></maya></maya></maya></maya></maya></maya></maya></maya></maya></maya></maya></maya></maya></maya></maya></maya></maya></maya></bob></bob></http:></built-in></http:></http:></maya></maya></maya></function></maya></maya></built-in></maya></function></function></function></maya></maya></maya></maya></maya></maya></maya></maya></p></body></html>