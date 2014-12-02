use v6;
class DROX::DROXActions;

our $*SPEC_CONTEXT = False;

constant $DL_ROOT = '<drox:dl
xmlns:drox="http://drosoft.org/ns/drosera"
xmlns:m="http://www.w3.org/1998/Math/MathML"
xmlns:c89="http://drosoft.org/cd/c89#"
xmlns:c99="http://drosoft.org/cd/c99#"
xmlns:c11="http://drosoft.org/cd/c11#"
xmlns:bitwise1="http://drosoft.org/cd/bitwise1#"
xmlns:bitwise3="http://drosoft.org/cd/bitwise3#"
xmlns:arith2="http://drosoft.org/cd/arith2#"
xmlns:arith1="http://www.openmath.org/cd/arith1#"
xmlns:logic1="http://www.openmath.org/cd/logic1#"
xmlns:prog1="http://www.openmath.org/cd/prog1#"
xmlns:prog2="http://drosoft.org/cd/prog2#"
>';

constant $AL_STAG = '<m:apply>';
constant $AL_ETAG = '</m:apply>';
constant $AI_STAG = '<drox:li>';
constant $AI_ETAG = '</drox:li>';
constant $AT_STAG = '<drox:lt>';
constant $AT_ETAG = '</drox:lt>';
constant $AD_STAG = '<drox:ld>';
constant $AD_ETAG = '</drox:ld>';
constant $BL_STAG = '<m:bind>';
constant $BL_ETAG = '</m:bind>';
constant $BG_STAG = '<drox:bvars>';
constant $BG_ETAG = '</drox:bvars>';
constant $BV_STAG = '<m:bvar>';
constant $BV_ETAG = '</m:bvar>';
constant $RT_STAG = '<drox:rt>';
constant $RT_ETAG = '</drox:rt>';
constant $DL_STAG = '<drox:dl>';
constant $DL_ETAG = '</drox:dl>';
constant $DI_STAG = '<drox:di>';
constant $DI_ETAG = '</drox:di>';
constant $DT_STAG = '<drox:dt>';
constant $DT_ETAG = '</drox:dt>';
constant $DD_STAG = '<drox:dd>';
constant $DD_ETAG = '</drox:dd>';
constant $SL_STAG = '<drox:sl>';
constant $SL_ETAG = '</drox:sl>';
constant $SI_STAG = '<drox:si>';
constant $SI_ETAG = '</drox:si>';
constant $ST_STAG = '<drox:st>';
constant $ST_ETAG = '</drox:st>';
constant $SD_STAG = '<drox:sd>';
constant $SD_ETAG = '</drox:sd>';
constant $TL_STAG = '<drox:type>';
constant $TL_ETAG = '</drox:type>';

constant $GENERIC_KW = '<c99:generic/>';

method TOP($/) {
    make $/.values.[0].ast;
}

method ident($/) {
    make '<m:ci>' ~ $<name> ~ '</m:ci>';
}

method universal-character-name:sym<u>($/) {
    make '&#x' ~ $<xdigit>.Str ~ ';'
}

method universal-character-name:sym<U>($/) {
    make '&#x' ~ $<xdigit>.Str ~ ';'
}

method constant:sym<integer>($/) {
    make $<integer-constant>.ast;
}

method constant:sym<floating>($/) {
    make $<floating-constant>.ast;
}

method constant:sym<enumeration>($/) {
    make $<enumeration-constant>.ast;
}

method constant:sym<character>($/) {
    make $<character-constant>.ast;
}

method integer-constant($/) {
    if $<integer-suffix> {
        make 'TODO integer-suffix';
    } else {
        make $<integer-value>.ast;
    }
}

method integer-value:sym<8>($/) {
    make $<octal-constant>.ast;
}

method integer-value:sym<10>($/) {
    make $<decimal-constant>.ast;
}

method integer-value:sym<16>($/) {
    make $<hexadecimal-constant>.ast;
}

method octal-constant($/) {
    if $<odigit> {
        make '<m:cn base="8">' ~ $<odigit>.Str ~ '</m:cn>';
    } else {
        make '<m:cn>0</m:cn>';
    }
}

method decimal-constant($/) {
    make '<m:cn>' ~ $/.Str ~ '</m:cn>';
}

method hexadecimal-constant($/) {
    make '<m:cn base="16">' ~ $<xdigit>.Str ~ '</m:cn>';
}

method floating-constant:radix<10>($/) {
    make ~$/
}

method floating-constant:radix<16>($/) {
    make ~$/
}

method decimal-floating-constant:sym<9.9>($/) {
    make ~$/
}

method decimal-floating-constant:sym<9e9>($/) {
    make ~$/
}

