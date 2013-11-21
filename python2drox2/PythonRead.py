#!/usr/bin/env python

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import with_statement
import ast

def xml_escape(text):
    from xml.sax.saxutils import escape
    if isinstance(text, bytes):
        try:
            text = text.decode('utf-8')
        except:
            text = text.decode('latin1')
    text = text.replace('\0', '&#0;')
    text = text.replace('\x7f', '&#x7f;')
    for c in range(0, 0x20):
        if c in [0x9, 0xA, 0xD]: continue
        text = text.replace(unichr(c), '&#x'+hex(c)[2:]+';')
    for c in range(0x80, 0xA0):
        text = text.replace(unichr(c), '&#x'+hex(c)[2:]+';')
    return escape(text)

class DroVisitor(ast.NodeVisitor):
    PYTHON_MAJOR_VERSION = 2
    print_function = 2
    unicode_literals = 2

    def __init__(self, comments=None):
        if not comments: comments = []
        self.comments = comments
        super(DroVisitor, self).__init__()

    def visit(self, *args, **kwargs):
        super(DroVisitor, self).visit(*args, **kwargs)

    def visit_comments(self):
        pass

    def visit_comment(self):
        pass

    def emit_symbol(self, cd, name):
        print('<m:csymbol cd="%s">%s</m:csymbol>' % (cd, name))

    def emit_id_as(self, name, asname):
        self.emit_app()
        self.emit_symbol('python2', 'as')
        self.emit_id(name)
        self.emit_id(asname)
        self.emit_app_end()

    def emit_raw_id(self, s):
        print('<m:ci>%s</m:ci>' % s)

    def emit_id(self, s):
        # We go through all possible global identifiers
        # and try to emit something more universal.

        if s == 'abs':
            self.emit_symbol('arith1', 'abs')
        #elif s == 'all':
        #    self.emit_symbol('iter1', 'forall_true')
        #elif s == 'any':
        #    self.emit_symbol('iter1', 'exists_true')
        elif s == 'apply':
            self.emit_symbol('fns2', 'apply_to_list')
        #elif s == 'ascii':
        #    self.emit_symbol('python3', 'ascii')
        #elif s == 'basestring':
        #    self.emit_symbol('python2', 'basestring')
        #elif s == 'bin':
        #    self.emit_symbol('python2', 'bin')
        #elif s == 'bool':
        #    self.emit_symbol('logic5', 'to_boolean')
        #elif s == 'buffer':
        #    self.emit_symbol('python2', 'buffer')
        #elif s == 'bytearray':
        #    self.emit_symbol('mbytes1', 'to_mbytes') # Mutable [Byte]
        #elif s == 'bytes':
        #    self.emit_symbol('bytes1', 'to_bytes') # Imm [Byte]
        #elif s == 'callable':
        #    self.emit_symbol('python2', 'callable')
        #elif s == 'chr':
        #    self.emit_symbol('char1', 'integer_to_character')
        #elif s == 'classmethod':
        #    self.emit_symbol('python2', 'classmethod')
        #elif s == 'cmp':
        #    self.emit_symbol('python2', 'cmp')
        #elif s == 'coerce':
        #    self.emit_symbol('python2', 'coerce')
        #elif s == 'compile':
        #    self.emit_symbol('python2', 'compile')
        elif s == 'complex':
            self.emit_symbol('complex1', 'complex_cartesian')
        #elif s == 'delattr':
        #    self.emit_symbol('python2', 'delattr')
        #elif s == 'dict':
        #    self.emit_symbol('dict5', 'to_dict')
        #elif s == 'dir':
        #    self.emit_symbol('python2', 'dir')
        #elif s == 'divmod':
        #    self.emit_symbol('python2', 'divmod')
        #elif s == 'enumerate':
        #    self.emit_symbol('python2', 'enumerate')
        #elif s == 'eval':
        #    self.emit_symbol('python2', 'eval')
        #elif s == 'exec':
        #    self.emit_symbol('python3', 'exec')
        #elif s == 'execfile':
        #    self.emit_symbol('python2', 'execfile')
        #elif s == 'file':
        #    self.emit_symbol('python2', 'file')
        #elif s == 'filter':
        #    self.emit_symbol('iter1', 'filter')
        #elif s == 'float':
        #    self.emit_symbol('float64', 'to_float64')
        #elif s == 'format':
        #    self.emit_symbol('python2', 'format')
        #elif s == 'frozenset':
        #    self.emit_symbol('set5', 'to_set')
        #elif s == 'getattr':
        #    self.emit_symbol('python2', 'getattr')
        #elif s == 'globals':
        #    self.emit_symbol('python2', 'globals')
        #elif s == 'hasattr':
        #    self.emit_symbol('python2', 'hasattr')
        #elif s == 'hash':
        #    self.emit_symbol('python2', 'hash')
        #elif s == 'help':
        #    self.emit_symbol('python2', 'help')
        #elif s == 'hex':
        #    self.emit_symbol('python2', 'hex')
        #elif s == 'id':
        #    self.emit_symbol('python2', 'id')
        #elif s == 'input':
        #    self.emit_symbol('python2', 'input')
        #elif s == 'int':
        #    self.emit_symbol('python2', 'int')
        #elif s == 'intern':
        #    self.emit_symbol('python2', 'intern')
        #elif s == 'isinstance':
        #    self.emit_symbol('python2', 'isinstance')
        #elif s == 'issubclass':
        #    self.emit_symbol('python2', 'issubclass')
        #elif s == 'iter':
        #    self.emit_symbol('python2', 'iter')
        #elif s == 'len':
        #    self.emit_symbol('python2', 'len')
        #elif s == 'list':
        #    self.emit_symbol('mlist5', 'to_mlist')
        #elif s == 'locals':
        #    self.emit_symbol('python2', 'locals')
        #elif s == 'long':
        #    self.emit_symbol('python2', 'long')
        #elif s == 'map':
        #    self.emit_symbol('iter1', 'map')
        elif s == 'max':
            self.emit_symbol('minmax1', 'max')
        #elif s == 'memoryview':
        #    self.emit_symbol('python2', 'memoryview')
        elif s == 'min':
            self.emit_symbol('minmax1', 'min')
        #elif s == 'next':
        #    self.emit_symbol('python2', 'next')
        #elif s == 'object':
        #    self.emit_symbol('python2', 'object')
        #elif s == 'oct':
        #    self.emit_symbol('python2', 'oct')
        #elif s == 'open':
        #    self.emit_symbol('python2', 'open')
        #elif s == 'ord':
        #    self.emit_symbol('char1', 'character_to_integer')
        elif s == 'pow':
            self.emit_symbol('arith1', 'power')
        elif s == 'print':
            self.emit_symbol('python3', 'print')
        #elif s == 'property':
        #    self.emit_symbol('python2', 'property')
        #elif s == 'range':
        #    self.emit_symbol('python2', 'range')
        #elif s == 'raw_input':
        #    self.emit_symbol('python2', 'raw_input')
        #elif s == 'reduce':
        #    self.emit_symbol('iter1', 'reduce')
        #elif s == 'reload':
        #    self.emit_symbol('python2', 'reload')
        #elif s == 'repr':
        #    self.emit_symbol('python2', 'repr')
        #elif s == 'reversed':
        #    self.emit_symbol('python2', 'reversed')
        elif s == 'round':
            self.emit_symbol('rounding_rta', 'round')
        #elif s == 'set':
        #    self.emit_symbol('mset5', 'to_mset')
        elif s == 'setattr':
            self.emit_symbol('python2', 'setattr')
        elif s == 'slice':
            self.emit_symbol('python2', 'slice')
        elif s == 'sorted':
            self.emit_symbol('python2', 'sorted')
        elif s == 'staticmethod':
            self.emit_symbol('python2', 'staticmethod')
        elif s == 'str' and self.unicode_literals == 2:
            self.emit_symbol('string1', 'to_string')
        elif s == 'str' and self.unicode_literals == 3:
            self.emit_symbol('bytes1', 'to_bytes')
        #elif s == 'sum':
        #    self.emit_symbol('iter1', 'sum')
        #elif s == 'super':
        #    self.emit_symbol('python2', 'super')
        #elif s == 'tuple':
        #    self.emit_symbol('list5', 'to_list')
        #elif s == 'type':
        #    self.emit_symbol('python2', 'type')
        #elif s == 'unichr':
        #    self.emit_symbol('python2', 'unichr')
        #elif s == 'unicode':
        #    self.emit_symbol('string1', 'to_string')
        #elif s == 'vars':
        #    self.emit_symbol('python2', 'vars')
        #elif s == 'xrange':
        #    self.emit_symbol('python2', 'xrange')
        #elif s == 'zip':
        #    self.emit_symbol('iter1', 'zip')
        elif s == 'True':
            self.emit_symbol('logic1', 'true')
        elif s == 'False':
            self.emit_symbol('logic1', 'false')
        elif s == 'None':
            self.emit_symbol('prog2', 'null')
        else:
            print('<m:ci>%s</m:ci>' % s)

    def emit_elem(self, prefix, name):
        print('<%s:%s>' % (prefix, name))

    def emit_elem_end(self, prefix, name):
        print('</%s:%s>' % (prefix, name))

    def emit_app_parens_false(self):
        self.emit_elem('m', 'apply parens="false"')

    def emit_app(self):
        self.emit_elem('m', 'apply')

    def emit_app_end(self):
        self.emit_elem_end('m', 'apply')

    def emit_bind(self):
        self.emit_elem('m', 'bind')

    def emit_bind_end(self):
        self.emit_elem_end('m', 'bind')

    def emit_bvar(self):
        self.emit_elem('m', 'bvar')

    def emit_bvar_end(self):
        self.emit_elem_end('m', 'bvar')

    def emit_bdom(self):
        self.emit_elem('m', 'domainofapplication')

    def emit_bdom_end(self):
        self.emit_elem_end('m', 'domainofapplication')

    def emit_decl(self):
        self.emit_elem('drox', 'dl')

    def emit_decl_end(self):
        self.emit_elem_end('drox', 'dl')

    def emit_decl_item(self):
        self.emit_elem('drox', 'di')

    def emit_decl_item_end(self):
        self.emit_elem_end('drox', 'di')

    def emit_decl_term(self):
        self.emit_elem('drox', 'dt')

    def emit_decl_term_end(self):
        self.emit_elem_end('drox', 'dt')

    def visit_arguments(self, node):
        narguments = len(node.args) - len(node.defaults)
        for arg in node.args[:narguments]:
            self.emit_bvar()
            self.emit_id(arg.id)
            self.emit_bvar_end()
        for index in range(len(node.defaults)):
            key = node.args[narguments + index]
            value = node.defaults[index]
            self.emit_bvar()
            self.emit_id(key.id)
            self.emit_elem('drox', 'init')
            self.visit(value)
            self.emit_elem_end('drox', 'init')
            self.emit_bvar_end()
        if node.vararg:
            self.emit_bvar()
            self.emit_app()
            self.emit_symbol('python2', 'args')
            self.emit_id(node.vararg)
            self.emit_app_end()
            self.emit_bvar_end()
        if node.kwarg:
            self.emit_bvar()
            self.emit_app()
            self.emit_symbol('python2', 'kwargs')
            self.emit_id(node.kwarg)
            self.emit_app_end()
            self.emit_bvar_end()

    def visit_bases(self, bases):
        # TODO: rethink
        if len(bases) > 0:
            print('<py:base>')
            for base in bases:
                self.visit(base)
            print('</py:base>')

    def visit_decorators(self, decorators):
        # TODO: rethink
        if len(decorators) > 0:
            print('<py:decorator>')
            for decorator in decorators:
                self.visit(decorator)
            print('</py:decorator>')

    def visit_raw_num(self, num):
        print('<m:cn>%s</m:cn>' % num)

    def visit_Num(self, node):
        if node.n == 0:
            self.emit_symbol('alg1', 'zero')
        elif node.n == 1:
            self.emit_symbol('alg1', 'one')
        else:
            self.visit_raw_num(node.n)

    def visit_Str(self, node):
        print('<m:cs>%s</m:cs>' % xml_escape(node.s))

    def visit_Module(self, node):
        print('''<drox:dl
xmlns:drox="http://drosoft.org/ns/drosera"
xmlns:py="http://drosoft.org/ns/drosera/pythonxml"
xmlns:m="http://www.w3.org/1998/Math/MathML">''')
        self.emit_symbol('python2', 'module')
        self.generic_visit(node)
        print('</drox:dl>')

    def visit_FunctionDef(self, node):
        self.emit_decl()
        self.emit_symbol('python2', 'def')
        self.emit_decl_term()
        self.emit_id(node.name)
        self.emit_decl_term_end()
        self.visit_decorators(node.decorator_list)
        self.visit_arguments(node.args)
        for stmt in node.body:
            self.visit(stmt)
        self.emit_decl_end()

    def visit_ClassDef(self, node):
        self.emit_decl()
        self.emit_symbol('python2', 'class')
        self.emit_decl_term()
        self.emit_id(node.name)
        self.visit_bases(node.bases)
        self.visit_decorators(node.decorator_list)
        self.emit_decl_term_end()
        for stmt in node.body:
            self.visit(stmt)
        self.emit_decl_end()

    def visit_Return(self, node):
        self.emit_app()
        self.emit_symbol('prog1', 'return')
        self.generic_visit(node)
        self.emit_app_end()

    def visit_Delete(self, node):
        self.emit_app()
        self.emit_symbol('prog2', 'delete')
        self.generic_visit(node)
        self.emit_app_end()

    def visit_Assign(self, node):
        self.emit_decl()
        self.emit_symbol('prog1', 'assignment')
        self.emit_decl_term()
        for target in node.targets:
            self.visit(target)
        self.emit_decl_term_end()
        self.visit(node.value)
        self.emit_decl_end()

    def visit_AugAssign(self, node):
        self.emit_decl()
        self.emit_symbol('prog2', 'assignment_operator')
        self.emit_decl_term()
        self.visit(node.target)
        self.emit_decl_term_end()
        self.visit(node.op)
        self.visit(node.value)
        self.emit_decl_end()

    def visit_Print(self, node):
        self.emit_app()
        self.emit_symbol('python2', 'print')
        self.generic_visit(node)
        self.emit_app_end()

    def visit_For(self, node):
        self.emit_app()
        self.emit_symbol('prog2', 'for_each')
        print('<m:bvar>')
        self.visit(node.target)
        print('</m:bvar>')
        print('<m:domainofapplication>')
        self.visit(node.iter)
        print('</m:domainofapplication>')
        for stmt in node.body:
            self.visit(stmt)
        if len(node.orelse) > 0:
            self.visit_Else(node.orelse)
        self.emit_app_end()

    def visit_While(self, node):
        self.emit_app()
        self.emit_symbol('prog1', 'while')
        self.visit(node.test)
        for stmt in node.body:
            self.visit(stmt)
        if len(node.orelse) > 0:
            self.visit_Else(node.orelse)
        self.emit_app_end()

    def visit_If(self, node):
        if len(node.orelse) > 0 and node.orelse[0].__class__.__name__ == 'If':
            self.emit_decl()
            self.emit_symbol('switch2', 'cond')
            mode = node
            while mode and mode.__class__.__name__ == 'If':
                self.emit_decl_item()
                self.visit(mode.test)
                for stmt in mode.body:
                    self.visit(stmt)
                self.emit_decl_item_end()
                if len(mode.orelse) > 0 and mode.orelse[0].__class__.__name__ != 'If':
                    for stmt in mode.orelse:
                        self.visit(stmt)
                    break
                if len(mode.orelse) == 0:
                    break
                mode = mode.orelse[0]
            self.emit_decl_end()
        else:
            self.emit_app()
            self.emit_symbol('prog2', 'if')
            self.visit(node.test)
            for stmt in node.body:
                self.visit(stmt)
            if len(node.orelse) > 0:
                self.visit_Else(node.orelse)
            self.emit_app_end()

    def visit_Else(self, stmts):
        self.emit_app()
        self.emit_symbol('prog2', 'else')
        for stmt in stmts:
            self.visit(stmt)
        self.emit_app_end()

    def visit_WithItem(self, node):
        pass

    def visit_With(self, node):
        self.emit_app()
        self.emit_symbol('python3', 'with')
        self.generic_visit(node)
        self.emit_app_end()

    def visit_Raise(self, node):
        self.emit_app()
        self.emit_symbol('prog2', 'throw')
        self.generic_visit(node)
        self.emit_app_end()

    def visit_TryExcept(self, node):
        # TODO: test
        self.emit_app()
        self.emit_symbol('python2', 'try_except')
        self.generic_visit(node)
        self.emit_app_end()

    def visit_TryFinally(self, node):
        # TODO: test
        self.emit_app()
        self.emit_symbol('python2', 'try_finally')
        self.generic_visit(node)
        self.emit_app_end()

    def visit_Assert(self, node):
        self.emit_app()
        self.emit_symbol('prog2', 'assert')
        self.visit(node.test)
        if node.msg:
            self.visit(node.msg)
        self.emit_app_end()

    def visit_Import(self, node):
        self.emit_app()
        self.emit_symbol('python2', 'import')
        self.visit_names(node.names)
        self.emit_app_end()

    def visit_alias(self, alias):
        if alias.asname == None:
            self.emit_id(alias.name)
        else:
            self.emit_id_as(alias.name, alias.asname)

    def visit_names(self, names):
        for alias in names:
            self.visit_alias(alias)

    def visit_ImportFrom(self, node):
        self.emit_app()
        self.emit_symbol('python2', 'import_from')
        self.emit_id(node.module)
        if node.module == '__future__':
            for alias in node.names:
                if alias.name == 'print_function':
                    DroVisitor.print_function = 3
                if alias.name == 'unicode_literals':
                    DroVisitor.unicode_literals = 3
        self.visit_names(node.names)
        if node.level > 0:
            self.visit_raw_num(node.level)
        self.emit_app_end()

    def visit_Exec(self, node):
        self.emit_app()
        self.emit_symbol('python2', 'exec')
        self.generic_visit(node)
        self.emit_app_end()

    def visit_Global(self, node):
        self.emit_app()
        self.emit_symbol('prog1', 'global_var')
        self.generic_visit(node)
        self.emit_app_end()

    def visit_Pass(self, node):
        self.emit_app()
        self.emit_symbol('prog2', 'empty')
        self.generic_visit(node)
        self.emit_app_end()

    def visit_Break(self, node):
        self.emit_app()
        self.emit_symbol('prog2', 'break')
        self.generic_visit(node)
        self.emit_app_end()

    def visit_Continue(self, node):
        self.emit_app()
        self.emit_symbol('prog2', 'continue')
        self.generic_visit(node)
        self.emit_app_end()

    def visit_BoolOp(self, node):
        self.emit_app_parens_false()
        self.visit(node.op)
        for value in node.values:
            self.visit(value)
        self.emit_app_end()

    def visit_BinOp(self, node):
        self.emit_app_parens_false()
        self.visit(node.op)
        self.visit(node.left)
        self.visit(node.right)
        self.emit_app_end()

    def visit_UnaryOp(self, node):
        self.emit_app()
        self.visit(node.op)
        self.visit(node.operand)
        self.emit_app_end()

    def visit_Lambda(self, node):
        self.emit_bind()
        self.emit_symbol('fns1', 'lambda')
        self.visit_arguments(node.args)
        self.visit(node.body)
        self.emit_bind_end()

    def visit_IfExp(self, node):
        self.emit_app()
        self.emit_symbol('prog2', 'if_exp')
        self.generic_visit(node)
        self.emit_app_end()

    def visit_Dict(self, node):
        self.emit_app()
        self.emit_symbol('python2', 'dict')
        self.generic_visit(node)
        self.emit_app_end()

    def visit_Set(self, node):
        self.emit_app()
        self.emit_symbol('python2', 'set')
        self.generic_visit(node)
        self.emit_app_end()

    def visit_ListComp(self, node):
        self.emit_app()
        self.emit_symbol('python2', 'list_comp')
        self.generic_visit(node)
        self.emit_app_end()

    def visit_SetComp(self, node):
        self.emit_app()
        self.emit_symbol('python2', 'set_comp')
        self.generic_visit(node)
        self.emit_app_end()

    def visit_DictComp(self, node):
        self.emit_app()
        self.emit_symbol('python2', 'dict_comp')
        self.generic_visit(node)
        self.emit_app_end()

    def visit_GeneratorExp(self, node):
        self.emit_app()
        self.emit_symbol('python2', 'generator')
        self.generic_visit(node)
        self.emit_app_end()

    def visit_Yield(self, node):
        self.emit_app()
        self.emit_symbol('prog3', 'yield')
        self.generic_visit(node)
        self.emit_app_end()

    def visit_Compare(self, node):
        if len(node.ops) == 1:
            self.emit_app()
            self.visit(node.ops[0])
            self.visit(node.left)
            self.visit(node.comparators[0])
            self.emit_app_end()
        else:
            self.emit_app()
            self.emit_symbol('python2', 'compare')
            self.visit(node.left)
            for i in range(len(node.ops)):
                self.visit(node.ops[i])
                self.visit(node.comparators[i])
            self.emit_app_end()

    def visit_keyword(self, keyword):
        key = keyword.arg
        value = keyword.value
        self.emit_decl_item()
        self.emit_id(key)
        self.visit(value)
        self.emit_decl_item_end()

    def visit_Call(self, node):
        self.emit_app()
        self.visit(node.func)
        for arg in node.args:
            self.visit(arg)
        for arg in node.keywords:
            self.visit_keyword(arg)
        if node.starargs:
            self.emit_app()
            self.emit_symbol('python2', 'args')
            self.visit(node.starargs)
            self.emit_app_end()
        if node.kwargs:
            self.emit_app()
            self.emit_symbol('python2', 'kwargs')
            self.visit(node.kwargs)
            self.emit_app_end()
        self.emit_app_end()

    def visit_Repr(self, node):
        self.emit_app()
        self.emit_symbol('python2', 'repr')
        self.visit(node.value)
        self.emit_app_end()

    def visit_context(self, ctx):
        if type(ctx) is not ast.Load:
            self.visit(ctx)

    def visit_Attribute(self, node):
        if type(node.value) is ast.Attribute:
            if type(node.value.value) is ast.Attribute:
                if type(node.value.value.value) is ast.Name:
                    ns = [node.value.value.value.id, 
                          node.value.value.attr, 
                          node.value.attr, node.attr]
                    print('<m:ci>%s</m:ci>' % '<m:sep/>'.join(ns))
            elif type(node.value.value) is ast.Name:
                ns = [node.value.value.id, node.value.attr, node.attr]
                print('<m:ci>%s</m:ci>' % '<m:sep/>'.join(ns))
        elif type(node.value) is ast.Name:
            ns = [node.value.id, node.attr]
            print('<m:ci>%s</m:ci>' % '<m:sep/>'.join(ns))
        else:
            self.emit_app()
            self.emit_symbol('prog2', 'namespace_selector')
            self.visit(node.value)
            self.emit_id(node.attr)
            self.visit_context(node.ctx)
            self.emit_app_end()

    def visit_Subscript(self, node):
        self.emit_app()
        self.emit_symbol('python2', 'selector')
        self.visit(node.value)
        self.visit(node.slice)
        self.visit_context(node.ctx)
        self.emit_app_end()

    def visit_Name(self, node):
        self.emit_id(node.id)

    def visit_List(self, node):
        self.emit_app()
        self.emit_symbol('python2', 'list')
        for elem in node.elts:
            self.visit(elem)
        self.visit_context(node.ctx)
        self.emit_app_end()

    def visit_Tuple(self, node):
        self.emit_app()
        self.emit_symbol('python2', 'tuple')
        for elem in node.elts:
            self.visit(elem)
        self.visit_context(node.ctx)
        self.emit_app_end()

    def visit_Ellipsis(self, node):
        self.emit_symbol('python2', 'ellipsis')

    def visit_Slice(self, node):
        self.emit_app()
        self.emit_symbol('python2', 'slice')
        if node.lower:
            print('<m:lowlimit>')
            self.visit(node.lower)
            print('</m:lowlimit>')
        if node.upper:
            print('<m:uplimit>')
            self.visit(node.upper)
            print('</m:uplimit>')
        if node.step:
            print('<py:step>')
            self.visit(node.step)
            print('</py:step>')
        self.emit_app_end()

    def visit_ExtSlice(self, node):
        self.emit_app()
        self.emit_app_end()

    def visit_Index(self, node):
        self.visit(node.value)

    def visit_Load(self, node):
        # TODO: rethink
        self.emit_symbol('python2', 'load')

    def visit_Store(self, node):
        # TODO: rethink
        self.emit_symbol('python2', 'store')

    def visit_Del(self, node):
        # TODO: rethink
        self.emit_symbol('python2', 'del')

    def visit_AugLoad(self, node):
        # TODO: rethink
        self.emit_symbol('python2', 'aug_load')

    def visit_AugStore(self, node):
        # TODO: rethink
        self.emit_symbol('python2', 'aug_store')

    def visit_Param(self, node):
        # TODO: rethink
        self.emit_symbol('python2', 'param')

    def visit_And(self, node):
        self.emit_symbol('logic1', 'and')

    def visit_Or(self, node):
        self.emit_symbol('logic1', 'or')

    def visit_Add(self, node):
        self.emit_symbol('arith2', 'plus')

    def visit_Sub(self, node):
        self.emit_symbol('arith1', 'minus')

    def visit_Mult(self, node):
        self.emit_symbol('arith1', 'times')

    def visit_Div(self, node):
        self.emit_symbol('python2', 'divide')

    def visit_Mod(self, node):
        self.emit_symbol('rounding_rtn', 'remainder')

    def visit_Pow(self, node):
        self.emit_symbol('arith1', 'power')

    def visit_LShift(self, node):
        self.emit_symbol('bitwise3', 'left_shift')

    def visit_RShift(self, node):
        self.emit_symbol('bitwise3', 'arithmetic_right_shift')

    def visit_BitOr(self, node):
        self.emit_symbol('bitwise1', 'or')

    def visit_BitXor(self, node):
        self.emit_symbol('bitwise1', 'xor')

    def visit_BitAnd(self, node):
        self.emit_symbol('bitwise1', 'and')

    def visit_FloorDiv(self, node):
        self.emit_symbol('rounding_rtn', 'quotient')

    def visit_Invert(self, node):
        self.emit_symbol('bitwise1', 'not')

    def visit_Not(self, node):
        self.emit_symbol('logic1', 'not')

    def visit_UAdd(self, node):
        self.emit_symbol('arith2', 'unary_plus')

    def visit_USub(self, node):
        self.emit_symbol('arith1', 'unary_minus')

    def visit_Eq(self, node):
        self.emit_symbol('relation1', 'eq')

    def visit_NotEq(self, node):
        self.emit_symbol('relation1', 'neq')

    def visit_Lt(self, node):
        self.emit_symbol('relation1', 'lt')

    def visit_LtE(self, node):
        self.emit_symbol('relation1', 'leq')

    def visit_Gt(self, node):
        self.emit_symbol('relation1', 'gt')

    def visit_GtE(self, node):
        self.emit_symbol('relation1', 'geq')

    def visit_Is(self, node):
        self.emit_symbol('python2', 'is')

    def visit_IsNot(self, node):
        self.emit_symbol('python2', 'isnot')

    def visit_In(self, node):
        self.emit_symbol('set1', 'in')

    def visit_NotIn(self, node):
        self.emit_symbol('set1', 'notin')
