#include "PostChildVisitor.h"

#define __STDC_LIMIT_MACROS
#define __STDC_CONSTANT_MACROS
#include "../llvm/tools/clang/tools/libclang/CursorVisitor.h"

//extern "C" {

unsigned clang_visitChildrenWithPost(CXCursor parent,
                                     CXCursorVisitor visitor,
                                     CXPostChildrenVisitor post_visitor,
                                     CXClientData client_data) {
    clang::cxcursor::CursorVisitor CursorVis(clang_Cursor_getTranslationUnit(parent), visitor, client_data,
                          /*VisitPreprocessorLast=*/false,
                          /*VisitIncludedPreprocessingEntries=*/false,
                          /*RegionOfInterest=*/clang::SourceRange(),
                          /*VisitDeclsOnly=*/false,
                          /*PostChildrenVisitor=*/post_visitor);
    return CursorVis.VisitChildren(parent);
}

//} /* extern "C" */