method hexadecimal-floating-constant:sym<F.F>($/) {
    make ~$/
}

method hexadecimal-floating-constant:sym<FpF>($/) {
    make ~$/
}

method fractional-constant:sym<9.9>($/) {
    make ~$/
}

method fractional-constant:sym<9.>($/) {
    make ~$/
}

method hexadecimal-fractional-constant:sym<F.F>($/) {
    make ~$/
}

method hexadecimal-fractional-constant:sym<F.>($/) {
    make ~$/
}

method binary-exponent-part($/) {
    make ~$/
}

method hexadecimal-digit-sequence($/) {
    make ~$/
}

method enumeration-constant($/) {
    make '<m:ci type="enumeration">'
       ~ $<ident><name>.ast
       ~ '</m:ci>';
}

method character-constant:sym<quote>($/) {
    make '<m:cs type="character">'
       ~ (map {$_.Str}, @<c-char-sequence>).join
       ~ '</m:cs>';
}

method character-constant:sym<L>($/) {
    make ~$/
}

method character-constant:sym<u>($/) {
    make ~$/
}

method character-constant:sym<U>($/) {
    make ~$/
}

method string-literal:sym<quote>($/) {
    make '<m:cs>'
       ~ (map {$_.Str}, @<s-char-sequence>).join
       ~ '</m:cs>';
}

method string-literal:sym<L>($/) {
    make ~$/
}

method string-literal:sym<u8>($/) {
    make ~$/
}

method string-literal:sym<u>($/) {
    make ~$/
}

method string-literal:sym<U>($/) {
    make ~$/
}

method s-char:sym<any>($/) {
    make ~$/
}

method s-char:sym<escape>($/) {
    make ~$/
}

method primary-expression:sym<identifier>($/) {
    make $<ident>.ast;
}

method primary-expression:sym<constant>($/) { 
    make $<constant>.ast;
}

method primary-expression:sym<string-literal>($/) { 
    make $<string-literal>.ast;
}

method primary-expression:sym<expression>($/) {
    make $<expression>.ast
}

method primary-expression:sym<generic-selection>($/) { # C11
    make $<generic-selection>.ast
}

method generic-selection($/) {
    make $SL_STAG
       ~ $GENERIC_KW
       ~ $<assignment-expression>.ast
       ~ $<generic-assoc-list>.ast
       ~ $SL_ETAG;
}
method generic-assoc-list($/) {
    make (map {$_.ast}, @<generic-association>).join
}
method generic-association:sym<typename>($/) {
    make $SI_STAG
       ~ $<type-name>.ast
       ~ $<assignment-expression>.ast
       ~ $SI_ETAG;
}
method generic-association:sym<default>($/) {
    make $SD_STAG
       ~ $<assignment-expression>.ast
       ~ $SD_ETAG;
}

method postfix-expression($/) {
    our $ast = $<postfix-expression-first>.ast;

    for (1..($<postfix-expression-rest>.elems)) {
        my $partial = $<postfix-expression-rest>[$_ - 1].ast;
        $ast = $AL_STAG
             ~ $partial[0]
             ~ $ast
             ~ $partial[1..*].join('-') 
             ~ $AL_ETAG;
    }

    make $ast;
}

method postfix-expression-first:sym<primary>($/) {
    make $<primary-expression>.ast;
}

method postfix-expression-first:sym<initializer>($/) {
    make $AL_STAG
       ~ '<prog2:make_literal/>'
       ~ $<type-name>.ast
       ~ $<initializer-list>.ast
       ~ $AL_ETAG;
}

method postfix-expression-rest:sym<[ ]> ($/) {
    make ['<c89:array_selector/>',
          $<expression>.ast];
}

method postfix-expression-rest:sym<( )> ($/) {
    # postfix parenthetical expression aka. calls.

    # We don't need an applier, since our caller has it. 
    # We return the empty string, so when it is 
    # concatenated, our caller skips it.
    make ['', (map {$_.ast}, @<argument-expression-list>).join];
}

method postfix-expression-rest:sym<.>($/) {
    make ['<prog2:namespace_selector/>',
          $<ident>.ast];
}

method postfix-expression-rest:sym«->»($/) {
    make ['<prog2:namespace_dereference/>',
          $<ident>.ast];
}

method postfix-expression-rest:sym<++>($/) {
    make ['<prog2:post_increment/>'];
}

method postfix-expression-rest:sym<-->($/) {
    make ['<prog2:post_increment/>'];
}

method argument-expression-list($/) {
    make (map {$_.ast}, @<assignment-expression>).join;
}

method unary-expression:sym<postfix>($/) {
    make $<postfix-expression>.ast;
}

