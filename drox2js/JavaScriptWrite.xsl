<?xml version="1.0"?>
<t:stylesheet version="1.0" 
    xmlns:t="http://www.w3.org/1999/XSL/Transform"
    xmlns:js="http://drosoft.org/cd/ecmascript3#">

  <t:strip-space elements="*"/>

  <t:output method="text" omit-xml-declaration="yes" 
	        media-type="text/javascript"/>

  <t:variable name="ECMASCRIPT_VERSION" select="3"/>

  <!-- BEGIN tokens -->
  <t:variable name="DOT" select="'.'"/>
  <t:variable name="SPACE" select="' '"/>
  <t:variable name="SLASH" select="'/'"/>
  <t:variable name="SLASH_SLASH" select="'//'"/>
  <t:variable name="LESSTHAN" select="'&lt;'"/>
  <t:variable name="GREATERTHAN" select="'&gt;'"/>
  <t:variable name="LPAREN" select="'('"/>
  <t:variable name="RPAREN" select="')'"/>
  <t:variable name="NEWLINE">
    <t:text>
</t:text>
  </t:variable>
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



  <t:template match="/">
    <t:apply-templates/>
  </t:template>

  <t:template match="js:script">
    <t:for-each select="*">
      <t:apply-templates select="."/>
      <t:text>
</t:text>
    </t:for-each>
  </t:template>


  <t:template match="js:ci">
    <t:value-of select="text()"/>
<!--
    <t:param name="tabs" select="''"/>
    <t:choose>
      <t:when test="position()=1 and local-name(..)='apply'">
      </t:when>
      <t:otherwise>
      </t:otherwise>
    </t:choose>
-->
  </t:template>

  <t:template match="js:cn">
    <t:value-of select="text()[1]"/>
  </t:template>

  <t:template match="js:cs">
    <t:choose>
      <t:when test="@type = 'double'">
	<t:text>"</t:text>
	<t:value-of select="text()"/>
	<t:text>"</t:text>
      </t:when>
      <t:otherwise>
	<t:text>'</t:text>
	<t:value-of select="text()"/>
	<t:text>'</t:text>
      </t:otherwise>
    </t:choose>
  </t:template>

  <t:template match="js:dd">
    <t:param name="tabs" select="''"/>
    <t:apply-templates>
      <t:with-param name="tabs" select="$tabs"/>
    </t:apply-templates>
  </t:template>

  <t:template match="js:di">
    <t:param name="tabs" select="''"/>
    <t:value-of select="$tabs"/>
    <t:apply-templates>
      <t:with-param name="tabs" select="$tabs"/>
    </t:apply-templates>
    <t:if test="not(position()=last())">
      <t:text>,
