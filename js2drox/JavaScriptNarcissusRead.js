function emitId(name) {
    // TODO: add parameter to force symbol, ci

    switch (name) {
    case 'NaN': 		emitSym('nums1', 'NaN'); break;
    case 'Infinity': 	emitSym('nums1', 'infinity'); break;
    case 'undefined': 	emitSym('ecmascript3', 'undefined'); break;
    case 'arguments': 	emitSym('ecmascript3', 'arguments'); break;
    case 'eval': 		emitSym('ecmascript3', 'eval'); break;
    case 'parseInt': 	emitSym('ecmascript3', 'parseInt'); break;
    case 'parseFloat':  emitSym('ecmascript3', 'parseFloat'); break;
    case 'isNaN': 		emitSym('ecmascript3', 'isNaN'); break;
    case 'isFinite': 	emitSym('ecmascript3', 'isFinite'); break;
    case 'decodeURI': 	emitSym('ecmascript3', 'decodeURI'); break;
    case 'decodeURIComponent': emitSym('ecmascript3', 'decodeURIComponent'); break;
    case 'encodeURI': 	emitSym('ecmascript3', 'encodeURI'); break;
    case 'encodeURIComponent': emitSym('ecmascript3', 'encodeURIComponent'); break;

    default:
        print('<m:ci>' + name + '</m:ci>');
    }
}

function emitNs(names) {
    // TODO: add parameter to force symbol, apply/ci, ns

    var name = names[0].value;
    names.slice(1).forEach(function(nameObj, index){
        name += '.' + nameObj.value;
    }, this);

    switch (name) {
    case 'Math.abs': 	emitSym('arith1', 'abs'); break;
    case 'Math.acos':	emitSym('transc1', 'arccos'); break;
    case 'Math.asin':	emitSym('transc1', 'arcsin'); break;
    case 'Math.atan':	emitSym('transc1', 'arctan'); break;
    case 'Math.atan2':	emitSym('transc2', 'arctan'); break;
    case 'Math.ceil': 	emitSym('rounding1', 'ceiling'); break;
    case 'Math.cos': 	emitSym('transc1', 'cos'); break;
    case 'Math.e': 	emitSym('nums1', 'e'); break;
    case 'Math.exp': 	emitSym('transc1', 'exp'); break;
    case 'Math.floor': 	emitSym('rounding1', 'floor'); break;
    case 'Math.log': 	emitSym('transc1', 'ln'); break;
    case 'Math.max': 	emitSym('minmax1', 'max'); break;
    case 'Math.min': 	emitSym('minmax1', 'min'); break;
    case 'Math.pi': 	emitSym('nums1', 'pi'); break;
    case 'Math.pow': 	emitSym('arith1', 'power'); break;
    case 'Math.random': emitSym('random1', 'random_unit'); break;
    case 'Math.round': 	emitSym('rounding_rnp', 'round'); break;
    case 'Math.sin': 	emitSym('transc1', 'sin'); break;
    case 'Math.sqrt': 	emitSym('transc1', 'sqrt'); break;
    case 'Math.tan': 	emitSym('transc1', 'tan'); break;

    default:
        print('<drox:ns>' + name + '</drox:ns>');
    }
}