method unary-expression:sym<++>($/) {
    make $AL_STAG
       ~ '<prog2:pre_increment/>'
       ~ $<unary-expression>.ast
       ~ $AL_ETAG;
}

method unary-expression:sym<-->($/) {
    make $AL_STAG
       ~ '<prog2:pre_decrement/>'
       ~ $<unary-expression>.ast
       ~ $AL_ETAG;
}

method unary-expression:sym<unary-cast>($/) {
    make $AL_STAG
       ~ $<unary-operator>.ast
       ~ $<cast-expression>.ast
       ~ $AL_ETAG;
}

method unary-expression:sym<size-of-expr>($/) {
}

method unary-expression:sym<size-of-type>($/) {
}

method unary-expression:sym<align-of-type>($/) {
}

method unary-operator:sym<&>($/) {
    make '<ref1:referenceof/>';
}

method unary-operator:sym<*>($/) {
    make '<ref1:dereference/>';
}

method unary-operator:sym<+>($/) {
    make '<arith2:unary_plus/>';
}

method unary-operator:sym<->($/) {
    make '<arith1:unary_minus/>';
}

method unary-operator:sym<~>($/) {
    make '<bitwise1:not/>';
}

method unary-operator:sym<!>($/) {
    make '<logic1:not/>';
}

method cast-expression($/) {
    make $<unary-expression>.ast;
    # TODO
}

method cast-operator($/) {
}

method multiplicative-expression($/) {
    make $<cast-expression>[0].ast;
}

method multiplicative-operator:sym<*>($/) {
}

method multiplicative-operator:sym</>($/) {
}

method multiplicative-operator:sym<%>($/) {
}

method additive-expression($/) {
    make $<multiplicative-expression>[0].ast;
}

method additive-operator:sym<+>($/) {
}

method additive-operator:sym<->($/) {
}

method shift-expression($/) {
    make $<additive-expression>[0].ast;
}

method shift-operator:sym«<<»($/) {
}

method shift-operator:sym«>>»($/) {
}

method relational-expression($/) {
    make $<shift-expression>[0].ast;
}

method relational-operator:sym«<»($/) {
}

method relational-operator:sym«>»($/) {
}

method relational-operator:sym«<=»($/) {
}

method relational-operator:sym«>=»($/) {
}

method equality-expression($/) {
    make $<relational-expression>[0].ast;
}

method equality-operator:sym<==>($/) {
}

method equality-operator:sym<!=>($/) {
}

method and-expression($/) {
    make $<equality-expression>[0].ast;
}

method and-operator:sym<&>($/) {
}

method exclusive-or-expression($/) {
    make $<and-expression>[0].ast;
}

method exclusive-or-operator:sym<^>($/) {
}

method inclusive-or-expression($/) {
    make $<exclusive-or-expression>[0].ast;
}

method inclusive-or-operator:sym<|>($/) {
}

method logical-and-expression($/) {
    make $<inclusive-or-expression>[0].ast;
}

method logical-and-operator:sym<&&>($/) {
}

method logical-or-expression($/) {
    make $<logical-and-expression>[0].ast;
}

method logical-or-operator:sym<||>($/) {
    make 'TODO';
}

method conditional-expression($/) {
    if $<expression> {
        make $AL_STAG
           ~ '<prog2:if_exp/>'
           ~ $<logical-or-expression>.ast
           ~ $<expression>[0].ast
           ~ $<conditional-expression>[0].ast
           ~ $AL_ETAG;
    } else {
        make $<logical-or-expression>.ast;
    }
}

method assignment-expression($/) {
    our $ast = $<conditional-expression>.ast;

    for (1..($<unary-expression>.elems)) {
        $ast = $SL_STAG
            ~ $ast
            ~ $<assignment-operator>[$_ - 1].ast
            ~ $<unary-expression>[$_ - 1].ast
            ~ $SL_ETAG;
    }

    make $ast;
}

method assignment-operator:sym<=>($/) {
    make '<prog1:assignment>';
}

method assignment-operator:sym<*=>($/) {
    make '<prog2:assignment_operator>'
       ~ '<arith1:times/>';
}

method assignment-operator:sym</=>($/) {
    make '<prog2:assignment_operator>'
       ~ '<arith1:divide/>';
}

method assignment-operator:sym<%=>($/) {
    make '<prog2:assignment_operator>'
       ~ '<arith1:rem/>';
}

method assignment-operator:sym<+=>($/) {
    make '<prog2:assignment_operator>'
       ~ '<arith1:plus/>';
}

method assignment-operator:sym<-=>($/) {
    make '<prog2:assignment_operator>'
       ~ '<arith1:minus/>';
}

