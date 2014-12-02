#ifndef CLANG2DROX_EMIT_H
#define CLANG2DROX_EMIT_H

// emit an XML element start tag, with XML namespace declarations
void
emit_ROOT(const char *prefix, const char *name);

// emit an XML element start tag
void
emit_STAG(const char *prefix, const char *name);

// emit an XML element end tag
void
emit_ETAG(const char *prefix, const char *name);

// emit an XML element tag with no children
void
emit_NTAG(const char *prefix, const char *name);

void
emit_NETAG();

 
//void emit_ROOT(const char *prefix, const char *name);
void emit_SAETAG(const char *prefix, const char *name, const char *attribs, const char *content); 
void emit_SETAG(const char *prefix, const char *name, const char *content); 
void emit_SATAG(const char *prefix, const char *name, const char *attribs);
//void emit_STAG(const char *prefix, const char *name);
//void emit_ETAG(const char *prefix, const char *name); 
//void emit_NTAG(const char *prefix, const char *name); 

#endif /* CLANG2DROX_EMIT_H */

