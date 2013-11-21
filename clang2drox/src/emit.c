#include "emit.h"
#include <stdio.h>

void
emit_ROOT(const char *prefix,
          const char *name)
{
    const char *namespaces =
        "xmlns:drox=\"http://drosoft.org/ns/drosera\" "
        "xmlns:m=\"http://www.w3.org/1998/Math/MathML\" "
        "";

    printf("<?xml version=\"1.0\"?>\n");
    emit_SATAG(prefix, name, namespaces);
}

void
emit_SATAG(const char *prefix,
           const char *name,
           const char *attribs)
{
    printf("<%s:%s %s>", prefix, name, attribs);
}

void
emit_STAG(const char *prefix,
          const char *name)
{
    printf("<%s:%s>", prefix, name);
}

void
emit_ETAG(const char *prefix,
          const char *name)
{
    printf("</%s:%s>\n", prefix, name);
}

void
emit_NTAG(const char *prefix,
          const char *name)
{
    printf("<%s:%s/>", prefix, name);
}

void
emit_NETAG()
{
    printf("</>\n");
}

void
emit_SETAG(const char *prefix,
           const char *name,
           const char *content)
{
    printf("<%s:%s>%s</%s:%s>\n", prefix, name, content, prefix, name);
}

void
emit_SAETAG(const char *prefix,
            const char *name,
            const char *attribs,
            const char *content)
{
    printf("<%s:%s %s>%s</%s:%s>\n", prefix, name, attribs, content, prefix, name);
}