method assignment-operator:sym«<<=»($/) {
    make '<prog2:assignment_operator>'
       ~ '<bitwise3:left_shift/>';
}

method assignment-operator:sym«>>=»($/) {
    make '<prog2:assignment_operator>'
       ~ '<bitwise3:right_shift/>';
}

method assignment-operator:sym<&=>($/) {
    make '<prog2:assignment_operator>'
       ~ '<bitwise1:and/>';
}

method assignment-operator:sym<^=>($/) {
    make '<prog2:assignment_operator>'
       ~ '<bitwise1:xor/>';
}

method assignment-operator:sym<|=>($/) {
    make '<prog2:assignment_operator>'
       ~ '<bitwise1:or/>';
}

method expression($/) {
    make (map {$_.ast}, @<assignment-expression>).join;
}

method constant-expression($/) {
    make $<conditional-expression>.ast;
}

method declaration:sym<declaration>($/) {

    sub is_typedef($/) {
        {
            say "is_typedef()";
            if $<declaration-specifiers><declaration-specifier>[0]<storage-class-specifier><sym>.perl eq 'Any' {
                return False;
            }
            if $<declaration-specifiers><declaration-specifier>[0]<storage-class-specifier><sym>.Str eq 'typedef' {
                return True;
            }
            CATCH {
                return False;
            }
        }
        return False;
    }

    sub is_func($/) {
        {
            say "is_func()";
            #say $<init-declarator-list>[0]<init-declarator>[0]<declarator><direct-declarator><direct-declarator-rest>[0]<parameter-type-list>.perl;
            if $<init-declarator-list>[0]<init-declarator>[0]<declarator><direct-declarator><direct-declarator-rest>[0]<parameter-type-list>.perl eq 'Any' {
                return False;
            }
            CATCH {
                return False;
            }
        }
        return True;
    }

    if is_func($/) {
        our $str = $DL_STAG;
        $str ~= '<c89:function_declaration/>';

        {
            my $params = $<init-declarator-list>[0]<init-declarator>[0]<declarator>;#<direct-declarator><direct-declarator-rest>[0]<parameter-type-list>;
            my $obj = $<init-declarator-list>[0]<init-declarator>[0].ast;
            my $types = $<declaration-specifiers>.ast;

            $str ~= $DT_STAG
                  ~ $obj{'name'}
                  ~ $DT_ETAG;

            if $obj{'type'} {
                $types.push($obj{'type'});
            }
            
            $str ~= $RT_STAG
                  ~ $types.join
                  ~ $RT_ETAG;

            if $obj{'rest'} {
                $str ~= $obj{'rest'};
            }
        }

        $str ~= $DL_ETAG;
        make $str;
    } elsif is_typedef($/) {
        our $str = $DL_STAG;
        $str ~= '<c89:type_definition/>';

        {
            my $types = map {$_.ast}, @<declaration-specifiers><declaration-specifier>[1..*-2];
            my $name = $<declaration-specifiers><declaration-specifier>[*-1].ast;

            $str ~= $DT_STAG
                  ~ $name
                  ~ $DT_ETAG;
            
            $str ~= $types.join;
        }

        $str ~= $DL_ETAG;
        make $str;
    } elsif $<init-declarator-list> {
        say "is_declarator()";
        
        our $str = $DL_STAG;
        $str ~= '<prog1:local_var/>';

        if $<init-declarator-list> {
            $str ~= $DT_STAG;

            my $obj = @<init-declarator-list>[0]<init-declarator>[0].ast;
            my $types = $<declaration-specifiers>.ast;
            
            $str ~= $obj{'name'};

            if $obj{'type'} {
                $types.push($obj{'type'});
            }

            if $obj{'rest'} {
                $types.push($obj{'rest'});
            }

            $str ~= '<drox:btype>'
                  ~ $types.join
                  ~ '</drox:btype>';
                   
            if $obj{'init'} {
                $str ~= '<drox:binit>'
                      ~ $obj{'init'}
                      ~ '</drox:binit>';
            }

            $str ~= $DT_ETAG;
        }

        $str ~= $DL_ETAG;
        make $str;
    } else {
        say "is_other()";
        make $<declaration-specifiers>.ast;
    }
}

method declaration:sym<static_assert>($/) {
    make $<static-assert-declaration>.ast;
}

method declaration-specifiers($/) {
    make (map {$_.ast}, @<declaration-specifier>);
}

method declaration-specifier:sym<storage-class>($/) {
    make $<storage-class-specifier>.ast;
}

method declaration-specifier:sym<type-specifier>($/) {
    make $<type-specifier>.ast;
}

method declaration-specifier:sym<type-qualifier>($/) {
    make $<type-qualifier>.ast;
}

