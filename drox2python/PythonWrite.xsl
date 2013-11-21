<?xml version="1.0"?>
<t:stylesheet version="1.0" 
    xmlns:t="http://www.w3.org/1999/XSL/Transform"
    xmlns:m="http://www.w3.org/1998/Math/MathML"
    xmlns:py="http://drosoft.org/ns/drosera/pythonxml"
    xmlns:drox="http://drosoft.org/ns/drosera">

  <t:strip-space elements="*"/>

  <t:output method="text" omit-xml-declaration="yes" 
	        media-type="text/python"/>

  <t:variable name="PYTHON_MAJOR_VERSION" select="2"/>

  <!-- BEGIN tokens -->
  <t:variable name="NEWLINE">
    <t:text>
</t:text>
  </t:variable>
  <t:variable name="DOT" select="'.'"/>
  <t:variable name="SPACE" select="' '"/>
  <t:variable name="SLASH" select="'/'"/>
  <t:variable name="SLASH_SLASH" select="'//'"/>
  <t:variable name="LESSTHAN" select="'&lt;'"/>
  <t:variable name="GREATERTHAN" select="'&gt;'"/>
  <t:variable name="LPAREN" select="'('"/>
  <t:variable name="RPAREN" select="')'"/>
  <t:variable name="COMMA" select="','"/>
  <t:variable name="COMMA_SPACE">
    <t:value-of select="$COMMA"/>
    <t:value-of select="$SPACE"/>
  </t:variable>
  <t:variable name="COMMA_NEWLINE">
    <t:value-of select="$COMMA"/>
    <t:value-of select="$NEWLINE"/>
  </t:variable>
  <t:variable name="QUOTE">
    <t:text>'</t:text>
  </t:variable>
  <t:variable name="DOUBLEQUOTE">
    <t:text>"</t:text>
  </t:variable>
  <t:variable name="LBRACE" select="'{'"/>
  <t:variable name="RBRACE" select="'}'"/>
  <t:variable name="LBRACKET" select="'['"/>
  <t:variable name="RBRACKET" select="']'"/>
  <t:variable name="DOLLAR" select="'$'"/>
  <t:variable name="MINUS" select="'-'"/>
  <t:variable name="PLUS" select="'+'"/>
  <t:variable name="EQUAL" select="'='"/>
  <t:variable name="COLON" select="':'"/>
  <t:variable name="COLON_SPACE">
    <t:value-of select="$COLON"/>
    <t:value-of select="$SPACE"/>
  </t:variable>
  <t:variable name="COLON_NEWLINE">
    <t:value-of select="$COLON"/>
    <t:value-of select="$NEWLINE"/>
  </t:variable>
  <t:variable name="SEMICOLON" select="';'"/>
  <t:variable name="TAB" select="'    '"/>
  <!-- END tokens -->

  <!-- BEGIN named templates -->

  <t:template name="standard-call-args">
    <t:param name="indent" select="''"/>
    <t:param name="context"/>
    <t:text>(</t:text>
    <t:call-template name="standard-stmt-args">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select="$context"/>
    </t:call-template>
    <t:text>)</t:text>
  </t:template>

  <t:template name="standard-call">
    <t:param name="indent" select="''"/>
    <t:param name="context"/>
    <t:value-of select="$indent"/>
	<t:value-of select="$context/*[1]/text()"/>
    <t:call-template name="standard-call-args">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select="$context/*[not(position()=1)]"/>
    </t:call-template>
  </t:template>

  <t:template name="standard-stmt-args">
    <t:param name="indent" select="''"/>
    <t:param name="context"/>
    <t:for-each select="$context">
      <t:apply-templates select="."/>
      <t:if test="not(position()=last())">
        <t:value-of select="$COMMA_SPACE"/>
      </t:if>
    </t:for-each>
  </t:template>

  <t:template name="standard-stmt">
    <t:param name="indent" select="''"/>
    <t:param name="context"/>
    <t:value-of select="$indent"/>
	<t:value-of select="$context/*[1]/text()"/>
    <t:value-of select="$SPACE"/>
    <t:call-template name="standard-stmt-args">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select="$context/*[not(position()=1)]"/>
    </t:call-template>
  </t:template>

  <t:template name="standard-block">
    <t:param name="indent" select="''"/>
    <t:param name="context"/>
    <t:value-of select="$COLON_NEWLINE"/>
    <t:for-each select="$context">
      <t:apply-templates select=".">
        <t:with-param name="indent" select="concat($TAB, $indent)"/>
      </t:apply-templates>
      <t:if test="not(position()=last())">
        <t:value-of select="$NEWLINE"/>
      </t:if>
    </t:for-each>
  </t:template>

  <t:template name="standard-prefix">
    <t:param name="indent" select="''"/>
    <t:param name="context"/>
    <t:param name="operator"/>
    <t:value-of select="$indent"/>
    <t:value-of select="$operator"/>
    <t:apply-templates select="$context/*[2]"/>
  </t:template>

  <t:template name="standard-infix">
    <t:param name="indent" select="''"/>
    <t:param name="context"/>
    <t:param name="operator"/>
    <t:if test="$context[@parens='true']">
      <t:text>(</t:text>
    </t:if>
    <t:apply-templates select="$context/*[2]"/>
    <t:for-each select="$context/*[position() > 2]">
      <t:value-of select="$operator"/>
      <t:apply-templates select="."/>
    </t:for-each>
    <t:if test="$context[@parens='true']">
      <t:text>)</t:text>
    </t:if>
  </t:template>

  <!-- END named templates -->

  <!-- BEGIN match templates -->

  <t:template match="m:csymbol[position()=1 and @cd='python2' and text()='module']">
    <t:param name="indent" select="''"/>
    <t:param name="context" select=".."/>
    <t:value-of select="$indent"/>
    <t:for-each select="$context/*[not(position()=1)]">
      <t:apply-templates select=".">
        <t:with-param name="indent" select="$indent"/>
      </t:apply-templates>
      <t:value-of select="$NEWLINE"/>
    </t:for-each>
  </t:template>

  <t:template match="m:csymbol[position()=1 and @cd='python2' and text()='class']">
    <t:param name="indent" select="''"/>
    <t:param name="context" select=".."/>
    <t:value-of select="$NEWLINE"/>
    <t:value-of select="$indent"/>
	<t:text>class</t:text>
    <t:value-of select="$SPACE"/>
    <t:apply-templates select="$context/drox:dt/*[not(local-name()='base')]"/>
    <t:if test="$context/drox:dt/py:base">
      <t:call-template name="standard-call-args">
        <t:with-param name="indent" select="$indent"/>
        <t:with-param name="context" select="$context/drox:dt/py:base/*"/>
      </t:call-template>
    </t:if>
    <t:call-template name="standard-block">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select="$context/*[position()>2]"/>
    </t:call-template>
  </t:template>

  <t:template match="m:csymbol[position()=1 and @cd='python2' and text()='def']">
    <t:param name="indent" select="''"/>
    <t:param name="context" select=".."/>
    <t:value-of select="$NEWLINE"/>
    <t:value-of select="$indent"/>
	<t:text>def</t:text>
    <t:value-of select="$SPACE"/>
    <t:apply-templates select="$context/drox:dt/*"/>
    <t:call-template name="standard-call-args">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select="$context/m:bvar"/>
    </t:call-template>
    <t:call-template name="standard-block">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select="$context/*[position() > 2 and not(local-name()='bvar')]"/>
    </t:call-template>
  </t:template>

  <!-- Python 3 print function -->
  <t:template match="m:csymbol[position()=1 and @cd='python3' and text()='print']">
    <t:param name="indent" select="''"/>
    <t:param name="context" select=".."/>
    <t:call-template name="standard-call">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select="$context"/>
    </t:call-template>
  </t:template>

  <!-- Python 2 print statement -->
  <t:template match="m:csymbol[position()=1 and @cd='python2' and text()='print']">
    <t:param name="indent" select="''"/>
    <t:param name="context" select=".."/>
    <t:call-template name="standard-stmt">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select="$context"/>
    </t:call-template>
  </t:template>

  <t:template match="m:csymbol[position()=1 and @cd='prog1' and text()='return']">
    <t:param name="indent" select="''"/>
    <t:param name="context" select=".."/>
    <t:call-template name="standard-stmt">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select="$context"/>
    </t:call-template>
  </t:template>

  <t:template match="m:csymbol[position()=1 and @cd='prog2' and text()='delete']">
    <t:param name="indent" select="''"/>
    <t:param name="context" select=".."/>
    <t:value-of select="$indent"/>
	<t:text>del</t:text>
    <t:value-of select="$SPACE"/>
    <t:call-template name="standard-stmt-args">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select="$context"/>
    </t:call-template>
  </t:template>

  <t:template match="m:csymbol[position()=1 and @cd='prog2' and text()='empty']">
    <t:param name="indent" select="''"/>
    <t:value-of select="$indent"/>
    <t:text>pass</t:text>
  </t:template>

  <t:template match="m:csymbol[position()=1 and @cd='prog2' and text()='for_each']">
    <t:param name="indent" select="''"/>
    <t:param name="context" select=".."/>
    <t:value-of select="$indent"/>
    <t:text>for</t:text>
    <t:value-of select="$SPACE"/>
    <t:apply-templates select="$context/m:bvar/*"/>
    <t:value-of select="$SPACE"/>
    <t:text>in</t:text>
    <t:value-of select="$SPACE"/>
    <t:apply-templates select="$context/m:domainofapplication/*"/>
    <t:call-template name="standard-block">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select="$context/*[position()>3]"/>
    </t:call-template>
  </t:template>

  <t:template match="m:csymbol[position()=1 and @cd='prog1' and text()='while']">
    <t:param name="indent" select="''"/>
    <t:param name="context" select=".."/>
    <t:call-template name="standard-stmt">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select="$context"/>
    </t:call-template>
  </t:template>

  <!-- (switch2:cond #di(condition_expr stmt1 stmt2 ...) ... stmt3 stmt4 ...) -->
  <t:template match="m:csymbol[position()=1 and @cd='switch2' and text()='cond']">
    <t:param name="indent" select="''"/>
    <t:param name="context" select=".."/>
    <t:for-each select="$context/drox:di">
      <t:value-of select="$indent"/>
	  <t:choose>
		<t:when test="position()=1">
		  <t:text>if</t:text>
		</t:when>
		<t:otherwise>
		  <t:text>elif</t:text>
		</t:otherwise>
	  </t:choose>
      <t:value-of select="$SPACE"/>
      <t:apply-templates select="*[1]"/>
      <t:call-template name="standard-block">
		<t:with-param name="indent" select="$indent"/>
		<t:with-param name="context" select="*[position()>1]"/>
      </t:call-template>
      <t:value-of select="$NEWLINE"/>
    </t:for-each>
    <t:if test="$context/*[position()>1 and not(local-name()='di')]">
      <t:value-of select="$indent"/>
	  <t:text>else</t:text>
      <t:call-template name="standard-block">
		<t:with-param name="indent" select="$indent"/>
		<t:with-param name="context" select="$context/*[position()>1 and not(local-name()='di')]"/>
      </t:call-template>
    </t:if>
  </t:template>

  <!-- (prog1:if condition_expr block1 block2) -->
  <t:template match="m:csymbol[position()=1 and @cd='prog1' and text()='if']">
    <t:param name="indent" select="''"/>
    <t:param name="context" select=".."/>
    <t:value-of select="$indent"/>
    <t:text>if </t:text>
    <t:apply-templates select="$context/*[2]"/>
    <t:call-template name="standard-block">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select="$context/*[3]"/>
    </t:call-template>
    <t:if test="$context/*[4]">
      <t:value-of select="$indent"/>
      <t:text>else</t:text>
      <t:call-template name="standard-block">
        <t:with-param name="indent" select="$indent"/>
        <t:with-param name="context" select="$context/*[4]"/>
      </t:call-template>
    </t:if>
  </t:template>

  <!-- (prog2:if condition_expr stmt1 stmt2 stmt3 ...) -->
  <t:template match="m:csymbol[position()=1 and @cd='prog2' and text()='if']">
    <t:param name="indent" select="''"/>
    <t:param name="context" select=".."/>
    <t:value-of select="$indent"/>
    <t:text>if </t:text>
    <t:apply-templates select="$context/*[2]"/>
    <t:call-template name="standard-block">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select="$context/*[position() > 2 and not(self::m:apply/m:csymbol[position()=1 and @cd='prog2' and text()='else'])]"/>
    </t:call-template>
    <t:if test="$context/m:apply/m:csymbol[position()=1 and @cd='prog2' and text()='else']">
      <t:value-of select="$NEWLINE"/>
      <t:value-of select="$indent"/>
      <t:text>else</t:text>
      <t:call-template name="standard-block">
        <t:with-param name="indent" select="$indent"/>
        <t:with-param name="context" select="$context/m:apply[*[1][self::m:csymbol[position()=1 and @cd='prog2' and text()='else']]]/*[position() > 1]"/>
      </t:call-template>
    </t:if>
  </t:template>

  <t:template match="m:csymbol[position()=1 and @cd='python2' and text()='with']">
    <t:param name="indent" select="''"/>
    <t:param name="context" select=".."/>
    <t:value-of select="$indent"/>
    <t:text>with</t:text>
    <t:value-of select="$SPACE"/>
    <!-- TODO: handle multiple as -->
    <t:apply-templates select="$context/*[2]"/>
    <t:text> as </t:text>
    <t:apply-templates select="$context/*[3]"/>
    <t:call-template name="standard-block">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select="$context/*[position() > 3]"/>
    </t:call-template>
  </t:template>

  <t:template match="m:csymbol[position()=1 and @cd='prog2' and text()='throw']">
    <t:param name="indent" select="''"/>
    <t:param name="context" select=".."/>
    <t:value-of select="$indent"/>
	<t:text>raise</t:text>
    <t:value-of select="$SPACE"/>
    <t:call-template name="standard-stmt">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select="$context"/>
    </t:call-template>
  </t:template>

  <t:template match="m:csymbol[position()=1 and @cd='prog2' and text()='assert']">
    <t:param name="indent" select="''"/>
    <t:param name="context" select=".."/>
    <t:call-template name="standard-stmt">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select="$context"/>
      <t:with-param name="context" select=".."/>
    </t:call-template>
  </t:template>

  <t:template match="m:csymbol[@cd='prog2' and text()='throw']">
    <t:param name="indent" select="''"/>
    <t:param name="context" select=".."/>
    <t:call-template name="standard-stmt">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select="$context"/>
    </t:call-template>
  </t:template>

  <t:template match="m:csymbol[position()=1 and @cd='python2' and text()='import']">
    <t:param name="indent" select="''"/>
    <t:param name="context" select=".."/>
    <t:call-template name="standard-stmt">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select="$context"/>
    </t:call-template>
  </t:template>

  <t:template match="m:csymbol[position()=1 and @cd='python2' and text()='import_from']">
    <t:param name="indent" select="''"/>
    <t:param name="context" select=".."/>
    <t:value-of select="$indent"/>
    <t:text>from </t:text>
    <t:value-of select="$context/*[2]"/>
    <t:text> import </t:text>
    <t:value-of select="$context/*[3]"/>
  </t:template>

  <t:template match="m:csymbol[position()=1 and @cd='python2' and text()='args']">
    <t:param name="indent" select="''"/>
    <t:param name="context" select=".."/>
    <t:text>*</t:text>
    <t:apply-templates select="$context/*[2]"/>
  </t:template>

  <t:template match="m:csymbol[position()=1 and @cd='python2' and text()='kwargs']">
    <t:param name="indent" select="''"/>
    <t:param name="context" select=".."/>
    <t:text>**</t:text>
    <t:apply-templates select="$context/*[2]"/>
  </t:template>




  <t:template match="m:csymbol[position()=1 and @cd='python2' and text()='selector']">
    <t:param name="indent" select="''"/>
    <t:param name="context" select=".."/>
    <t:apply-templates select="$context/*[2]"/>
    <!-- TODO: aug_assign -->
    <t:text>[</t:text>
    <t:apply-templates select="$context/*[3]"/>
    <t:text>]</t:text>
  </t:template>

  <t:template match="m:csymbol[position()=1 and @cd='prog1' and text()='assignment']">
    <t:param name="indent" select="''"/>
    <t:param name="context" select=".."/>
    <t:value-of select="$indent"/>
    <t:apply-templates select="$context/*[2]"/>
    <!-- TODO: aug_assign -->
    <t:text> = </t:text>
    <t:apply-templates select="$context/*[3]"/>
  </t:template>

  <t:template match="m:csymbol[position()=1 and @cd='logic1' and text()='and']">
    <t:param name="indent" select="''"/>
    <t:call-template name="standard-infix">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select=".."/>
      <t:with-param name="operator" select="' and '"/>
    </t:call-template>
  </t:template>

  <t:template match="m:csymbol[position()=1 and @cd='logic1' and text()='or']">
    <t:param name="indent" select="''"/>
    <t:call-template name="standard-infix">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select=".."/>
      <t:with-param name="operator" select="' or '"/>
    </t:call-template>
  </t:template>

  <t:template match="m:csymbol[position()=1 and @cd='logic1' and text()='not']">
    <t:param name="indent" select="''"/>
    <t:call-template name="standard-prefix">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select=".."/>
      <t:with-param name="operator" select="'not '"/>
    </t:call-template>
  </t:template>

  <!-- Python Add -->
  <!-- Python UAdd -->
  <t:template match="m:csymbol[position()=1 and @cd='arith2' and text()='plus']">
    <t:param name="indent" select="''"/>
    <t:call-template name="standard-infix">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select=".."/>
      <t:with-param name="operator" select="' + '"/>
    </t:call-template>
  </t:template>

  <!-- Python Sub -->
  <!-- Python USub -->
  <t:template match="m:csymbol[position()=1 and @cd='arith1' and text()='minus']">
    <t:param name="indent" select="''"/>
    <t:call-template name="standard-infix">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select=".."/>
      <t:with-param name="operator" select="' - '"/>
    </t:call-template>
  </t:template>

  <t:template match="m:csymbol[position()=1 and @cd='arith1' and text()='times']">
    <t:param name="indent" select="''"/>
    <t:call-template name="standard-infix">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select=".."/>
      <t:with-param name="operator" select="'*'"/>
    </t:call-template>
  </t:template>

  <t:template match="m:csymbol[position()=1 and @cd='python2' and text()='divide']">
    <t:param name="indent" select="''"/>
    <t:call-template name="standard-infix">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select=".."/>
      <t:with-param name="operator" select="'/'"/>
    </t:call-template>
  </t:template>

  <t:template match="m:csymbol[position()=1 and @cd='rounding_rtn' and text()='remainder']">
    <t:param name="indent" select="''"/>
    <t:call-template name="standard-infix">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select=".."/>
      <t:with-param name="operator" select="' % '"/>
    </t:call-template>
  </t:template>

  <t:template match="m:csymbol[position()=1 and @cd='arith1' and text()='power']">
    <t:param name="indent" select="''"/>
    <t:call-template name="standard-infix">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select=".."/>
      <t:with-param name="operator" select="' ** '"/>
    </t:call-template>
  </t:template>

  <t:template match="m:csymbol[position()=1 and @cd='bitwise3' and text()='left_shift']">
    <t:param name="indent" select="''"/>
    <t:call-template name="standard-infix">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select=".."/>
      <t:with-param name="operator" select="' &lt;&lt; '"/>
    </t:call-template>
  </t:template>

  <t:template match="m:csymbol[position()=1 and @cd='bitwise3' and text()='right_shift']">
    <t:param name="indent" select="''"/>
    <t:call-template name="standard-infix">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select=".."/>
      <t:with-param name="operator" select="' &gt;&gt; '"/>
    </t:call-template>
  </t:template>

  <t:template match="m:csymbol[position()=1 and @cd='bitwise1' and text()='and']">
    <t:param name="indent" select="''"/>
    <t:call-template name="standard-infix">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select=".."/>
      <t:with-param name="operator" select="' &amp; '"/>
    </t:call-template>
  </t:template>

  <t:template match="m:csymbol[position()=1 and @cd='bitwise1' and text()='or']">
    <t:param name="indent" select="''"/>
    <t:call-template name="standard-infix">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select=".."/>
      <t:with-param name="operator" select="' | '"/>
    </t:call-template>
  </t:template>

  <t:template match="m:csymbol[position()=1 and @cd='bitwise1' and text()='xor']">
    <t:param name="indent" select="''"/>
    <t:call-template name="standard-infix">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select=".."/>
      <t:with-param name="operator" select="' ^ '"/>
    </t:call-template>
  </t:template>

  <t:template match="m:csymbol[position()=1 and @cd='rounding_rtn' and text()='quotient']">
    <t:param name="indent" select="''"/>
    <t:call-template name="standard-infix">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select=".."/>
      <t:with-param name="operator" select="' // '"/>
    </t:call-template>
  </t:template>

  <t:template match="m:csymbol[position()=1 and @cd='bitwise1' and text()='not']">
    <t:param name="indent" select="''"/>
    <t:call-template name="standard-prefix">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select=".."/>
      <t:with-param name="operator" select="'~ '"/>
    </t:call-template>
  </t:template>

  <t:template match="m:csymbol[position()=1 and @cd='relation1' and text()='eq']">
    <t:param name="indent" select="''"/>
    <t:call-template name="standard-infix">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select=".."/>
      <t:with-param name="operator" select="' == '"/>
    </t:call-template>
  </t:template>

  <t:template match="m:csymbol[position()=1 and @cd='relation1' and text()='neq']">
    <t:param name="indent" select="''"/>
    <t:call-template name="standard-infix">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select=".."/>
      <t:with-param name="operator" select="' != '"/>
    </t:call-template>
  </t:template>

  <t:template match="m:csymbol[position()=1 and @cd='relation1' and text()='lt']">
    <t:param name="indent" select="''"/>
    <t:call-template name="standard-infix">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select=".."/>
      <t:with-param name="operator" select="' &lt; '"/>
    </t:call-template>
  </t:template>

  <t:template match="m:csymbol[position()=1 and @cd='relation1' and text()='leq']">
    <t:param name="indent" select="''"/>
    <t:call-template name="standard-infix">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select=".."/>
      <t:with-param name="operator" select="' &lt;= '"/>
    </t:call-template>
  </t:template>

  <t:template match="m:csymbol[position()=1 and @cd='relation1' and text()='gt']">
    <t:param name="indent" select="''"/>
    <t:call-template name="standard-infix">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select=".."/>
      <t:with-param name="operator" select="' &gt; '"/>
    </t:call-template>
  </t:template>

  <t:template match="m:csymbol[position()=1 and @cd='relation1' and text()='geq']">
    <t:param name="indent" select="''"/>
    <t:call-template name="standard-infix">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select=".."/>
      <t:with-param name="operator" select="' &gt;= '"/>
    </t:call-template>
  </t:template>

  <t:template match="m:csymbol[position()=1 and @cd='python2' and text()='is']">
    <t:param name="indent" select="''"/>
    <t:call-template name="standard-infix">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select=".."/>
      <t:with-param name="operator" select="' is '"/>
    </t:call-template>
  </t:template>

  <t:template match="m:csymbol[position()=1 and @cd='python2' and text()='isnot']">
    <t:param name="indent" select="''"/>
    <t:call-template name="standard-infix">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select=".."/>
      <t:with-param name="operator" select="' is not '"/>
    </t:call-template>
  </t:template>

  <t:template match="m:csymbol[position()=1 and @cd='set1' and text()='in']">
    <t:param name="indent" select="''"/>
    <t:call-template name="standard-infix">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select=".."/>
      <t:with-param name="operator" select="' in '"/>
    </t:call-template>
  </t:template>

  <t:template match="m:csymbol[position()=1 and @cd='set1' and text()='notin']">
    <t:param name="indent" select="''"/>
    <t:call-template name="standard-infix">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select=".."/>
      <t:with-param name="operator" select="' not in '"/>
    </t:call-template>
  </t:template>

  <!--
  <t:template match="m:csymbol">
    <t:param name="indent" select="''"/>
    <t:call-template name="standard-args">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select=".."/>
    </t:call-template>
  </t:template>
  -->

  <t:template match="m:csymbol[position()=1 and @cd='python2' and text()='tuple']">
    <t:param name="indent" select="''"/>
    <t:param name="context" select=".."/>
    <t:text>(</t:text>
    <t:call-template name="standard-stmt-args">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select="../*[position() > 1]"/>
    </t:call-template>
    <t:text>)</t:text>
  </t:template>

  <t:template match="m:csymbol[position()=1 and @cd='python2' and text()='list']">
    <t:param name="indent" select="''"/>
    <t:param name="context" select=".."/>
    <t:text>[</t:text>
    <t:call-template name="standard-stmt-args">
      <t:with-param name="indent" select="$indent"/>
      <t:with-param name="context" select="../*[position() > 1]"/>
    </t:call-template>
    <t:text>]</t:text>
  </t:template>

  <t:template match="m:csymbol[@cd='alg1' and text()='zero']">
    <t:text>0</t:text>
  </t:template>

  <t:template match="m:csymbol[@cd='alg1' and text()='one']">
    <t:text>1</t:text>
  </t:template>

  <t:template match="m:csymbol[@cd='prog2' and text()='null']">
    <t:text>None</t:text>
  </t:template>

  <t:template match="m:csymbol[@cd='logic1' and text()='false']">
    <t:text>False</t:text>
  </t:template>

  <t:template match="m:csymbol[@cd='logic1' and text()='true']">
    <t:text>True</t:text>
  </t:template>

  <t:template match="drox:ns">
    <t:value-of select="text()"/>
  </t:template>

  <t:template match="m:ci">
    <t:value-of select="text()"/>
  </t:template>

  <t:template match="m:cs">
    <t:choose>
      <t:when test="contains(text(), $QUOTE)">
		<t:choose>
		  <t:when test="contains(text(), $DOUBLEQUOTE)">
			<t:value-of select="$DOUBLEQUOTE"/>
			<t:value-of select="$DOUBLEQUOTE"/>
			<t:value-of select="$DOUBLEQUOTE"/>
			<t:value-of select="text()"/>
			<t:value-of select="$DOUBLEQUOTE"/>
			<t:value-of select="$DOUBLEQUOTE"/>
			<t:value-of select="$DOUBLEQUOTE"/>
		  </t:when>
		  <t:otherwise>
			<t:value-of select="$DOUBLEQUOTE"/>
			<t:value-of select="text()"/>
			<t:value-of select="$DOUBLEQUOTE"/>
		  </t:otherwise>
		</t:choose>
      </t:when>
      <t:otherwise>
        <t:value-of select="$QUOTE"/>
        <t:value-of select="text()"/>
        <t:value-of select="$QUOTE"/>
      </t:otherwise>
    </t:choose>
  </t:template>

  <!-- BEGIN trivial templates -->

  <t:template match="drox:dl">
    <t:param name="indent" select="''"/>
	<!--t:text>DECL</t:text-->
	<t:apply-templates select="*[1]">
	  <t:with-param name="indent" select="$indent"/>
	</t:apply-templates>
  </t:template>

  <t:template match="m:apply">
    <t:param name="indent" select="''"/>
	<!--t:text>APPLY</t:text-->
    <t:choose>
      <t:when test="local-name(*[1])='ci' or local-name(*[1])='ns'">
        <t:call-template name="standard-call">
          <t:with-param name="indent" select="$indent"/>
          <t:with-param name="context" select="."/>
        </t:call-template>
      </t:when>
      <t:otherwise>
	    <t:apply-templates select="*[1]">
	      <t:with-param name="indent" select="$indent"/>
	    </t:apply-templates>
      </t:otherwise>
    </t:choose>
  </t:template>

  <t:template match="/">
    <t:apply-templates/>
  </t:template>

</t:stylesheet>
