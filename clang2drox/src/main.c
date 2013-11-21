#include "visitor.h"

int
main(int argc, char ** argv)
{
    if (argc < 2) {
        puts("not enough args");
        return 1;
    }
    char *filename = argv[1];

    // This is pretty standard clang setup
    CXIndex index = clang_createIndex(1, 0);
    CXTranslationUnit unit = clang_createTranslationUnitFromSourceFile(index, filename, 0, NULL, 0, NULL);
    CXCursor cursor = clang_getTranslationUnitCursor(unit);
    ds_Visitor *visitor = ds_Visitor_create(ds_Visitor_new(), filename);

    // This requires a patch, included in this directory, which adds this function
    // to the clang-C API, and provides a function type and enumeration to go with it.
    ds_Visitor_visitTranslationUnit(cursor, cursor, visitor);
    //clang_visitChildrenWithPost(cursor, &ds_Visitor_visit, &ds_Visitor_visitPost, visitor);

    ds_Visitor_delete(visitor);
    clang_disposeTranslationUnit(unit);
    return 0;
}