method declaration-specifier:sym<function>($/) {
    make $<function-specifier>.ast;
}

method declaration-specifier:sym<alignment>($/) {
    make $<alignment-specifier>.ast;
}

method init-declarator-list($/) {
    make (map {$_.ast}, @<init-declarator>);
}

method init-declarator($/) {
    my $obj = $<declarator>.ast;
    my $init = False;
    if @<initializer> {
        $obj{'init'} = @<initializer>[0].ast;
    }
    make $obj;
}

method storage-class-specifier:sym<typedef>($/) {
    make '<c89:typedef/>';
}

method storage-class-specifier:sym<extern>($/) {
    make '<c89:extern/>';
}

method storage-class-specifier:sym<static>($/) {
    make '<c89:static/>';
}

method storage-class-specifier:sym<_Thread_local>($/) {
    make '<c99:thread_local/>';
}

method storage-class-specifier:sym<auto>($/) {
    make '<c89:auto/>';
}

method storage-class-specifier:sym<register>($/) {
    make '<c89:register/>';
}

method type-specifier:sym<void>($/) {
    make '<c89:void/>';
}

method type-specifier:sym<char>($/) {
    make '<c89:char/>';
}

method type-specifier:sym<short>($/) {
    make '<c89:short/>';
}

method type-specifier:sym<int>($/) {
    make '<c89:int/>';
}

method type-specifier:sym<long>($/) {
    make '<c89:long/>';
}

method type-specifier:sym<float>($/) {
    make '<c89:float/>';
}

method type-specifier:sym<double>($/) {
    make '<c89:double/>';
}

method type-specifier:sym<signed>($/) {
    make '<c89:signed/>';
}

method type-specifier:sym<unsigned>($/) {
    make '<c89:unsigned/>';
}

method type-specifier:sym<_Bool>($/) {
    make '<c99:bool/>';
}

method type-specifier:sym<_Complex>($/) {
    make '<c99:complex/>';
}

method type-specifier:sym<atomic-type>($/) {
    make $<atomic-type-specifier>.ast;
}

method type-specifier:sym<struct-or-union>($/) {
    make $<struct-or-union-specifier>.ast;
}

method type-specifier:sym<enum-specifier>($/) {
    make $<enum-specifier>.ast;
}

method type-specifier:sym<typedef-name>($/) {
    make $<typedef-name>.ast;
}

method struct-or-union-specifier:sym<spec>($/) {
    say "struct-or-union-specifier:sym<spec>";
    make $AL_STAG
       ~ $<struct-or-union>.ast
       ~ $<ident>.ast
       ~ $AL_STAG;
}

method struct-or-union-specifier:sym<decl>($/) {
    say "struct-or-union-specifier:sym<decl>";
    make $DL_STAG
       ~ $<struct-or-union>.ast
       ~ $DT_STAG
       ~ $<ident>.ast
       ~ $DT_ETAG
       ~ $<struct-declaration-list>.ast
       ~ $DL_ETAG;
}

method struct-or-union:sym<struct>($/) {
    make '<c89:struct/>';
}

method struct-or-union:sym<union>($/) {
    make '<c89:union/>';
}

method struct-declaration-list($/) {
    make (map {$_.ast}, @<struct-declaration>).join;
}

method struct-declaration:sym<struct>($/) {
    say "struct-declaration:sym<struct>";
    say $<struct-declarator-list>.ast;
    say $<struct-declarator-list>.perl;
    say $<specifier-qualifier-list>.ast;
    say $<specifier-qualifier-list>.perl;
    my $name = $<struct-declarator-list>.ast[0].ast{'name'};
    my $decl_type = $<struct-declarator-list>.ast[0].ast{'type'};
    my $base_type = $<specifier-qualifier-list>.ast;
    my $str = "";

    if (1) {
        $str ~= $DI_STAG
            ~ $DT_STAG
            ~ $name
            ~ $DT_ETAG
            ~ ":"
            ~ $decl_type
            ~ ";"
            ~ $base_type
            ~ ","
            ~ $DI_ETAG;
    }

    make $str;
}

sub build-type($obj) {
    note $obj.perl;
    if ($obj.WHAT == Str) {
        return "build-type(Str)";
    }
    my $type = $obj{'type'}.join;
    my $str = $obj{'rest'}.join;
    if ($obj{'type'}.elems > 0) {
        $str = $AL_STAG
            ~ $type
            ~ $str
            ~ $AL_ETAG;
    }
    return $str;
}