function encodeHTML(text) {
	var str = new String(encodeURI(text));
    return str.replace(/&/g, '&amp;')
              .replace(/</g, '&lt;')
              .replace(/>/g, '&gt;')
              .replace(/"/g, '&quot;');
}

function emitNum(value) {
    // TODO: add parameter to force symbol, cn
    switch (value) {
    case 0:
        emitSym('alg1', 'zero');
        break;
    case 1:
        emitSym('alg1', 'one');
        break;
    default:
        print('<m:cn>' + encodeHTML(value) + '</m:cn>');
    }
}

function emitStr(value) {
    print('<m:cs>' + encodeHTML(value) + '</m:cs>');
}

function emitSym(cd, name) {
    print('<m:csymbol cd="' + cd + '">' + name + '</m:csymbol>')
}

function emitElem(prefix, name) {
    print('<' + prefix + ':' + name + '>')
}

function emitElemEnd(prefix, name) {
    print('</' + prefix + ':' + name + '>')
}

// no more print()

function emitApp() {
    emitElem('m', 'apply');
}

function emitAppEnd() {
    emitElemEnd('m', 'apply');
}

function emitBind() {
    emitElem('m', 'bind');
}

function emitBindEnd() {
    emitElemEnd('m', 'bind');
}

function emitStmt() {
    emitElem('drox', 'sl');
}

function emitStmtEnd() {
    emitElemEnd('drox', 'sl');
}

function emitStmtItem() {
    emitElem('drox', 'si');
}

function emitStmtItemEnd() {
    emitElemEnd('drox', 'si');
}

function emitStmtTerm() {
    emitElem('drox', 'st');
}

function emitStmtTermEnd() {
    emitElemEnd('drox', 'st');
}

function emitStmtElse() {
    emitElem('drox', 'sd');
}

function emitStmtElseEnd() {
    emitElemEnd('drox', 'sd');
}

function emitDecl() {
    emitElem('drox', 'dl');
}

function emitDeclEnd() {
    emitElemEnd('drox', 'dl');
}

function emitDeclItem() {
    emitElem('drox', 'di');
}

function emitDeclItemEnd() {
    emitElemEnd('drox', 'di');
}

function emitDeclTerm() {
    emitElem('drox', 'dt');
}

function emitDeclTermEnd() {
    emitElemEnd('drox', 'dt');
}

function emitDeclElse() {
    emitElem('drox', 'dd');
}

function emitDeclElseEnd() {
    emitElemEnd('drox', 'dd');
}

function emitScript() {
    emitElem('drox', 'dl xmlns:drox="http://drosoft.org/ns/drosera" xmlns:m="http://www.w3.org/1998/Math/MathML"');
	emitSym('ecmascript3', 'script');
}

function emitScriptEnd() {
    emitDeclEnd()
}

function compileParam(param, defs) {
    emitElem('m', 'bvar');
    emitId(param);
    emitElemEnd('m', 'bvar');
}

function compileParams(params, defs) {
    params.forEach(function(param, index){
        compileParam(param, defs);
    }, this);
}

function compileBlock1(block, defs) {
    if (block.type == defs.tokenIds['BLOCK']
        && block.children.length == 1) {
        compileNode(block.children[0], defs);
    } else {
        compileNode(block, defs);
    }
}

function compileBlockSeq(block, defs) {
    if (block.type == defs.tokenIds['BLOCK']) {
        compileNodes(block.children, defs);
    } else {
        compileNode(block, defs);
    }
}

function compileBody(body, defs) {
    if (body.type == defs.tokenIds['SCRIPT']) {
        compileNodes(body.children, defs);
    } else {
        compileNode(body, defs);
    }
}

function compileVar(varDecl, defs) {
    emitDeclTerm();
    emitId(varDecl.name);
    emitDeclTermEnd();
    if (varDecl.initializer) {
        compileNode(varDecl.initializer, defs);
    }
}

function compileVars(varDecls, defs) {
    varDecls.forEach(function(varDecl, index){
        emitDeclItem();
        compileVar(varDecl, defs);
        emitDeclItemEnd();
    }, this);
}

function compileAssign(node, defs) {
    if (!node.assignOp) {
        emitSym('prog1', 'assignment');
        emitDeclTerm();
        compileNode(node.children[0], defs);
        emitDeclTermEnd();
        compileNode(node.children[1], defs);
        return false;
    }

    // else
    emitSym('prog2', 'assignment_operator');
    emitDeclTerm();
    compileNode(node.children[0], defs);
    emitDeclTermEnd();
    switch (node.assignOp) {
    case defs.tokenIds['BITWISE_OR']:
        emitSym('bitwise1', 'or');
        break;
    case defs.tokenIds['BITWISE_XOR']:
        emitSym('bitwise1', 'xor');
        break;
    case defs.tokenIds['BITWISE_AND']:
        emitSym('bitwise1', 'and');
        break;
    case defs.tokenIds['LSH']: // <<
        emitSym('bitwise3', 'left_shift');
        break;
    case defs.tokenIds['RSH']: // >>
        emitSym('bitwise3', 'arithmetic_right_shift');
        break;
    case defs.tokenIds['URSH']: // >>>
        emitSym('bitwise3', 'right_shift');
        break;
    case defs.tokenIds['PLUS']:
        emitSym('arith2', 'plus');
        break;
    case defs.tokenIds['MINUS']:
        emitSym('arith1', 'minus');
        break;
    case defs.tokenIds['MUL']:
        emitSym('arith1', 'times');
        break;
    case defs.tokenIds['DIV']:
        emitSym('arith1', 'divide');
        break;
    case defs.tokenIds['MOD']:
        emitSym('arith1', 'rem');
        break;
    }
    compileNode(node.children[1], defs);
    return true;
}

function compileNodes(nodes, defs) {
    nodes.forEach(function(node, index){
        compileNode(node, defs);
    }, this);
}

function compileNode(node, defs) {
    if (!node) {
        emitSym('prog2', 'empty');
        return;
    }

    switch (node.type) {
    case defs.tokenIds['SEMICOLON']: // expression statements
        compileNode(node.expression, defs);
        break;
    case defs.tokenIds['COMMA']: // multiple expressions
        emitApp();
        emitSym('prog2', 'begin');
        compileNodes(node.children, defs);
        emitAppEnd();
        break;
    case defs.tokenIds['ASSIGN']:
        emitDecl();
        compileAssign(node, defs);
        emitDeclEnd();
        break;
    case defs.tokenIds['HOOK']: // a?b:c
        emitApp();
        emitSym('prog2', 'if_exp');
        compileNodes(node.children, defs);
        emitAppEnd();
        break;
        //case defs.tokenIds['COLON']: // never appears
        //    break;
        //case defs.tokenIds['CONDITIONAL']: // never appears
        //    break;
    case defs.tokenIds['OR']:
        emitApp();
        emitSym('logic1', 'or');
        emitAppEnd();
        break;
    case defs.tokenIds['AND']:
        emitApp();
        emitSym('logic1', 'and');
        compileNodes(node.children, defs);
        emitAppEnd();
        break;
    case defs.tokenIds['BITWISE_OR']:
        emitApp();
        emitSym('bitwise1', 'or');
        compileNodes(node.children, defs);
        emitAppEnd();
        break;
    case defs.tokenIds['BITWISE_XOR']:
        emitApp();
        emitSym('bitwise1', 'xor');
        compileNodes(node.children, defs);
        emitAppEnd();
        break;
    case defs.tokenIds['BITWISE_AND']:
        emitApp();
        emitSym('bitwise1', 'and');
        compileNodes(node.children, defs);
        emitAppEnd();
        break;
    case defs.tokenIds['EQ']:
        emitApp();
        emitSym('relation1', 'eq');
        compileNodes(node.children, defs);
        emitAppEnd();
        break;
    case defs.tokenIds['NE']:
        emitApp();
        emitSym('relation1', 'neq');
        compileNodes(node.children, defs);
        emitAppEnd();
        break;
    case defs.tokenIds['STRICT_EQ']:
        emitApp();
        emitSym('ecmascript3', 'strict_eq');
        compileNodes(node.children, defs);
        emitAppEnd();
        break;
    case defs.tokenIds['STRICT_NE']:
        emitApp();
        emitSym('ecmascript3', 'strict_neq');
        compileNodes(node.children, defs);
        emitAppEnd();
        break;
    case defs.tokenIds['LT']:
        emitApp();
        emitSym('relation1', 'lt');
        compileNodes(node.children, defs);
        emitAppEnd();
        break;
    case defs.tokenIds['LE']:
        emitApp();
        emitSym('relation1', 'leq');
        compileNodes(node.children, defs);
        emitAppEnd();
        break;
    case defs.tokenIds['GE']:
        emitApp();
        emitSym('relation1', 'geq');
        compileNodes(node.children, defs);
        emitAppEnd();
        break;
    case defs.tokenIds['GT']:
        emitApp();
        emitSym('relation1', 'gt');
        compileNodes(node.children, defs);
        emitAppEnd();
        break;
    case defs.tokenIds['LSH']: // <<
        emitApp();
        emitSym('bitwise3', 'left_shift');
        compileNodes(node.children, defs);
        emitAppEnd();
        break;
    case defs.tokenIds['RSH']: // >>
        emitApp();
        emitSym('bitwise3', 'arithmetic_right_shift');
        compileNodes(node.children, defs);
        emitAppEnd();
        break;
    case defs.tokenIds['URSH']: // >>>
        emitApp();
        emitSym('bitwise3', 'right_shift');
        compileNodes(node.children, defs);
        emitAppEnd();
        break;
    case defs.tokenIds['PLUS']:
        emitApp();
        emitSym('arith2', 'plus');
        compileNodes(node.children, defs);
        emitAppEnd();
        break;
    case defs.tokenIds['MINUS']:
        emitApp();
        emitSym('arith1', 'minus');
        compileNodes(node.children, defs);
        emitAppEnd();
        break;
    case defs.tokenIds['MUL']:
        emitApp();
        emitSym('arith1', 'times');
        compileNodes(node.children, defs);
        emitAppEnd();
        break;
    case defs.tokenIds['DIV']:
        emitApp();
        emitSym('arith1', 'divide');
        compileNodes(node.children, defs);
        emitAppEnd();
        break;
    case defs.tokenIds['MOD']:
        emitApp();
        emitSym('arith1', 'rem');
        compileNodes(node.children, defs);
        emitAppEnd();
        break;
    case defs.tokenIds['NOT']:
        emitApp();
        emitSym('logic1', 'not');
        compileNodes(node.children, defs);
        emitAppEnd();
        break;
    case defs.tokenIds['BITWISE_NOT']:
        emitApp();
        emitSym('bitwise1', 'not');
        compileNodes(node.children, defs);
        emitAppEnd();
        break;
    case defs.tokenIds['UNARY_PLUS']:
        emitApp();
        emitSym('arith2', 'unary_plus');
        compileNodes(node.children, defs);
        emitAppEnd();
        break;
    case defs.tokenIds['UNARY_MINUS']:
        emitApp();
        emitSym('arith1', 'unary_minus');
        compileNodes(node.children, defs);
        emitAppEnd();
        break;

        // TODO: figure out pre/post-inc/dec

    case defs.tokenIds['INCREMENT']:
        emitApp();
        if (node.postfix) {
            emitSym('prog2', 'post_increment');
        } else {
            emitSym('prog2', 'increment');
        }
        compileNodes(node.children, defs);
        emitAppEnd();
        break;
    case defs.tokenIds['DECREMENT']:
        emitApp();
        if (node.postfix) {
            emitSym('prog2', 'post_decrement');
        } else {
            emitSym('prog2', 'decrement');
        }
        compileNodes(node.children, defs);
        emitAppEnd();
        break;
    case defs.tokenIds['DOT']:
        if (node.children.every(function(name){
            return name.type == defs.tokenIds['IDENTIFIER'];})) {
            emitNs(node.children);
            break;
        }
        emitApp();
        emitSym('prog2', 'namespace_selector');
        compileNodes(node.children, defs);
        emitAppEnd();
        break;

        // ...

    case defs.tokenIds['SCRIPT']:
        emitScript();
        //emitSym('ecmascript3', 'script');
        compileNodes(node.children, defs);
        emitScriptEnd();
        break;
    case defs.tokenIds['BLOCK']:
        emitApp();
        emitSym('prog1', 'block');
        compileNodes(node.children, defs);
        emitAppEnd();
        break;
    case defs.tokenIds['LABEL']:
        emitApp();
        emitSym('prog2', 'label');
        compileNode(node.statement, defs);
        emitAppEnd();
        break;
    case defs.tokenIds['FOR_IN']:
        emitApp();
        emitSym('prog2', 'for_each');
	if (node.varDecl) {
            compileNode(node.varDecl, defs);
	} else {
            compileNode(node.iterator, defs);
	}
        compileNode(node.object, defs);
        compileBody(node.body, defs);
        emitAppEnd();
        break;
    case defs.tokenIds['CALL']:
        emitApp();
        compileNode(node.children[0], defs);
        if (node.children[1].type == defs.tokenIds['LIST']) {
            compileNodes(node.children[1].children, defs);
        } else {
            compileNode(node.children[1], defs);
        }
        emitAppEnd();
        break;
    case defs.tokenIds['NEW_WITH_ARGS']:
        emitApp();
        emitSym('prog2', 'new');
        compileNode(node.children[0], defs);
        if (node.children[1].type == defs.tokenIds['LIST']) {
            compileNodes(node.children[1].children, defs);
        } else {
            compileNode(node.children[1], defs);
        }
        emitAppEnd();
        break;
    case defs.tokenIds['INDEX']:
        emitApp();
        emitSym('ecmascript3', 'selector');
        compileNodes(node.children, defs);
        emitAppEnd();
        break;
    case defs.tokenIds['ARRAY_INIT']:
        emitApp();
        emitSym('ecmascript3', 'array');
        compileNodes(node.children, defs);
        emitAppEnd();
        break;
    case defs.tokenIds['OBJECT_INIT']:
        emitApp();
        emitSym('ecmascript3', 'object');
        compileNodes(node.children, defs);
        emitAppEnd();
        break;
    case defs.tokenIds['PROPERTY_INIT']:
        emitDeclItem();
	    emitDeclTerm();
        compileNode(node.children[0], defs);
	    emitDeclTermEnd();
        compileNodes(node.children.slice(1), defs);
        emitDeclItemEnd();
        break;
    case defs.tokenIds['GETTER']:
        emitDecl();
        emitSym('ecmascript3', 'get');
        compileNodes(node.children, defs);
        emitDeclEnd();
        break;
    case defs.tokenIds['SETTER']:
        emitDecl();
        emitSym('ecmascript3', 'set');
        compileNodes(node.children, defs);
        emitDeclEnd();
        break;
        //case defs.tokenIds['GROUP']:
        //          emitApp();
        //          emit Sym('ecmascript4', 'group');
        //          compileNodes(node.children, defs);
        //          emitAppEnd();
        //          break;
        //case defs.tokenIds['LET_BLOCK']:
        //          emitApp();
        //          emit Sym('ecmascript4', 'let_block');
        //          compileNodes(node.children, defs);
        //          emitAppEnd();
        //          break;
        //case defs.tokenIds['ARRAY_COMP']:
        //          emitApp();
        //          emit Sym('ecmascript4', 'array_comp');
        //          compileNodes(node.children, defs);
        //          emitAppEnd();
        //          break;
        //case defs.tokenIds['GENERATOR']:
        //          emitApp();
        //          emit Sym('ecmascript4', 'generator');
        //          compileNodes(node.children, defs);
        //          emitAppEnd();
        //          break;
        //case defs.tokenIds['COMP_TAIL']:
        //          emitApp();
        //          emit Sym('ecmascript4', 'comp_tail');
        //          compileNodes(node.children, defs);
        //          emitAppEnd();
        //          break;
        //case defs.tokenIds['IMPLEMENTS']:
        //          emitApp();
        //          emit Sym('ecmascript4', 'implements');
        //          compileNodes(node.children, defs);
        //          emitAppEnd();
        //          break;
        //case defs.tokenIds['INTERFACE']:
        //          emitApp();
        //          emit Sym('ecmascript4', 'interface');
        //          compileNodes(node.children, defs);
        //          emitAppEnd();
        //          break;
        //case defs.tokenIds['LET']:
        //          emitApp();
        //          emit Sym('ecmascript4', 'let');
        //          compileNodes(node.children, defs);
        //          emitAppEnd();
        //          break;
        //case defs.tokenIds['MODULE']:
        //          emitApp();
        //          emit Sym('ecmascript4', 'module');
        //          compileNodes(node.children, defs);
        //          emitAppEnd();
        //          break;
        //case defs.tokenIds['PACKAGE']:
        //          emitApp();
        //          emit Sym('ecmascript4', 'package');
        //          compileNodes(node.children, defs);
        //          emitAppEnd();
        //          break;
        //case defs.tokenIds['PRIVATE']:
        //          emitApp();
        //          emit Sym('ecmascript4', 'private');
        //          compileNodes(node.children, defs);
        //          emitAppEnd();
        //          break;
        //case defs.tokenIds['PROTECTED']:
        //          emitApp();
        //          emit Sym('ecmascript4', 'protected');
        //          compileNodes(node.children, defs);
        //          emitAppEnd();
        //          break;
        //case defs.tokenIds['PUBLIC']:
        //          emitApp();
        //          emit Sym('ecmascript4', 'public');
        //          compileNodes(node.children, defs);
        //          emitAppEnd();
        //          break;
        //case defs.tokenIds['STATIC']:
        //          emitApp();
        //          emit Sym('ecmascript4', 'static');
        //          compileNodes(node.children, defs);
        //          emitAppEnd();
        //          break;
        //case defs.tokenIds['USE']:
        //          emitApp();
        //          emit Sym('ecmascript4', 'use');
        //          compileNodes(node.children, defs);
        //          emitAppEnd();
        //          break;
        //case defs.tokenIds['YIELD']:
        //          emitApp();
        //          emit Sym('ecmascript4', 'yield');
        //          compileNode(node.value, defs);
        //          emitAppEnd();
        //          break;
    case defs.tokenIds['IDENTIFIER']:
        emitId(node.value);
        break;
    case defs.tokenIds['NUMBER']:
        emitNum(node.value);
        break;
    case defs.tokenIds['STRING']:
        emitStr(node.value);
        break;
    case defs.tokenIds['REGEXP']:
        emitApp();
        emitSym('ecmascript3', 'regexp');
        var re = defs.source.slice(node.start, node.end);
        emitStr(re);
        emitAppEnd();
        break;

        // Keywords

        //case defs.keywords['else']:
        //    break;
        //case defs.keywords['export']:
        //    break;
        //case defs.keywords['import']:
        //    break;

    case defs.keywords['break']:
        emitApp();
        emitSym('prog2', 'break');
        emitAppEnd();
        break;
    case defs.keywords['case']:
        emitStmtItem();
        emitStmtTerm();
        compileNode(node.caseLabel, defs);
        emitStmtTermEnd();
        compileBlockSeq(node.statements, defs);
        emitStmtItemEnd();
        break;
    case defs.keywords['catch']:
	    emitBind();
        emitSym('prog2', 'catch');
	    compileParam(node.varName);
	    compileBlockSeq(node.block, defs);
	    emitBindEnd();
        break;
    case defs.keywords['const']:
        emitDecl();
        emitSym('ecmascript4', 'const');
        compileVars(node.children, defs);
        emitDeclEnd();
        break;
    case defs.keywords['continue']:
        emitApp();
        emitSym('prog2', 'continue');
        emitAppEnd();
        break;
    case defs.keywords['debugger']:
        emitApp();
        emitSym('ecmascript3', 'debugger');
        emitAppEnd();
        break;
    case defs.keywords['default']:
        compileBlockSeq(node.statements, defs);
        break;
    case defs.keywords['delete']:
        emitApp();
        emitSym('prog2', 'delete');
        compileNodes(node.children, defs);
        emitAppEnd();
        break;
    case defs.keywords['do']:
        emitApp();
        emitSym('prog2', 'do_while');
        compileBody(node.body, defs);
        compileNode(node.condition, defs);
        emitAppEnd();
        break;
    case defs.keywords['false']:
        emitSym('logic1', 'false');
        break;
    //case defs.keywords['finally']:
    case defs.keywords['for']:
        emitApp();
        emitSym('prog1', 'for');
        compileNode(node.setup, defs);
        compileNode(node.condition, defs);
        compileNode(node.update, defs);
        compileBody(node.body, defs);
        emitAppEnd();
        break;
    case defs.keywords['function']:
        switch (node.functionForm) {
        case 2: // parser.STATEMENT_FORM, function
        case 0: // parser.DECLARED_FORM, function
            emitDecl();
            emitSym('ecmascript3', 'function');
            emitDeclTerm()
            emitId(node.name);
            emitDeclTermEnd()
            compileParams(node.params, defs);
            compileBody(node.body, defs);
            emitDeclEnd();
            break;
        case 1: // parser.EXPRESSED_FORM, lambda
            emitBind();
            emitSym('fns1', 'lambda');
            compileParams(node.params, defs);
            compileBody(node.body, defs);
            emitBindEnd();
            break;
        }
        break;
    case defs.keywords['if']:
        // TODO: add parameter to force if/cond
        if (node.elsePart && node.elsePart.type == defs.keywords['if']) {
            emitStmt();
            emitSym('switch2', 'cond');
            var mode;
            for (mode = node; 
                 mode && mode.type == defs.keywords['if']; 
                 mode = mode.elsePart || null) {
                emitStmtItem();
                emitStmtTerm();
                compileNode(mode.condition, defs);
                emitStmtTermEnd();
                compileBlockSeq(mode.thenPart, defs); // block
                emitStmtItemEnd()
                if (mode.elsePart && mode.elsePart.type != defs.keywords['if']) {
                    compileBlockSeq(mode.elsePart, defs);
					break;
                }
            }
            emitStmtEnd();
        } else {
            emitApp();
            emitSym('prog1', 'if');
            compileNode(node.condition, defs); // if_not?
            compileNode(node.thenPart, defs); // block
            if (node.elsePart) {
                emitElem('drox', 'else');
                compileNode(node.elsePart, defs); // if?
                emitElemEnd('drox', 'else');
            }
            emitAppEnd();
        }
        break;
    case defs.keywords['in']:
        emitApp();
        emitSym('ecmascript3', 'in');
        compileNodes(node.children, defs);
        emitAppEnd();
        break;
    case defs.keywords['instanceof']:
        emitApp();
        emitSym('ecmascript3', 'instanceof');
        emitAppEnd();
        break;
    case defs.keywords['new']:
        emitApp();
        emitSym('prog2', 'new');
        compileNodes(node.children, defs);
        emitAppEnd();
        break;
    case defs.keywords['null']:
        emitSym('prog2', 'null');
        break;
    case defs.keywords['return']:
        emitApp();
        emitSym('prog1', 'return');
        if (node.value) {
            compileNode(node.value, defs);
        }
        emitAppEnd();
        break;
    case defs.keywords['switch']:
        emitStmt();
        emitSym('switch1', 'case');
        compileNode(node.discriminant, defs);
        compileNodes(node.cases, defs);
        emitStmtEnd();
        break;
    case defs.keywords['this']:
        emitSym('ecmascript3', 'this');
        break;
    case defs.keywords['throw']:
        emitApp();
        emitSym('prog2', 'throw');
        compileNodes(node.children, defs);
        emitAppEnd();
        break;
    case defs.keywords['true']:
        emitSym('logic1', 'true');
        break;
    case defs.keywords['try']:
        emitApp();
        emitSym('prog2', 'try');
        compileBlock1(node.tryBlock, defs);
        compileNodes(node.catchClauses, defs);
	    if (node.finallyBlock) {
	        emitApp();
            emitSym('prog2', 'finally');
	        compileBlock1(node.finallyBlock, defs);
	        emitAppEnd();
	    }
        emitAppEnd();
        break;
    case defs.keywords['typeof']:
        emitApp();
        emitSym('ecmascript3', 'typeof');
        compileNodes(node.children, defs);
        emitAppEnd();
        break;
    case defs.keywords['var']:
        emitDecl();
        emitSym('prog1', 'local_var');
        compileVars(node.children, defs);
        emitDeclEnd();
        break;
    case defs.keywords['void']:
        emitApp();
        emitSym('ecmascript3', 'void');
        compileNodes(node.children, defs);
        emitAppEnd();
        break;
    case defs.keywords['while']:
        emitApp();
        emitSym('prog1', 'while');
        compileNode(node.condition, defs);
        compileBody(node.body, defs);
        emitAppEnd();
        break;
    case defs.keywords['with']:
        emitApp();
        emitSym('ecmascript3', 'with');
        compileNodes(node.children, defs);
        emitAppEnd();
        break;
    }
    return;
}

function compile(filename, ast) {
    var getContents = readFile || load;
    var source = getContents(filename);
    var node = ast.parser.parse(source, filename, 0);
    var defs = ast.definitions;

    // XXX: but we need the
    // source code for RegExp() objects.
    defs.source = source;
    defs.parser = ast.parser;
    compileNode(node, defs);
}

exports.compile = compile