</t:text>
    </t:if>
  </t:template>

  <t:template match="js:dl">
    <t:param name="tabs" select="''"/>
    <t:text>{
</t:text>
    <t:apply-templates>
      <t:with-param name="tabs" select="concat($tabs, '    ')"/>
    </t:apply-templates>
    <t:text>
}</t:text>
  </t:template>

  <t:template match="js:dt">
    <t:param name="tabs" select="''"/>
    <t:value-of select="text()"/>
    <t:text>: </t:text>
  </t:template>

  <t:template match="js:false">
    <t:text>null</t:text>
  </t:template>

  <t:template match="js:true">
    <t:text>null</t:text>
  </t:template>

  <t:template match="js:null">
    <t:text>null</t:text>
  </t:template>

  <t:template match="js:list">
    <t:text>[</t:text>
    <t:for-each select="*">
      <t:apply-templates select="."/>
      <t:if test="not(position()=last())">
	<t:text>, </t:text>
      </t:if>
    </t:for-each>
    <t:text>]</t:text>
  </t:template>

  <t:template match="js:apply">
    <t:param name="tabs" select="''"/>
    <t:choose>
      <t:when test="local-name(*[position()=1])='lambda'">
	<t:text>(</t:text>
	<t:apply-templates select="*[position()=1]">
	  <t:with-param name="tabs" select="$tabs"/>
	</t:apply-templates>
	<t:text>)</t:text>
	<t:call-template name="standard-lambda-expr">
	  <t:with-param name="tabs" select="$tabs"/>
	  <t:with-param name="context" select="."/>
	</t:call-template>
      </t:when>
      <!-- assume csymbol -->
      <t:otherwise>
	<t:apply-templates select="*[position()=1]">
	  <t:with-param name="tabs" select="$tabs"/>
	</t:apply-templates>
      </t:otherwise>
    </t:choose>
  </t:template>

  <t:template name="common-lambda-function">
  </t:template>

  <t:template match="js:lambda">
    <t:param name="tabs" select="''"/>
    <t:text>function </t:text>
    <t:text>(</t:text>
    <t:for-each select="js:bvar">
      <t:apply-templates select="."/>
      <t:if test="not(position()=last())">
	<t:text>, </t:text>
      </t:if>
    </t:for-each>
    <t:text>) {</t:text>
    <t:for-each select="*[not(local-name()='bvar')]">
      <t:text>
</t:text>
      <t:apply-templates select=".">
	<t:with-param name="tabs" select="concat($tabs, '    ')"/>
      </t:apply-templates>
      <t:text>;</t:text>
    </t:for-each>
    <t:text>
</t:text>
    <t:value-of select="$tabs"/>
    <t:text>}</t:text>
  </t:template>
<!--
  <t:template match="js:function">
    <t:text>function </t:text>
    <t:apply-templates select="*[1]"/>
    <t:text>(</t:text>
    <t:for-each select="js:bvar">
      <t:apply-templates select="."/>
      <t:if test="not(position()=last())">
	<t:text>, </t:text>
      </t:if>
    </t:for-each>
    <t:for-each select="js:bvar">
      <t:apply-templates select="."/>
    </t:for-each>
  </t:template>
-->
  <t:template name="standard-function-expr">
    <t:param name="tabs" select="''"/>
    <t:param name="context"/>
    <t:value-of select="$tabs"/>
    <t:value-of select="$context/*[1]/text()"/>
    <t:text>(</t:text>
    <t:for-each select="$context/*[not(position()=1)]">
      <t:apply-templates select="."/>
      <t:if test="not(position()=last())">
	<t:text>, </t:text>
      </t:if>
    </t:for-each>
    <t:text>)</t:text>
  </t:template>

  <t:template name="standard-lambda-expr">
    <t:param name="tabs" select="''"/>
    <t:param name="context"/>
    <t:value-of select="$tabs"/>
    <t:text>(</t:text>
    <t:for-each select="$context/*[not(position()=1)]">
      <t:apply-templates select="."/>
      <t:if test="not(position()=last())">
	<t:text>, </t:text>
      </t:if>
    </t:for-each>
    <t:text>)</t:text>
  </t:template>

  <t:template name="standard-keyword-stmt">
    <t:param name="tabs" select="''"/>
    <t:param name="context"/>
    <t:value-of select="$tabs"/>
    <t:value-of select="local-name($context/*[1])"/>
    <t:text> </t:text>
    <t:for-each select="$context/*[not(position()=1)]">
      <t:apply-templates select="."/>
      <t:if test="not(position()=last())">
	<t:text>, </t:text>
      </t:if>
    </t:for-each>
  </t:template>

  <t:template match="js:return">
    <t:param name="tabs" select="''"/>
    <t:call-template name="standard-keyword-stmt">
      <t:with-param name="tabs" select="$tabs"/>
      <t:with-param name="context" select=".."/>
    </t:call-template>
  </t:template>

  <t:template match="js:csymbol" mode="delete" priority="9">
    <t:param name="tabs" select="''"/>
    <t:call-template name="standard-function-expr">
      <t:with-param name="tabs" select="$tabs"/>
      <t:with-param name="context" select=".."/>
    </t:call-template>
  </t:template>

</t:stylesheet>
