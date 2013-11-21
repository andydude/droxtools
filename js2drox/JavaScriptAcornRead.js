
function DroVisitor() {}
DroVisitor.prototype = {
    comments: [],
    encodeHTML: function(text) {
	    var str = new String(encodeURI(text));
        return str.replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;');
    },
    emitNs: function(names) {
        // TODO: add parameter to force symbol, apply/ci, ns

        var mapping = {
            'Math.abs': 	['arith1', 		'abs'],
            'Math.acos':	['transc1', 	'arccos'],
            'Math.asin':	['transc1', 	'arcsin'],
            'Math.atan':	['transc1', 	'arctan'],
            'Math.atan2':	['transc2', 	'arctan'],
            'Math.ceil': 	['rounding1', 	'ceiling'],
            'Math.cos': 	['transc1', 	'cos'],
            'Math.e': 		['nums1', 		'e'],
            'Math.exp': 	['transc1', 	'exp'],
            'Math.floor': 	['rounding1', 	'floor'],
            'Math.log': 	['transc1', 	'ln'],
            'Math.max': 	['minmax1', 	'max'],
            'Math.min': 	['minmax1', 	'min'],
            'Math.pi': 		['nums1', 		'pi'],
            'Math.pow': 	['arith1', 		'power'],
            'Math.random': 	['random1', 	'random_unit'],
            'Math.round': 	['rounding_rnp', 'round'],
            'Math.sin': 	['transc1', 	'sin'],
            'Math.sqrt': 	['transc1', 	'sqrt'],
            'Math.tan': 	['transc1', 	'tan'],
        };

        var s = names[0].value;
        names.slice(1).forEach(function(nameObj, index){
            s += '.' + nameObj.value;
        }, this);

        if (mapping.hasOwnProperty(s)) {
            this.emitSymbol(mapping[s]);
        } else {
            print('<m:ci>' + s.replace(/\./g, '<m:sep/>') + '</m:ci>');
        }
    },
    emitId: function(s) {
        // TODO: add parameter to force symbol, ci
        var mapping = {
            'true': 		['logic1', 		'true'],
            'false': 		['logic1', 		'false'],
            'null': 		['prog2', 		'null'],
            'NaN': 			['nums1', 		'NaN'],
            'Infinity': 	['nums1', 		'Infinity'],
            'undefined': 	['ecmascript3', 'undefined'],
            'get': 			['ecmascript3', 'get'],
            'set': 			['ecmascript3', 'set'],
            'arguments': 	['ecmascript3', 'arguments'],
            'eval': 		['ecmascript3', 'eval'],
            'parseInt': 	['ecmascript3', 'parseInt'],
            'parseFloat': 	['ecmascript3', 'parseFloat'],
            'isNaN': 		['ecmascript3', 'isNaN'],
            'isFinite': 	['ecmascript3', 'isFinite'],
            'decodeURI': 	['ecmascript3', 'decodeURI'],
            'decodeURIComponent': ['ecmascript3', 'decodeURIComponent'],
            'encodeURI': 	['ecmascript3', 'encodeURI'],
            'encodeURIComponent': ['ecmascript3', 'encodeURIComponent'],
        };

        if (mapping.hasOwnProperty(s)) {
            this.emitSymbol(mapping[s]);
        } else {
            print('<m:ci>' + s + '</m:ci>');
        }
    },
    emitNum: function(value) {
        // TODO: add parameter to force symbol, cn
        switch (value) {
        case 0:
            this.emitSym('alg1', 'zero');
            break;
        case 1:
            this.emitSym('alg1', 'one');
            break;
        default:
            print('<m:cn>' + this.encodeHTML(value) + '</m:cn>');
        }
    },
    emitLit: function(value) {
        switch (typeof value) {
        case "string":
            this.emitStr(value);
            break;
        case "number":
            this.emitNum(value);
            break;
        case "boolean":
        case "undefined":
        case "object":
            var str = String(value);
            this.emitId(str);
            break;
        default:
            print("Unknown Literal");
        }
    },
    emitStr: function(value) {
        print('<m:cs>' + this.encodeHTML(value) + '</m:cs>');
    },
    emitSym: function(cd, name) {
        print('<m:csymbol cd="' + cd + '">' + name + '</m:csymbol>')
    },
    emitSymbol: function(pair) {
        //[cd, name] = pair;
        var cd = pair[0], name = pair[1];
        print('<m:csymbol cd="' + cd + '">' + name + '</m:csymbol>')
    },
    emitRegExp: function(value) {
        this.emitApp();
        this.emitSym('ecmascript3', 'regexp');
        //print(JSON.stringify(value));
        //var re = defs.source.slice(node.start, node.end);
        this.emitStr(value);
        this.emitAppEnd();
    },
    emitElem: function(prefix, name) {
        print('<' + prefix + ':' + name + '>')
    },
    emitElemEnd: function(prefix, name) {
        print('</' + prefix + ':' + name + '>')
    },

    // no more print() uses

    emitApp: function() {
        this.emitElem('m', 'apply');
    },
    emitAppEnd: function() {
        this.emitElemEnd('m', 'apply');
    },
    emitBind: function() {
        this.emitElem('m', 'bind');
    },
    emitBindEnd: function() {
        this.emitElemEnd('m', 'bind');
    },
    emitDecl: function() {
        this.emitElem('drox', 'decl');
    },
    emitDeclEnd: function() {
        this.emitElemEnd('drox', 'decl');
    },
    emitDeclItem: function() {
        this.emitElem('drox', 'di');
    },
    emitDeclItemEnd: function() {
        this.emitElemEnd('drox', 'di');
    },
    emitDeclTerm: function() {
        this.emitElem('drox', 'dt');
    },
    emitDeclTermEnd: function() {
        this.emitElemEnd('drox', 'dt');
    },
    emitStmt: function() {
        this.emitElem('drox', 'stmt');
    },
    emitStmtEnd: function() {
        this.emitElemEnd('drox', 'stmt');
    },
    emitStmtTerm: function() {
        this.emitElem('drox', 'st');
    },
    emitStmtTermEnd: function() {
        this.emitElemEnd('drox', 'st');
    },
    emitScript: function() {
        this.emitElem('drox', 'decl xmlns:drox="http://drosoft.org/ns/drosera" xmlns:m="http://www.w3.org/1998/Math/MathML"');
    },
    emitScriptEnd: function() {
        this.emitDeclEnd()
    },
    emitComment: function(comment) {
        var out = '<!--';
        out += comment.block ? '\n' : '';
        out += comment.text.replace(/-/g, '&#x2D');
        out += comment.block ? '\n' : ' ';
        out += '-->';
        print(out);
    },
    onComment: function(block, text, start, end) {
        var comment = {
            type: 'Comment',
            text: text,
            block: block,
            start: start,
            end: end,
        };
        this.comments.push(comment);
    },

    // no more emit() decls

    visitNodeType: function(s) {
        var mapping = {
            'ArrayExpression': 		['ecmascript3', 'array'],
            'ArrayPattern': 		['ecmascript4', 'array_pattern'],
            'ArrowExpression': 		['ecmascript4', 'arrow'],
            'AssignmentExpression': ['prog1', 		'assignment'],
            'AssignmentOperator': 	['prog2', 		'assignment_operator'],
            'BlockStatement': 		['prog1', 		'block'],
            'BreakStatement': 		['prog2', 		'break'],
            'CallExpression': 		['prog2', 		'namespace_apply'],
            'CatchClause': 			['exn1', 		'catch'],
            'ComprehensionBlock': 	['ecmascript4', 'comp_block'],
            'ComprehensionExpression': ['ecmascript4', 'comp'],
            'ConditionalExpression': ['prog2', 		'if_exp'],
            'ContinueStatement': 	['prog2', 		'continue'],
            'DebuggerStatement': 	['ecmascript5', 'debugger'],
            'DotExpression':		['prog2', 		'namespace_selector'],
            'DoWhileStatement': 	['prog2', 		'do_while'],
            'EmptyStatement': 		['prog2', 		'empty'],
            'ForInStatement': 		['iter1', 		'for_each'],
            'ForOfStatement': 		['iter2', 		'for_each'],
            'ForStatement': 		['prog1', 		'for'],
            'FunctionDeclaration': 	['ecmascript3', 'function'],
            'FunctionExpression': 	['fns1', 		'lambda'],
            'FinallyClause': 		['exn1', 		'finally'],
            'GeneratorExpression': 	['ecmascript3', 'generator'],
            'GraphExpression': 		['ecmascript3', 'graph'],
            'GraphIndexExpression': ['ecmascript3', 'graph_selector'],
            'IfStatement': 			['prog1', 		'if'],
            'LabeledStatement': 	['prog2', 		'label'],
            'LetExpression': 		['ecmascript4', 'let'],
            'LetStatement': 		['ecmascript4', 'let'],
            'IndexExpression': 		['ecmascript3', 'selector'],
            'NewExpression': 		['prog2', 		'new'],
            'ObjectExpression': 	['prog2', 		'namespace'],
            'ObjectPattern': 		['ecmascript4', 'object_pattern'],
            'Pattern': 				['ecmascript4', 'pattern'],
            'Program': 				['ecmascript3',	'program'],
            'ReturnStatement': 		['prog1', 		'return'],
            'SequenceExpression': 	['prog2', 		'begin'],
            'SwitchStatement': 		['switch1', 	'case'],
            'ThisExpression': 		['ecmascript3', 'this'],
            'ThrowStatement': 		['exn1', 		'throw'],
            'TryStatement': 		['exn1', 		'try'],
            'VariableDeclaration': 	['prog1', 		'local_var'],
            'WhileStatement': 		['prog1', 		'while'],
            'WithStatement': 		['ecmascript3', 'with'],
        };
        this.emitSymbol(mapping[s]);
    },

    visitArrayExpression: function(node) {
        this.emitApp();
        this.visitNodeType(node.type);
        if (node.elements) {
            this.visitNodes(node.elements);
        }
        this.emitAppEnd();
    },
    visitArrayPattern: function(node) {
        print("CALLED");
    },
    visitAssignmentExpression: function(node) {
        this.emitStmt();

        if (node.operator === '=') {
            this.visitNodeType(node.type);
            this.emitStmtTerm();
            this.visit(node.left);
            this.emitStmtTermEnd();
            this.visit(node.right);
        } else {
            this.visitNodeType('AssignmentOperator');
            this.visitAssignmentOperator(node.operator);
            this.emitStmtTerm();
            this.visit(node.left);
            this.emitStmtTermEnd();
            this.visit(node.right);
        }

        this.emitStmtEnd();
    },
    visitAssignmentOperator: function(s) {
        this.visitBinaryOperator(s.slice(0, -1));
    },
    visitRegularExpression: function(node) {
        this.emitRegExp(node.raw);
    },
    visitBinaryExpression: function(node) {
        this.emitApp();
        this.visitBinaryOperator(node.operator);
        this.visit(node.left);
        this.visit(node.right);
        this.emitAppEnd();
    },
    visitBinaryOperator: function(s) {
        var mapping = {
            '===': 		['ecmascript3', 'eq'],
            '!==': 		['ecmascript3', 'neq'],
            '==': 		['relation1', 'eq'],
            '!=': 		['relation1', 'eq'],
            '<': 		['relation1', 'lt'],
            '<=': 		['relation1', 'leq'],
            '>': 		['relation1', 'gt'],
            '>=': 		['relation1', 'geq'],
            '<<': 		['bitwise3', 'left_shift'],
            '>>': 		['bitwise3', 'arithmetic_right_shift'],
            '>>>': 		['bitwise3', 'logical_right_shift'],
            '+': 		['arith2', 'plus'],
            '-': 		['arith1', 'minus'],
            '*': 		['arith1', 'times'],
            '/': 		['arith1', 'divide'],
            '%': 		['arith1', 'remainder'],
            '&': 		['bitwise1', 'and'],
            '|': 		['bitwise1', 'or'],
            '^': 		['bitwise1', 'xor'],
            '||': 		['logic1', 'or'],
            '&&': 		['logic1', 'and'],
            'in': 		['ecmascript3', 'in'],
            'instanceof': ['ecmascript3', 'instanceof'],
        };
        this.emitSymbol(mapping[s]);
    },

    visitBlockStatement: function(node) {
        this.emitStmt();
        this.visitNodeType(node.type);
        this.visitNodes(node.body);
        this.emitStmtEnd();
    },
    visitBreakStatement: function(node) {
        this.emitStmt();
        this.visitNodeType(node.type);
        this.emitStmtEnd();
    },
    visitCallExpression: function(node) {
        this.emitApp();
        this.visit(node.callee);
        if (node.arguments) {
            this.visitNodes(node.arguments);
        }
        this.emitAppEnd();
    },
    visitConditionalExpression: function(node) {
        this.emitApp();
        this.visitNodeType(node.type);
        this.visit(node.test);
        this.visit(node.consequent);
        this.visit(node.alternate);
        this.emitAppEnd();
    },
    visitContinueStatement: function(node) {
        this.emitStmt();
        this.visitNodeType(node.type);
        this.emitStmtEnd();
    },
    visitDebuggerStatement: function(node) {
        this.emitStmt();
        this.visitNodeType(node.type);
        this.emitStmtEnd();
    },
    visitDoWhileStatement: function(node) {
        this.emitStmt();
        this.visitNodeType(node.type);
        this.visit(node.test);
        this.visitBody(node.body);
        this.emitStmtEnd();
    },
    visitIfStatement: function(node) {
        this.emitStmt();
        this.visitNodeType(node.type);
        this.emitStmtEnd();
    },
    visitIdentifier: function(node) {
        this.emitId(node.name);
    },
    visitReturnStatement: function(node) {
        this.emitStmt();
        this.visitNodeType(node.type);
        if (node.argument) {
            this.visit(node.argument);
        }
        this.emitStmtEnd();
    },

    visitSwitchCase: function(node) {
        print('visitSwitchCase');
    },
    visitSwitchStatement: function(node) {
        this.emitStmt();
        this.visitNodeType(node.type);
        this.emitStmtEnd();
    },
    visitThrowStatement: function(node) {
        this.emitStmt();
        this.visitNodeType(node.type);
        this.visit(node.argument);
        this.emitStmtEnd();
    },
    visitCatchClause: function(node) {
        this.emitDecl();
        this.visitNodeType(node.type);
        this.visit(node.param);
        if (node.guard) {
            this.visit(node.guard);
        }
        this.visitBody(node.body);
        this.emitDeclEnd();
    },
    visitFinallyClause: function(node) {
        this.emitDecl();
        this.visitNodeType(node.type);
        //this.visit(node.body);
        this.emitDeclEnd();
    },
    visitTryStatement: function(node) {
        this.emitDecl();
        this.visitNodeType(node.type);
        this.visit(node.block);
        if (node.handler) { // SpiderMonkey Standard
            this.visit(node.handler);
        }
        if (node.handlers) { // Acorn
            this.visitNodes(node.handlers);
        }
        if (node.guardedHandlers) {
            this.visitNodes(node.guardedHandlers);
        }
	    if (node.finalizer) {
            var finalizer = {
                type: 'FinallyClause',
                body: node.finalizer,
                start: 0, end: 0
            };
            this.visitFinallyClause(finalizer);
	    }
        this.emitDeclEnd();
    },

    visitUpdateExpression: function(node) {
        var op = (node.prefix ? 'pre' : 'post');
        this.emitStmt();
        this.visitUnaryOperator(op + node.operator);
        this.emitStmtTerm();
        this.visit(node.argument);
        this.emitStmtTermEnd();
        this.emitStmtEnd();
    },

    visitUnaryExpression: function(node) {
        // node.prefix = true, AFAICT
        this.emitApp();
        this.visitUnaryOperator(node.operator);
        this.visit(node.argument);
        this.emitAppEnd();
    },
    visitUnaryOperator: function(op) {
        var mapping = {
            '-': 			['arith1', 'unary_minus'],
            '+': 			['arith2', 'unary_plus'],
            '!': 			['logic1', 'not'],
            '~': 			['bitwise1', 'not'],
            'pre--': 		['prog2', 'decrement'],
            'pre++': 		['prog2', 'increment'],
            'post--': 		['prog2', 'post_decrement'],
            'post++': 		['prog2', 'post_increment'],
            'typeof': 		['ecmascript3', 'typeof'],
            'void': 		['prog2', 'to_void'],
            'delete': 		['prog2', 'delete'],
        };
        this.emitSymbol(mapping[op]);
    },

    visitVariableDeclaration: function(node) {
        this.emitDecl();
        this.visitNodeType(node.type);
        if (node.declarations.length === 1) {
            this.visitVariableDeclarator(node.declarations[0]);
        } else {
            node.declarations.forEach(function(decl){
                this.emitDeclItem();
                this.visitVariableDeclarator(decl);
                this.emitDeclItemEnd();
            }, this);
        }
        this.emitDeclEnd();
    },
    visitVariableDeclarator: function(node) {
        this.emitDeclTerm();
        this.visit(node.id);
        this.emitDeclTermEnd();
        if (node.init) {
            this.visit(node.init);
        }
    },
    visitWhileStatement: function(node) {
        this.emitStmt();
        this.visitNodeType(node.type);
        this.visit(node.test);
        this.visit(node.body);
        this.emitStmtEnd();
    },
    visitWithStatement: function(node) {
        this.emitStmt();
        this.visitNodeType(node.type);
        this.visit(node.object);
        this.visit(node.body);
        this.emitStmtEnd();
    },

    visitEmptyStatement: function(node) {
        this.emitStmt();
        this.visitNodeType(node.type);
        this.emitStmtEnd();
    },
    visitLabeledStatement: function(node) {
        this.emitStmt();
        this.visitNodeType(node.type);
        this.emitStmtEnd();
    },
    visitExpressionStatement: function(node) {
        this.visit(node.expression);
    },
    visitForStatement: function(node) {
        this.emitStmt();
        this.visitNodeType(node.type);
        this.emitStmtEnd();
    },
    visitForInStatement: function(node) {
        this.emitStmt();
        this.visitNodeType(node.type);
        this.emitStmtEnd();
    },
    visitSequenceExpression: function(node) {
        this.emitApp();
        this.emitSym('prog2', 'begin');
        this.visitNodes(node.children);
        this.emitAppEnd();
    },
    visitLogicalExpression: function(node) {
    },
    visitMemberExpression: function(node) {
        node.type = node.computed ? 'IndexExpression' : 'DotExpression';

        this.emitApp();
        this.visitNodeType(node.type);
        this.visit(node.object);
        this.visit(node.property);
        this.emitAppEnd();
    },
    visitThisExpression: function(node) {
        this.emitId('this');
    },
    visitLiteral: function(node) {
        // Acorn-specific?
        if (node.raw.charAt(0) == '/') {
            node.type = 'RegularExpression';
            this.visitRegularExpression(node);
            return;
        }

        this.emitLit(node.value);
    },
    visitNewExpression: function(node) {
        this.emitApp();
        this.visitNodeType(node.type);
        this.visit(node.callee);
        if (node.arguments) {
            this.visitNodes(node.arguments);
        }
        this.emitAppEnd();
    },
    visitObjectExpression: function(node) {
        this.emitDecl();
        this.visitNodeType(node.type);
        if (node.properties) {
            node.properties.forEach(function(property) {
                this.visitObjectProperty(property);
            }, this);
        }
        this.emitDeclEnd();
    },
    visitObjectProperty: function(property) {
        // property.kind = 'init' | 'get' | 'set'
        // property.key = Literal | Identifier
        // property.value = Expression
        switch (property.kind) {
        case 'init':
            this.emitDeclItem();
            this.visit(property.key);
            this.visit(property.value);
            this.emitDeclItemEnd();
            break;
        case 'get':
        case 'set':
            this.emitDecl();
            this.emitId(property.kind);
            this.visit(property.key);
            this.visit(property.value);
            this.emitDeclEnd();
            break;
        }
    },
    visitFunctionDeclaration: function(node) {
        this.emitDecl();
        this.visitNodeType(node.type);
        this.emitDeclTerm()
        this.visitIdentifier(node.id);
        this.emitDeclTermEnd()
        this.visitFunctionParameters(node.params, node.defaults, node.rest);
        this.visitBody(node.body);
        //this.visit(node.generator);
        //this.visit(node.expression);
        this.emitDeclEnd();
    },
    visitFunctionExpression: function(node) {
        this.emitBind();
        this.visitNodeType(node.type);
        this.visitFunctionParameters(node.params, node.defaults, node.rest);
        this.visitBody(node.body);
        this.emitBindEnd();
    },
    visitFunctionParameters: function(params, defaults, rest) {
        params.forEach(function(param, index){
            this.emitElem('m', 'bvar');
            this.visit(param);
            this.emitElemEnd('m', 'bvar');
        }, this);
    },

    visitProgram: function(node) {
        this.emitScript();
        this.visitNodeType(node.type);
        this.visitNodes(node.body);
        this.emitScriptEnd();
    },

    visitArrowExpression: function(node) {
        print("CALLED arrow");
    },
    visitForOfStatement: function(node) {
        print("CALLED for_of");
    },
    visitLetStatement: function(node) {
        print("CALLED let");
    },
    visitLetExpression: function(node) {
        print("CALLED let");
    },
    visitYieldExpression: function(node) {
        print("CALLED");
    },
    visitComprehensionExpression: function(node) {
        print("CALLED comp");
    },
    visitGeneratorExpression: function(node) {
        print("CALLED generator");
    },
    visitGraphExpression: function(node) {
        print("CALLED");
    },
    visitGraphIndexExpression: function(node) {
        print("CALLED");
    },
    visitPattern: function(node) {
        print("CALLED pattern");
    },
    visitObjectPattern: function(node) {
        print("CALLED");
    },
    visitComprehensionBlock: function(node) {
        print("CALLED");
    },


    visitXMLDefaultDeclaration: function(node) {
    },
    visitXMLAnyName: function(node) {
    },
    visitXMLQualifiedIdentifier: function(node) {
    },
    visitXMLFunctionQualifiedIdentifier: function(node) {
    },
    visitXMLAttributeSelector: function(node) {
    },
    visitXMLFilterExpression: function(node) {
    },
    visitXMLElement: function(node) {
    },
    visitXMLList: function(node) {
    },
    visitXML: function(node) {
    },
    visitXMLEscape: function(node) {
    },
    visitXMLText: function(node) {
    },
    visitXMLStartTag: function(node) {
    },
    visitXMLEndTag: function(node) {
    },
    visitXMLPointTag: function(node) {
    },
    visitXMLName: function(node) {
    },
    visitXMLAttribute: function(node) {
    },
    visitXMLCdata: function(node) {
    },
    visitXMLComment: function(node) {
    },
    visitXMLProcessingInstruction: function(node) {
    },



    visitBody: function(body) {
        if (body.type === 'BlockStatement') {
            this.visitNodes(body.body);
        } else {
            this.visit(body);
        }
    },
    visitNodes: function(nodes) {
        nodes.forEach(function(node, index){
            this.visit(node);
        }, this);
    },
    visit: function(node) {
        this.comments.forEach(function(comment, index, comments) {
            //print('-- trace ' + node.start + ',' + comment.start);
            if (node.start > comment.start) {
                this.emitComment(comment);
                delete this.comments[index];
            }
        }, this);

        var method = 'visit' + node.type;
        //print("-- trace: " + method + "();");
        return this[method](node);
    }
};