#sub build-specifier-qualifier(%obj) {
#    say "build-specifier-qualifier(" ~ %obj.Str ~ ")";
#    if (%obj.WHAT == Str) {
#        return "build-specifier-qualifier(Str)";
#    }
#    say "build-specifier-qualifier(Array)";
#
#    my $type = build-type(%obj);
#    my $name = %obj{'name'};
#    my $str = $DI_STAG
#        ~ $DT_STAG
#        ~ $name
#        ~ $DT_ETAG
#        ~ $TL_STAG
#        ~ $type
#        ~ $TL_ETAG
#        ~ $DI_ETAG;
#
#    return $str;
#}
#
#sub build-struct-declarator(%obj) {
#    note "build-struct-declarator(" ~ %obj.perl ~ ")";
#    #say %obj.WHAT.Str;
#    if (%obj.WHAT == Str) {
#        return "build-struct-declarator(Str)";
#    }
#    #say "build-struct-declarator(Array)";
#
#
#    return $str;
#}

method struct-declaration:sym<static_assert>($/) {
    make $<static-assert-declaration>.ast;
}

method specifier-qualifier-list($/) {
    my $str = (map {$_.ast}, @<specifier-qualifier>).join;
    if (@<specifier-qualifier>.elems != 1) {
        $str = $AL_STAG
             ~ "<c89:specifier_qualifier_list/>"
             ~ $str
             ~ $AL_ETAG;
    }
    make $str;
}

method specifier-qualifier:sym<type-specifier>($/) {
    make $<type-specifier>.ast;
}

method specifier-qualifier:sym<type-qualifier>($/) {
    make $<type-qualifier>.ast;
}

method struct-declarator-list($/) {
    make @<struct-declarator>;
}

method struct-declarator:sym<declarator>($/) {
    make $<declarator>.ast;

    # my $type = $obj{'type'};
    # if ($obj{'type'}.elems > 0) {
    #     $str = $AL_STAG
    #         ~ $type
    #         ~ $str
    #         ~ $AL_ETAG;
    # }
    # 
    # my $type = build-type($obj);
    # my $name = $obj{'name'};
    # my $str = $DI_STAG
    #     ~ $DT_STAG
    #     ~ $name
    #     ~ $DT_ETAG
    #     ~ $TL_STAG
    #     ~ $type
    #     ~ $TL_ETAG
    #     ~ $DI_ETAG;
    # 
    # make $str;
}

# This is rare, but used in modern code
method struct-declarator:sym<bit-declarator>($/) {
    make $DL_STAG
       ~ '<c89:struct_bit_declarator/>'
       ~ $<declarator>.ast;
       ~ $<constant-expression>.ast;
       ~ $DL_ETAG;
}

method enum-specifier:sym<decl>($/) {
    make $DL_STAG
       ~ '<c89:enum_definition/>'
       ~ $DT_STAG
       ~ $<ident>.ast
       ~ $DT_ETAG
       ~ $<enumerator-list>.ast
       ~ $DL_ETAG;
}

method enum-specifier:sym<spec>($/) {
    make $AL_STAG
       ~ '<c89:enum_specifier/>'
       ~ $<ident>.ast
       ~ $AL_ETAG;
}

method enumerator-list($/) {
    make (map {$_.ast}, @<enumerator>).join;
}

method enumerator($/) {
    make $DI_STAG;
       ~ $<enumeration-constant>.ast
       ~ $<constant-expression>.ast
       ~ $DI_ETAG;
}

method atomic-type-specifier:sym<_Atomic>($/) {
    make $AL_STAG
       ~ '<c11:atomic/>'
       ~ $<type-name>.ast
       ~ $AL_ETAG;
}

method type-qualifier:sym<const>($/) {
    make '<c89:const/>';
}

method type-qualifier:sym<restrict>($/) {
    make '<c99:restrict/>';
}

method type-qualifier:sym<volatile>($/) {
    make '<c89:volatile/>';
}

method type-qualifier:sym<_Atomic>($/) {
    make '<c11:atomic/>';
}

method function-specifier:sym<inline>($/) {
    make '<c89:inline/>';
}

method function-specifier:sym<_Noreturn>($/) {
    make '<c11:noreturn/>';
}

method alignment-specifier:sym<type-name>($/) {
    make $AL_STAG
       ~ '<c11:alignas/>'
       ~ $<type-name>.ast
       ~ $AL_ETAG;
}

method alignment-specifier:sym<constant>($/) {
    make $AL_STAG
       ~ '<c11:alignas/>'
       ~ $<constant-expression>.ast
       ~ $AL_ETAG;
}

method declarator:sym<direct>($/) {
    my $obj = $<direct-declarator>.ast;
    my @ptr = map {$_.ast}, @<pointer>;
	make {
		name => $obj{'name'},
		type => @ptr.push($obj{'type'}),
        rest => $obj{'rest'}
	};
}

