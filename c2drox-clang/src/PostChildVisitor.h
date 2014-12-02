#ifndef LLVM_CLANG_LIBCLANG_POSTCHILDVISITOR_H
#define LLVM_CLANG_LIBCLANG_POSTCHILDVISITOR_H

#include <clang-c/Index.h>

typedef bool CXPostChildVisitResult;
bool CXPostChildVisit_Continue = false;
bool CXPostChildVisit_Break = true;

#ifdef __cplusplus
extern "C" {
#endif

// copy of
// clang::cxcursor::CursorVisitor::PostChildrenVisitorTy
typedef CXPostChildVisitResult (*CXPostChildrenVisitor)(CXCursor cursor,
                                                        CXClientData client_data);

unsigned clang_visitChildrenWithPost(CXCursor parent,
                                     CXCursorVisitor visitor,
                                     CXPostChildrenVisitor post_visitor,
                                     CXClientData client_data);

#ifdef __cplusplus
}
#endif

#endif
