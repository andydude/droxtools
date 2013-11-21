parser grammar JavaLexer;

options {
    language = Java;
}

@members {
}

COLON       : ':' ;
COMMA       : ',' ;
SEMI        : ';' ;
LPAREN      : '(' ;
RPAREN      : ')' ;
LT          : '<' ;
GT          ; '>' ;

document
	: declaration*
    | universal*
    | existential
    | statements?
    ;

formulaContent
    : statementList 
    ;

statementList
    : statement statementTail
    ;

statementTail
    : 
    | DOT statementList
    ;

statement
    : declaration
    | universal
    | existential
    | simpleStatement

universal
    : FORALL symbolList
    ;

existential
    : FORSOME symbolList
    ;

declaration
    : BASE explicitURI
    | PREFIX prefix explicitURI
    | KEYWORDS barenameList
    ;

simpleStatement
    : subject propertyList?
    ;

symbolList
    :
    ;

barenameList
    :
    ;

propertyList
    : predicate object objectTail? propertyListTail?
    ;

propertyListTail
    : SEMI propertyList?
    ;

objectTail
    : COMMA object objectTail?
    ;

predicate
    : expression
    | HAS expression
    | IS expression OF
    | A
    | EQ
    | RARROW
    | LARROW
    ;

subject
    : expression
    ;

object
    : expression
    ;

expression
    : pathItem pathTail?
    ;

pathTail
    : BANG expression
    | CARET expression
    ;

pathItem
    : symbol
    | LCURLY formulaContent RCURLY
    | quickVariable
    | numericLiteral
    | literal
    | LBRACKET propertyList? RBRACKET
    | LPAREN pathList RPAREN
    | boolean
    ;

boolean
    : TRUE
    | FALSE
    ;

pathList
    : expression*
    ;

symbol
    : explicitURI
    | qname
    ;

numericLiteral
    : INTEGER
    | RATIONAL
    | DOUBLE
    | DECIMAL
    ;

literal
    : string dtlang?
    ;

dtlang
    : LANG langCode
    | DATATYPE symbol
    ;
