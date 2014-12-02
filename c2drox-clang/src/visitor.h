#ifndef CLANG2DROX_VISITOR_H
#define CLANG2DROX_VISITOR_H

#include <stdbool.h>
#include <clang-c/Index.h>

typedef CXCursor ds_Cursor;
typedef CXClientData ds_VisitorData;
typedef enum CXChildVisitResult ds_VisitResult;
typedef enum CXCursorKind ds_CursorKind;
typedef enum CXPostChildVisitResult ds_PostVisitResult;

typedef struct ds_Visitor_s {
    const char *filename;
    ds_Cursor cursor;
    ds_Cursor parent;
    bool entering;
} ds_Visitor;

ds_Visitor *
ds_Visitor_new();

ds_Visitor *
ds_Visitor_create(ds_Visitor *, const char *filename);

void
ds_Visitor_delete(ds_Visitor *);

// methods


ds_PostVisitResult
ds_Visitor_visitPost(ds_Cursor cursor, ds_VisitorData client_data);

ds_VisitResult
ds_Visitor_visit(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);

// node-specific

ds_VisitResult ds_Visitor_visitUnknown(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitUnexposedDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitStructDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitUnionDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitClassDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitEnumDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitFieldDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitEnumConstantDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitFunctionDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitVarDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitParmDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitObjCInterfaceDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitObjCCategoryDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitObjCProtocolDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitObjCPropertyDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitObjCIvarDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitObjCInstanceMethodDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitObjCClassMethodDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitObjCImplementationDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitObjCCategoryImplDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitTypedefDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitCXXMethod(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitNamespace(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitLinkageSpec(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitConstructor(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitDestructor(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitConversionFunction(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitTemplateTypeParameter(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitNonTypeTemplateParameter(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitTemplateTemplateParameter(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitFunctionTemplate(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitClassTemplate(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitClassTemplatePartialSpecialization(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitNamespaceAlias(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitUsingDirective(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitUsingDeclaration(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitTypeAliasDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitObjCSynthesizeDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitObjCDynamicDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitCXXAccessSpecifier(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitObjCSuperClassRef(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitObjCProtocolRef(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitObjCClassRef(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitTypeRef(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitCXXBaseSpecifier(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitTemplateRef(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitNamespaceRef(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitMemberRef(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitLabelRef(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitOverloadedDeclRef(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitVariableRef(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitInvalidFile(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitNoDeclFound(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitNotImplemented(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitInvalidCode(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitUnexposedExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitDeclRefExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitMemberRefExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitCallExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitObjCMessageExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitBlockExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitIntegerLiteral(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitFloatingLiteral(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitImaginaryLiteral(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitStringLiteral(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitCharacterLiteral(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitParenExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitUnaryOperator(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitArraySubscriptExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitBinaryOperator(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitCompoundAssignOperator(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitConditionalOperator(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitCStyleCastExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitCompoundLiteralExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitInitListExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitAddrLabelExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitStmtExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitGenericSelectionExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitGNUNullExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitCXXStaticCastExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitCXXDynamicCastExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitCXXReinterpretCastExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitCXXConstCastExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitCXXFunctionalCastExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitCXXTypeidExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitCXXBoolLiteralExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitCXXNullPtrLiteralExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitCXXThisExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitCXXThrowExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitCXXNewExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitCXXDeleteExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitUnaryExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitObjCStringLiteral(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitObjCEncodeExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitObjCSelectorExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitObjCProtocolExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitObjCBridgedCastExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitPackExpansionExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitSizeOfPackExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitLambdaExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitObjCBoolLiteralExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitUnexposedStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitLabelStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitCompoundStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitCaseStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitDefaultStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitIfStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitSwitchStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitWhileStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitDoStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitForStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitGotoStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitIndirectGotoStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitContinueStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitBreakStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitReturnStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitGCCAsmStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitAsmStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitObjCAtTryStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitObjCAtCatchStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitObjCAtFinallyStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitObjCAtThrowStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitObjCAtSynchronizedStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitObjCAutoreleasePoolStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitObjCForCollectionStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitCXXCatchStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitCXXTryStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitCXXForRangeStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitSEHTryStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitSEHExceptStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitSEHFinallyStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitMSAsmStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitNullStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitDeclStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitTranslationUnit(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitUnexposedAttr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitIBActionAttr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitIBOutletAttr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitIBOutletCollectionAttr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitCXXFinalAttr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitCXXOverrideAttr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitAnnotateAttr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitAsmLabelAttr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitPreprocessingDirective(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitMacroDefinition(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitMacroExpansion(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitMacroInstantiation(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitInclusionDirective(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);
ds_VisitResult ds_Visitor_visitModuleImportDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data);

#endif /* CLANG2DROX_VISITOR_H */