function compileNode(node) {
    if (!node) {
        this.emitSym('prog2', 'empty');
        return;
    }

    switch (node.type) {
    case defs.tokenIds['SEMICOLON']: // expression statements
        compileNode(node.expression);
        break;
    case defs.tokenIds['COMMA']: // multiple expressions
        break;
    case defs.tokenIds['ASSIGN']:
        break;
    case defs.tokenIds['HOOK']: // a?b:c
        break;
        //case defs.tokenIds['COLON']: // never appears
        //    break;
        //case defs.tokenIds['CONDITIONAL']: // never appears
        //    break;
    case defs.tokenIds['OR']:
        this.emitApp();
        this.emitSym('logic1', 'or');
        this.emitAppEnd();
        break;
    case defs.tokenIds['AND']:
        this.emitApp();
        this.emitSym('logic1', 'and');
        this.visitNodes(node.children);
        this.emitAppEnd();
        break;
    case defs.tokenIds['BITWISE_OR']:
        this.emitApp();
        this.emitSym('bitwise1', 'or');
        this.visitNodes(node.children);
        this.emitAppEnd();
        break;
    case defs.tokenIds['BITWISE_XOR']:
        this.emitApp();
        this.emitSym('bitwise1', 'xor');
        this.visitNodes(node.children);
        this.emitAppEnd();
        break;
    case defs.tokenIds['BITWISE_AND']:
        this.emitApp();
        this.emitSym('bitwise1', 'and');
        this.visitNodes(node.children);
        this.emitAppEnd();
        break;
    case defs.tokenIds['EQ']:
        this.emitApp();
        this.emitSym('relation1', 'eq');
        this.visitNodes(node.children);
        this.emitAppEnd();
        break;
    case defs.tokenIds['NE']:
        this.emitApp();
        this.emitSym('relation1', 'neq');
        this.visitNodes(node.children);
        this.emitAppEnd();
        break;
    case defs.tokenIds['STRICT_EQ']:
        this.emitApp();
        this.emitSym('ecmascript3', 'strict_eq');
        this.visitNodes(node.children);
        this.emitAppEnd();
        break;
    case defs.tokenIds['STRICT_NE']:
        this.emitApp();
        this.emitSym('ecmascript3', 'strict_neq');
        this.visitNodes(node.children);
        this.emitAppEnd();
        break;
    case defs.tokenIds['LT']:
        this.emitApp();
        this.emitSym('relation1', 'lt');
        this.visitNodes(node.children);
        this.emitAppEnd();
        break;
    case defs.tokenIds['LE']:
        this.emitApp();
        this.emitSym('relation1', 'leq');
        this.visitNodes(node.children);
        this.emitAppEnd();
        break;
    case defs.tokenIds['GE']:
        this.emitApp();
        this.emitSym('relation1', 'geq');
        this.visitNodes(node.children);
        this.emitAppEnd();
        break;
    case defs.tokenIds['GT']:
        this.emitApp();
        this.emitSym('relation1', 'gt');
        this.visitNodes(node.children);
        this.emitAppEnd();
        break;
    case defs.tokenIds['LSH']: // <<
        this.emitApp();
        this.emitSym('bitwise3', 'left_shift');
        this.visitNodes(node.children);
        this.emitAppEnd();
        break;
    case defs.tokenIds['RSH']: // >>
        this.emitApp();
        this.emitSym('bitwise3', 'arithmetic_right_shift');
        this.visitNodes(node.children);
        this.emitAppEnd();
        break;
    case defs.tokenIds['URSH']: // >>>
        this.emitApp();
        this.emitSym('bitwise3', 'right_shift');
        this.visitNodes(node.children);
        this.emitAppEnd();
        break;
    case defs.tokenIds['PLUS']:
        this.emitApp();
        this.emitSym('arith2', 'plus');
        this.visitNodes(node.children);
        this.emitAppEnd();
        break;
    case defs.tokenIds['MINUS']:
        this.emitApp();
        this.emitSym('arith1', 'minus');
        this.visitNodes(node.children);
        this.emitAppEnd();
        break;
    case defs.tokenIds['MUL']:
        this.emitApp();
        this.emitSym('arith1', 'times');
        this.visitNodes(node.children);
        this.emitAppEnd();
        break;
    case defs.tokenIds['DIV']:
        this.emitApp();
        this.emitSym('arith1', 'divide');
        this.visitNodes(node.children);
        this.emitAppEnd();
        break;
    case defs.tokenIds['MOD']:
        this.emitApp();
        this.emitSym('arith1', 'rem');
        this.visitNodes(node.children);
        this.emitAppEnd();
        break;
    case defs.tokenIds['NOT']:
        this.emitApp();
        this.emitSym('logic1', 'not');
        this.visitNodes(node.children);
        this.emitAppEnd();
        break;
    case defs.tokenIds['BITWISE_NOT']:
        this.emitApp();
        this.emitSym('bitwise1', 'not');
        this.visitNodes(node.children);
        this.emitAppEnd();
        break;
    case defs.tokenIds['UNARY_PLUS']:
        this.emitApp();
        this.emitSym('arith2', 'unary_plus');
        this.visitNodes(node.children);
        this.emitAppEnd();
        break;
    case defs.tokenIds['UNARY_MINUS']:
        this.emitApp();
        this.emitSym('arith1', 'unary_minus');
        this.visitNodes(node.children);
        this.emitAppEnd();
        break;

        // TODO: figure out pre/post-inc/dec

    case defs.tokenIds['INCREMENT']:
        this.emitApp();
        if (node.postfix) {
            this.emitSym('prog2', 'post_increment');
        } else {
            this.emitSym('prog2', 'increment');
        }
        this.visitNodes(node.children);
        this.emitAppEnd();
        break;
    case defs.tokenIds['DECREMENT']:
        this.emitApp();
        if (node.postfix) {
            this.emitSym('prog2', 'post_decrement');
        } else {
            this.emitSym('prog2', 'decrement');
        }
        this.visitNodes(node.children);
        this.emitAppEnd();
        break;

        // ...

    case defs.tokenIds['SCRIPT']:
        break;
    case defs.tokenIds['BLOCK']:
        this.emitApp();
        this.emitSym('prog1', 'block');
        this.visitNodes(node.children);
        this.emitAppEnd();
        break;
    case defs.tokenIds['LABEL']:
        this.emitApp();
        this.emitSym('prog2', 'label');
        compileNode(node.statement);
        this.emitAppEnd();
        break;
    case defs.tokenIds['FOR_IN']:
        this.emitApp();
        this.emitSym('prog2', 'for_each');
	    if (node.varDecl) {
            compileNode(node.varDecl);
	    } else {
            compileNode(node.iterator);
	    }
        compileNode(node.object);
        compileBody(node.body);
        this.emitAppEnd();
        break;
    case defs.tokenIds['CALL']:
        this.emitApp();
        compileNode(node.children[0]);
        if (node.children[1].type == defs.tokenIds['LIST']) {
            this.visitNodes(node.children[1].children);
        } else {
            compileNode(node.children[1]);
        }
        this.emitAppEnd();
        break;
    case defs.tokenIds['NEW_WITH_ARGS']:
        break;
    case defs.tokenIds['ARRAY_INIT']:
        this.emitApp();
        this.emitSym('ecmascript3', 'array');
        this.visitNodes(node.children);
        this.emitAppEnd();
        break;
    case defs.tokenIds['OBJECT_INIT']:
        this.emitDecl();
        this.emitSym('ecmascript3', 'object');
        this.visitNodes(node.children);
        this.emitDeclEnd();
        break;
    case defs.tokenIds['PROPERTY_INIT']:
        this.emitDeclItem();
	emitDeclTerm();
        compileNode(node.children[0]);
	emitDeclTermEnd();
        this.visitNodes(node.children.slice(1));
        this.emitDeclItemEnd();
        break;
    case defs.tokenIds['GETTER']:
        this.emitDecl();
        this.emitSym('ecmascript3', 'get');
        this.visitNodes(node.children);
        this.emitDeclEnd();
        break;
    case defs.tokenIds['SETTER']:
        this.emitDecl();
        this.emitSym('ecmascript3', 'set');
        this.visitNodes(node.children);
        this.emitDeclEnd();
        break;
        //case defs.tokenIds['GROUP']:
        //          this.emitApp();
        //          this.emit Sym('ecmascript4', 'group');
        //          this.visitNodes(node.children);
        //          this.emitAppEnd();
        //          break;
        //case defs.tokenIds['LET_BLOCK']:
        //          this.emitApp();
        //          this.emit Sym('ecmascript4', 'let_block');
        //          this.visitNodes(node.children);
        //          this.emitAppEnd();
        //          break;
        //case defs.tokenIds['ARRAY_COMP']:
        //          this.emitApp();
        //          this.emit Sym('ecmascript4', 'array_comp');
        //          this.visitNodes(node.children);
        //          this.emitAppEnd();
        //          break;
        //case defs.tokenIds['GENERATOR']:
        //          this.emitApp();
        //          this.emit Sym('ecmascript4', 'generator');
        //          this.visitNodes(node.children);
        //          this.emitAppEnd();
        //          break;
        //case defs.tokenIds['COMP_TAIL']:
        //          this.emitApp();
        //          this.emit Sym('ecmascript4', 'comp_tail');
        //          this.visitNodes(node.children);
        //          this.emitAppEnd();
        //          break;
        //case defs.tokenIds['IMPLEMENTS']:
        //          this.emitApp();
        //          this.emit Sym('ecmascript4', 'implements');
        //          this.visitNodes(node.children);
        //          this.emitAppEnd();
        //          break;
        //case defs.tokenIds['INTERFACE']:
        //          this.emitApp();
        //          this.emit Sym('ecmascript4', 'interface');
        //          this.visitNodes(node.children);
        //          this.emitAppEnd();
        //          break;
        //case defs.tokenIds['LET']:
        //          this.emitApp();
        //          this.emit Sym('ecmascript4', 'let');
        //          this.visitNodes(node.children);
        //          this.emitAppEnd();
        //          break;
        //case defs.tokenIds['MODULE']:
        //          this.emitApp();
        //          this.emit Sym('ecmascript4', 'module');
        //          this.visitNodes(node.children);
        //          this.emitAppEnd();
        //          break;
        //case defs.tokenIds['PACKAGE']:
        //          this.emitApp();
        //          this.emit Sym('ecmascript4', 'package');
        //          this.visitNodes(node.children);
        //          this.emitAppEnd();
        //          break;
        //case defs.tokenIds['PRIVATE']:
        //          this.emitApp();
        //          this.emit Sym('ecmascript4', 'private');
        //          this.visitNodes(node.children);
        //          this.emitAppEnd();
        //          break;
        //case defs.tokenIds['PROTECTED']:
        //          this.emitApp();
        //          this.emit Sym('ecmascript4', 'protected');
        //          this.visitNodes(node.children);
        //          this.emitAppEnd();
        //          break;
        //case defs.tokenIds['PUBLIC']:
        //          this.emitApp();
        //          this.emit Sym('ecmascript4', 'public');
        //          this.visitNodes(node.children);
        //          this.emitAppEnd();
        //          break;
        //case defs.tokenIds['STATIC']:
        //          this.emitApp();
        //          this.emit Sym('ecmascript4', 'static');
        //          this.visitNodes(node.children);
        //          this.emitAppEnd();
        //          break;
        //case defs.tokenIds['USE']:
        //          this.emitApp();
        //          this.emit Sym('ecmascript4', 'use');
        //          this.visitNodes(node.children);
        //          this.emitAppEnd();
        //          break;
        //case defs.tokenIds['YIELD']:
        //          this.emitApp();
        //          this.emit Sym('ecmascript4', 'yield');
        //          compileNode(node.value);
        //          this.emitAppEnd();
        //          break;
    case defs.tokenIds['IDENTIFIER']:
        this.emitId(node.value);
        break;
    case defs.tokenIds['NUMBER']:
        this.emitNum(node.value);
        break;
    case defs.tokenIds['STRING']:
        this.emitStr(node.value);
        break;
    case defs.tokenIds['REGEXP']:
        break;

        // Keywords

        //case defs.keywords['else']:
        //    break;
        //case defs.keywords['export']:
        //    break;
        //case defs.keywords['import']:
        //    break;

    case defs.keywords['break']:
        this.emitApp();
        this.emitSym('prog2', 'break');
        this.emitAppEnd();
        break;
    case defs.keywords['case']:
        this.emitDeclItem();
        this.emitDeclTerm();
        compileNode(node.caseLabel);
        this.emitDeclTermEnd();
        this.visitBlocks(node.statements);
        this.emitDeclItemEnd();
        break;
    case defs.keywords['catch']:
	emitDecl();
        this.emitSym('prog2', 'catch');
	compileParam(node.varName);
	this.visitBlocks(node.block);
	emitDeclEnd();
        break;
    case defs.keywords['const']:
        this.emitDecl();
        this.emitSym('ecmascript4', 'const');
        compileVars(node.children);
        this.emitDeclEnd();
        break;
    case defs.keywords['continue']:
        this.emitApp();
        this.emitSym('prog2', 'continue');
        this.emitAppEnd();
        break;
    case defs.keywords['debugger']:
        this.emitApp();
        this.emitSym('ecmascript3', 'debugger');
        this.emitAppEnd();
        break;
    case defs.keywords['default']:
        this.visitBlocks(node.statements);
        break;
    case defs.keywords['delete']:
        this.emitApp();
        this.emitSym('prog2', 'delete');
        this.visitNodes(node.children);
        this.emitAppEnd();
        break;
    case defs.keywords['do']:
        this.emitSym('prog2', 'do_while');
        compileBody(node.body);
        compileNode(node.condition);
        break;
    case defs.keywords['false']:
        this.emitSym('logic1', 'false');
        break;
    //case defs.keywords['finally']:
    case defs.keywords['for']:
        this.emitApp();
        this.emitSym('prog1', 'for');
        compileNode(node.setup);
        compileNode(node.condition);
        compileNode(node.update);
        compileBody(node.body);
        this.emitAppEnd();
        break;
    case defs.keywords['function']:
        break;
    case defs.keywords['if']:
        // TODO: add parameter to force if/cond
        if (node.elsePart && node.elsePart.type == defs.keywords['if']) {
            this.emitDecl();
            this.emitSym('switch2', 'cond');
            var mode;
            for (mode = node; 
                 mode && mode.type == defs.keywords['if']; 
                 mode = mode.elsePart || null) {
                this.emitDeclItem();
                compileNode(mode.condition);
                this.visitBlocks(mode.thenPart); // block
                this.emitDeclItemEnd()
                if (mode.elsePart && mode.elsePart.type != defs.keywords['if']) {
                    this.visitBlocks(mode.elsePart);
					break;
                }
            }
            this.emitDeclEnd();
        } else {
            this.emitApp();
            this.emitSym('prog1', 'if');
            compileNode(node.condition); // if_not?
            compileNode(node.thenPart); // block
            if (node.elsePart) {
                this.emitElem('drox', 'else');
                compileNode(node.elsePart); // if?
                this.emitElemEnd('drox', 'else');
            }
            this.emitAppEnd();
        }
        break;
    case defs.keywords['in']:
        this.emitApp();
        this.emitSym('ecmascript3', 'in');
        this.visitNodes(node.children);
        this.emitAppEnd();
        break;
    case defs.keywords['instanceof']:
        this.emitApp();
        this.emitSym('ecmascript3', 'instanceof');
        this.emitAppEnd();
        break;
    case defs.keywords['new']:
        this.emitApp();
        this.emitSym('prog2', 'new');
        this.visitNodes(node.children);
        this.emitAppEnd();
        break;
    case defs.keywords['null']:
        this.emitSym('prog2', 'null');
        break;
    case defs.keywords['return']:
        break;
    case defs.keywords['switch']:
        this.emitDecl();
        this.emitSym('switch1', 'case');
        compileNode(node.discriminant);
        this.visitNodes(node.cases);
        this.emitDeclEnd();
        break;
    case defs.keywords['this']:
        this.emitSym('ecmascript3', 'this');
        break;
    case defs.keywords['throw']:
        this.emitApp();
        this.emitSym('prog2', 'throw');
        this.visitNodes(node.children);
        this.emitAppEnd();
        break;
    case defs.keywords['true']:
        this.emitSym('logic1', 'true');
        break;
    case defs.keywords['try']:
        break;
    case defs.keywords['typeof']:
        this.emitApp();
        this.emitSym('ecmascript3', 'typeof');
        this.visitNodes(node.children);
        this.emitAppEnd();
        break;
    case defs.keywords['var']:
        this.emitDecl();
        this.emitSym('prog1', 'local_var');
        compileVars(node.children);
        this.emitDeclEnd();
        break;
    case defs.keywords['void']:
        this.emitApp();
        this.emitSym('ecmascript3', 'void');
        this.visitNodes(node.children);
        this.emitAppEnd();
        break;
    case defs.keywords['while']:
        break;
    case defs.keywords['with']:
        break;
    }
    return;
};

function compileBlock(block) {
    if (block.type == defs.tokenIds['BLOCK']
        && block.children.length == 1) {
        this.visit(block.children[0]);
    } else {
        this.visit(block);
    }
}

function compileBlocks(block) {
    if (block.type == defs.tokenIds['BLOCK']) {
        this.visitNodes(block.children);
    } else {
        this.visit(block);
    }
}

function compile(filename, ast) {
    var visitor = new DroVisitor();
    var acornOptions = {
        onComment: visitor.onComment.bind(visitor),
        sourceFile: filename
    };
    var getContents = readFile || load;
    var source = getContents(filename);
    var node = ast.parse(source, acornOptions);

    visitor.visit(node);
}

exports.compile = compile