method direct-declarator($/) {
    my $obj = $<direct-declarator-first>.ast;
    my @rest = map {$_.ast}, @<direct-declarator-rest>;
    make {
        name => $obj{'name'},
        type => $obj{'type'},
        rest => @rest
    };
}

method direct-declarator-first:sym<identifier>($/) {
    make {
        name => $<ident>.ast,
        type => [],
        rest => []
    };
}

method direct-declarator-first:sym<declarator>($/) {
    make $<declarator>.ast;
}

method direct-declarator-rest:sym<b-assignment-expression>($/) {
    make '<c89:array/>';
}

method direct-declarator-rest:sym<b-static-type-qualifier>($/) {
    make "TODO";
}

method direct-declarator-rest:sym<b-type-qualifier-static>($/) {
    make "TODO";
}

method direct-declarator-rest:sym<b-type-qualifier-list>($/) {
    make "TODO";
}

method direct-declarator-rest:sym<p-parameter-type-list>($/) {
    make $<parameter-type-list>.ast;
}

method direct-declarator-rest:sym<p-identifier-list>($/) {
    make (map {$_.ast}, @<identifier-list>).join;
}

method pointer:sym<pointer>($/) {
    if $<type-qualifier-list> {
        make '<c89:pointer/>' ~ (map {$_.ast}, @<type-qualifier-list>).join;
    } else {
        make '<c89:pointer/>';
    }
}

method type-qualifier-list($/) {
    make (map {$_.ast}, @<type-qualifier>).join;
}

method parameter-type-list:sym<end>($/) {
    make $<parameter-list>.ast;
}

method parameter-type-list:sym<...>($/) {
    make $<parameter-list>.ast
       ~ $BV_STAG
       ~ '<c89:ellipsis/>'
       ~ $BV_ETAG;
}

method parameter-list($/) {
    make (map {$_.ast}, @<parameter-declaration>).join;
}

method parameter-declaration:sym<declarator>($/) {
    my $types = $<declaration-specifiers>.ast;
    my $obj = $<declarator>.ast;
    my $str = $BV_STAG;
    $str ~= $obj{'name'};

    if $obj{'type'} {
        $types.push($obj{'type'});
    }

    $str ~= '<drox:btype>'
          ~ $types.join
          ~ '</drox:btype>';

    if $obj{'rest'} {
        $str ~= '<drox:brest>'
              ~ $obj{'rest'}
              ~ '</drox:brest>';
    }

    $str ~= $BV_ETAG;
    make $str;
}

method parameter-declaration:sym<abstract>($/) {
    make "TODO parameter-declaration:abstract";
}

method identifier-list($/) {
    make "TODO";
}

method type-name($/) {
    make "TODO";
}

method abstract-declarator:sym<pointer>($/) {
    make "TODO";
}

method abstract-declarator:sym<direct-abstract>($/) {
    make "TODO";
}

method direct-abstract-declarator($/) {
    make "TODO";
}

method direct-abstract-declarator-first:sym<abstract>($/) {
    make "TODO";
}

method direct-abstract-declarator-rest:sym<b-type-qualifier>($/) {
    make "TODO";
}

method direct-abstract-declarator-rest:sym<b-static-type-qualifier>($/) {
    make "TODO";
}

method direct-abstract-declarator-rest:sym<b-type-qualifier-static>($/) {
    make "TODO";
}

method direct-abstract-declarator-rest:sym<b-*>($/) {
    make "TODO";
}

method direct-abstract-declarator-rest:sym<p-parameter-type-list>($/) {
    make "TODO";
}

method typedef-name($/) {
    make $<ident>.ast;
}

method initializer:sym<assignment>($/) {
    make $<assignment-expression>.ast;
}

method initializer:sym<initializer-list>($/) {
    make $<initializer-list>.ast;
}

method initializer-list($/) {
    make '<m:list>'
        ~ (map {$_.ast}, @<designation-initializer>).join
        ~ '</m:list>';
}

method designation-initializer($/) {
    if $<designation> {
        make 'TODO designation-initializer';
    } else {
        make $<initializer>.ast;
    }
}

method designation($/) {
    make 'TODO designation';
}

method designator-list($/) {
    make $<designator>.join;
}

method designator:sym<.>($/) {
}

method designator:sym<[ ]>($/) {
}

method static-assert-declaration($/) {
   say "static_assert-declaration";
   make $AL_STAG
      ~ "<c11:static_assert/>"
      ~ $AL_ETAG;
}

method statement:sym<labeled>($/) {
    make $<labeled-statement>.ast;
}

method statement:sym<compound>($/) {
    make $<compound-statement>.ast;
}

method statement:sym<expression>($/) {
    make $<expression-statement>.ast;
}

method statement:sym<selection>($/) {
    make $<selection-statement>.ast;
}

method statement:sym<iteration>($/) {
    make $<iteration-statement>.ast;
}

method statement:sym<jump>($/) {
    make $<jump-statement>.ast;
}

method labeled-statement:sym<identifier>($/) {
    make '<prog2:label/>';
}

method labeled-statement:sym<case>($/) {
    make '<drox:si/>';
}

method labeled-statement:sym<default>($/) {
    make '<drox:sd/>';
}

method compound-statement($/) {
    if $<block-item-list> {
        make (map {$_.ast}, @<block-item-list>).join;
    } else {
        make '<prog2:empty/>';
    }
}

method block-item-list($/) {
    make (map {$_.ast}, @<block-item>).join;
}

method block-item:sym<declaration>($/) {
    make $<declaration>.ast;
}

method block-item:sym<statement>($/) {
    make $<statement>.ast;
}

method expression-statement($/) {
    say $/.perl;
    if @<expression> {
        make @<expression>[0].ast;
    } else {
        make '<prog2:empty/>';
    }
}

method selection-statement:sym<if>($/) {
    make $SL_STAG
       ~ '<c89:if/>'
       ~ $<expression>.ast
       ~ '<m:apply><m:csymbol cd="prog1">block</m:csymbol>'
       ~ $<then_statement>.ast
       ~ '</m:apply>'
       ~ '<m:apply><m:csymbol cd="prog1">block</m:csymbol>'
       ~ $<else_statement>.ast
       ~ '</m:apply>'
       ~ $SL_ETAG;
}

method selection-statement:sym<switch>($/) {
    make $SL_STAG
       ~ '<c89:switch/>'
       ~ $<expression>.ast
       ~ $<statement>.ast
       ~ $SL_ETAG;
}

method iteration-statement:sym<while>($/) {
    make $SL_STAG
       ~ '<c89:while/>'
       ~ $<expression>.ast
       ~ $<statement>.ast
       ~ $SL_ETAG;
}

method iteration-statement:sym<do_while>($/) {
    make $SL_STAG
       ~ '<c89:do_while/>'
       ~ $<expression>.ast
       ~ $<statement>.ast
       ~ $SL_ETAG;
}

method iteration-statement:sym<for>($/) {
    make $SL_STAG
       ~ '<c89:for/>'
       ~ $<init>.ast
       ~ $<test>.ast
       ~ $<step>.ast
       ~ $SL_ETAG;
}

method iteration-statement:sym<for_decl>($/) {
    make $SL_STAG
       ~ '<c99:for_decl/>'
       ~ $<init>.ast
       ~ $<test>.ast
       ~ $<step>.ast
       ~ $SL_ETAG;
}

method jump-statement:sym<goto>($/) {
    make $SL_STAG
       ~ '<prog2:goto/>'
       ~ $<ident>.ast
       ~ $SL_ETAG;
}

method jump-statement:sym<continue>($/) {
    make $SL_STAG
       ~ '<prog2:continue/>'
       ~ $SL_ETAG;
}

method jump-statement:sym<break>($/) {
    make $SL_STAG
       ~ '<prog2:break/>'
       ~ $SL_ETAG;
}

method jump-statement:sym<return>($/) {
    make $SL_STAG
       ~ '<prog1:return/>'
       ~ (map {$_.ast}, @<expression>).join
       ~ $SL_ETAG;
}

method external-declaration:sym<function-definition>($/) {
    make $<function-definition>.ast;
}

method external-declaration:sym<declaration>($/) {
    make $<declaration>.ast;
}

method function-definition:sym<modern>($/) {
    say "function-definition:sym<modern>";
    my $types = $<declaration-specifiers>.ast;
    my $obj = $<declarator>.ast;
    our $str = $DL_STAG;
    $str ~= '<c89:function_definition/>';

    $str ~= $DT_STAG
          ~ $obj{'name'}
          ~ $DT_ETAG;

    if ($obj{'type'}:exists) {
        $types.push($obj{'type'})
    }

    $str ~= $RT_STAG
          ~ $types.join
          ~ $RT_ETAG;

    if $obj{'rest'} {
        $str ~= $obj{'rest'}
    }

    $str ~= $<compound-statement>.ast;
    $str ~= $DL_ETAG;

    make $str;
}

method function-definition:sym<ancient>($/) {
    say "function-definition:sym<ancient>";
}

method declaration-list($/) {
    make (map {$_.ast}, @<declaration>).join;
}

method translation-unit($/) {
    make $DL_ROOT
       ~ '<c89:translation_unit/>'
       ~ (map {$_.ast}, @<external-declaration>).join
       ~ $DL_ETAG;
}
