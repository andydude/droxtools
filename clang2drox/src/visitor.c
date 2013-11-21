#include "visitor.h"
#include "emit.h"
#include <stdlib.h>
#include <string.h>

ds_Visitor *
ds_Visitor_new()
{
    return malloc(sizeof(ds_Visitor));
}

ds_Visitor *
ds_Visitor_create(ds_Visitor *my, const char *filename)
{
    my->filename = strdup(filename);
    return my;
}

void
ds_Visitor_delete(ds_Visitor *my)
{
    free((void *)my->filename);
    free((void *)my);
}

// methods

ds_PostVisitResult
ds_Visitor_visitPost(ds_Cursor cursor, ds_VisitorData client_data)
{
    emit_NETAG();
    return CXPostChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visit(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
    ds_Visitor *my = (ds_Visitor *)client_data;

    switch (clang_getCursorKind(cursor)) {
    //case CXCursor_UnexposedDecl: return ds_Visitor_visitUnexposedDecl(cursor, parent, client_data);
	case CXCursor_StructDecl: return ds_Visitor_visitStructDecl(cursor, parent, client_data);
	case CXCursor_UnionDecl: return ds_Visitor_visitUnionDecl(cursor, parent, client_data);
	case CXCursor_ClassDecl: return ds_Visitor_visitClassDecl(cursor, parent, client_data);
	case CXCursor_EnumDecl: return ds_Visitor_visitEnumDecl(cursor, parent, client_data);
	case CXCursor_FieldDecl: return ds_Visitor_visitFieldDecl(cursor, parent, client_data);
	case CXCursor_EnumConstantDecl: return ds_Visitor_visitEnumConstantDecl(cursor, parent, client_data);
	case CXCursor_FunctionDecl: return ds_Visitor_visitFunctionDecl(cursor, parent, client_data);
	case CXCursor_VarDecl: return ds_Visitor_visitVarDecl(cursor, parent, client_data);
	case CXCursor_ParmDecl: return ds_Visitor_visitParmDecl(cursor, parent, client_data);
	//case CXCursor_ObjCInterfaceDecl: return ds_Visitor_visitObjCInterfaceDecl(cursor, parent, client_data);
	//case CXCursor_ObjCCategoryDecl: return ds_Visitor_visitObjCCategoryDecl(cursor, parent, client_data);
	//case CXCursor_ObjCProtocolDecl: return ds_Visitor_visitObjCProtocolDecl(cursor, parent, client_data);
	//case CXCursor_ObjCPropertyDecl: return ds_Visitor_visitObjCPropertyDecl(cursor, parent, client_data);
	//case CXCursor_ObjCIvarDecl: return ds_Visitor_visitObjCIvarDecl(cursor, parent, client_data);
	//case CXCursor_ObjCInstanceMethodDecl: return ds_Visitor_visitObjCInstanceMethodDecl(cursor, parent, client_data);
	//case CXCursor_ObjCClassMethodDecl: return ds_Visitor_visitObjCClassMethodDecl(cursor, parent, client_data);
	//case CXCursor_ObjCImplementationDecl: return ds_Visitor_visitObjCImplementationDecl(cursor, parent, client_data);
	//case CXCursor_ObjCCategoryImplDecl: return ds_Visitor_visitObjCCategoryImplDecl(cursor, parent, client_data);
	case CXCursor_TypedefDecl: return ds_Visitor_visitTypedefDecl(cursor, parent, client_data);
	case CXCursor_CXXMethod: return ds_Visitor_visitCXXMethod(cursor, parent, client_data);
	case CXCursor_Namespace: return ds_Visitor_visitNamespace(cursor, parent, client_data);
	case CXCursor_LinkageSpec: return ds_Visitor_visitLinkageSpec(cursor, parent, client_data);
	case CXCursor_Constructor: return ds_Visitor_visitConstructor(cursor, parent, client_data);
	case CXCursor_Destructor: return ds_Visitor_visitDestructor(cursor, parent, client_data);
	//case CXCursor_ConversionFunction: return ds_Visitor_visitConversionFunction(cursor, parent, client_data);
	//case CXCursor_TemplateTypeParameter: return ds_Visitor_visitTemplateTypeParameter(cursor, parent, client_data);
	//case CXCursor_NonTypeTemplateParameter: return ds_Visitor_visitNonTypeTemplateParameter(cursor, parent, client_data);
	//case CXCursor_TemplateTemplateParameter: return ds_Visitor_visitTemplateTemplateParameter(cursor, parent, client_data);
	//case CXCursor_FunctionTemplate: return ds_Visitor_visitFunctionTemplate(cursor, parent, client_data);
	//case CXCursor_ClassTemplate: return ds_Visitor_visitClassTemplate(cursor, parent, client_data);
	//case CXCursor_ClassTemplatePartialSpecialization: return ds_Visitor_visitClassTemplatePartialSpecialization(cursor, parent, client_data);
	//case CXCursor_NamespaceAlias: return ds_Visitor_visitNamespaceAlias(cursor, parent, client_data);
	//case CXCursor_UsingDirective: return ds_Visitor_visitUsingDirective(cursor, parent, client_data);
	//case CXCursor_UsingDeclaration: return ds_Visitor_visitUsingDeclaration(cursor, parent, client_data);
	//case CXCursor_TypeAliasDecl: return ds_Visitor_visitTypeAliasDecl(cursor, parent, client_data);
	//case CXCursor_ObjCSynthesizeDecl: return ds_Visitor_visitObjCSynthesizeDecl(cursor, parent, client_data);
	//case CXCursor_ObjCDynamicDecl: return ds_Visitor_visitObjCDynamicDecl(cursor, parent, client_data);
	//case CXCursor_CXXAccessSpecifier: return ds_Visitor_visitCXXAccessSpecifier(cursor, parent, client_data);
	//case CXCursor_FirstDecl: return ds_Visitor_visitFirstDecl(cursor, parent, client_data);
	//case CXCursor_LastDecl: return ds_Visitor_visitLastDecl(cursor, parent, client_data);
	//case CXCursor_FirstRef: return ds_Visitor_visitFirstRef(cursor, parent, client_data);
	//case CXCursor_ObjCSuperClassRef: return ds_Visitor_visitObjCSuperClassRef(cursor, parent, client_data);
	//case CXCursor_ObjCProtocolRef: return ds_Visitor_visitObjCProtocolRef(cursor, parent, client_data);
	//case CXCursor_ObjCClassRef: return ds_Visitor_visitObjCClassRef(cursor, parent, client_data);
	case CXCursor_TypeRef: return ds_Visitor_visitTypeRef(cursor, parent, client_data);
	case CXCursor_CXXBaseSpecifier: return ds_Visitor_visitCXXBaseSpecifier(cursor, parent, client_data);
	case CXCursor_TemplateRef: return ds_Visitor_visitTemplateRef(cursor, parent, client_data);
	case CXCursor_NamespaceRef: return ds_Visitor_visitNamespaceRef(cursor, parent, client_data);
	case CXCursor_MemberRef: return ds_Visitor_visitMemberRef(cursor, parent, client_data);
	case CXCursor_LabelRef: return ds_Visitor_visitLabelRef(cursor, parent, client_data);
	//case CXCursor_OverloadedDeclRef: return ds_Visitor_visitOverloadedDeclRef(cursor, parent, client_data);
	case CXCursor_VariableRef: return ds_Visitor_visitVariableRef(cursor, parent, client_data);
	//case CXCursor_InvalidFile: return ds_Visitor_visitInvalidFile(cursor, parent, client_data);
	//case CXCursor_NoDeclFound: return ds_Visitor_visitNoDeclFound(cursor, parent, client_data);
	//case CXCursor_NotImplemented: return ds_Visitor_visitNotImplemented(cursor, parent, client_data);
	//case CXCursor_InvalidCode: return ds_Visitor_visitInvalidCode(cursor, parent, client_data);
	//case CXCursor_UnexposedExpr: return ds_Visitor_visitUnexposedExpr(cursor, parent, client_data);
	case CXCursor_DeclRefExpr: return ds_Visitor_visitDeclRefExpr(cursor, parent, client_data);
	case CXCursor_MemberRefExpr: return ds_Visitor_visitMemberRefExpr(cursor, parent, client_data);
	case CXCursor_CallExpr: return ds_Visitor_visitCallExpr(cursor, parent, client_data);
	case CXCursor_ObjCMessageExpr: return ds_Visitor_visitObjCMessageExpr(cursor, parent, client_data);
	case CXCursor_BlockExpr: return ds_Visitor_visitBlockExpr(cursor, parent, client_data);
	case CXCursor_IntegerLiteral: return ds_Visitor_visitIntegerLiteral(cursor, parent, client_data);
	case CXCursor_FloatingLiteral: return ds_Visitor_visitFloatingLiteral(cursor, parent, client_data);
	case CXCursor_ImaginaryLiteral: return ds_Visitor_visitImaginaryLiteral(cursor, parent, client_data);
	case CXCursor_StringLiteral: return ds_Visitor_visitStringLiteral(cursor, parent, client_data);
	case CXCursor_CharacterLiteral: return ds_Visitor_visitCharacterLiteral(cursor, parent, client_data);
	case CXCursor_ParenExpr: return ds_Visitor_visitParenExpr(cursor, parent, client_data);
	case CXCursor_UnaryOperator: return ds_Visitor_visitUnaryOperator(cursor, parent, client_data);
	case CXCursor_ArraySubscriptExpr: return ds_Visitor_visitArraySubscriptExpr(cursor, parent, client_data);
	case CXCursor_BinaryOperator: return ds_Visitor_visitBinaryOperator(cursor, parent, client_data);
	case CXCursor_CompoundAssignOperator: return ds_Visitor_visitCompoundAssignOperator(cursor, parent, client_data);
	case CXCursor_ConditionalOperator: return ds_Visitor_visitConditionalOperator(cursor, parent, client_data);
	//case CXCursor_CStyleCastExpr: return ds_Visitor_visitCStyleCastExpr(cursor, parent, client_data);
	//case CXCursor_CompoundLiteralExpr: return ds_Visitor_visitCompoundLiteralExpr(cursor, parent, client_data);
	//case CXCursor_InitListExpr: return ds_Visitor_visitInitListExpr(cursor, parent, client_data);
	//case CXCursor_AddrLabelExpr: return ds_Visitor_visitAddrLabelExpr(cursor, parent, client_data);
	//case CXCursor_StmtExpr: return ds_Visitor_visitStmtExpr(cursor, parent, client_data);
	//case CXCursor_GenericSelectionExpr: return ds_Visitor_visitGenericSelectionExpr(cursor, parent, client_data);
	//case CXCursor_GNUNullExpr: return ds_Visitor_visitGNUNullExpr(cursor, parent, client_data);
	//case CXCursor_CXXStaticCastExpr: return ds_Visitor_visitCXXStaticCastExpr(cursor, parent, client_data);
	//case CXCursor_CXXDynamicCastExpr: return ds_Visitor_visitCXXDynamicCastExpr(cursor, parent, client_data);
	//case CXCursor_CXXReinterpretCastExpr: return ds_Visitor_visitCXXReinterpretCastExpr(cursor, parent, client_data);
	//case CXCursor_CXXConstCastExpr: return ds_Visitor_visitCXXConstCastExpr(cursor, parent, client_data);
	//case CXCursor_CXXFunctionalCastExpr: return ds_Visitor_visitCXXFunctionalCastExpr(cursor, parent, client_data);
	//case CXCursor_CXXTypeidExpr: return ds_Visitor_visitCXXTypeidExpr(cursor, parent, client_data);
	//case CXCursor_CXXBoolLiteralExpr: return ds_Visitor_visitCXXBoolLiteralExpr(cursor, parent, client_data);
	//case CXCursor_CXXNullPtrLiteralExpr: return ds_Visitor_visitCXXNullPtrLiteralExpr(cursor, parent, client_data);
	//case CXCursor_CXXThisExpr: return ds_Visitor_visitCXXThisExpr(cursor, parent, client_data);
	//case CXCursor_CXXThrowExpr: return ds_Visitor_visitCXXThrowExpr(cursor, parent, client_data);
	//case CXCursor_CXXNewExpr: return ds_Visitor_visitCXXNewExpr(cursor, parent, client_data);
	//case CXCursor_CXXDeleteExpr: return ds_Visitor_visitCXXDeleteExpr(cursor, parent, client_data);
	//case CXCursor_UnaryExpr: return ds_Visitor_visitUnaryExpr(cursor, parent, client_data);
	//case CXCursor_ObjCStringLiteral: return ds_Visitor_visitObjCStringLiteral(cursor, parent, client_data);
	//case CXCursor_ObjCEncodeExpr: return ds_Visitor_visitObjCEncodeExpr(cursor, parent, client_data);
	//case CXCursor_ObjCSelectorExpr: return ds_Visitor_visitObjCSelectorExpr(cursor, parent, client_data);
	//case CXCursor_ObjCProtocolExpr: return ds_Visitor_visitObjCProtocolExpr(cursor, parent, client_data);
	//case CXCursor_ObjCBridgedCastExpr: return ds_Visitor_visitObjCBridgedCastExpr(cursor, parent, client_data);
	//case CXCursor_PackExpansionExpr: return ds_Visitor_visitPackExpansionExpr(cursor, parent, client_data);
	//case CXCursor_SizeOfPackExpr: return ds_Visitor_visitSizeOfPackExpr(cursor, parent, client_data);
	//case CXCursor_LambdaExpr: return ds_Visitor_visitLambdaExpr(cursor, parent, client_data);
	//case CXCursor_ObjCBoolLiteralExpr: return ds_Visitor_visitObjCBoolLiteralExpr(cursor, parent, client_data);
	//case CXCursor_LastExpr: return ds_Visitor_visitLastExpr(cursor, parent, client_data);
	//case CXCursor_FirstStmt: return ds_Visitor_visitFirstStmt(cursor, parent, client_data);
	case CXCursor_UnexposedStmt: return ds_Visitor_visitUnexposedStmt(cursor, parent, client_data);
	case CXCursor_LabelStmt: return ds_Visitor_visitLabelStmt(cursor, parent, client_data);
	case CXCursor_CompoundStmt: return ds_Visitor_visitCompoundStmt(cursor, parent, client_data);
	case CXCursor_CaseStmt: return ds_Visitor_visitCaseStmt(cursor, parent, client_data);
	case CXCursor_DefaultStmt: return ds_Visitor_visitDefaultStmt(cursor, parent, client_data);
	case CXCursor_IfStmt: return ds_Visitor_visitIfStmt(cursor, parent, client_data);
	case CXCursor_SwitchStmt: return ds_Visitor_visitSwitchStmt(cursor, parent, client_data);
	case CXCursor_WhileStmt: return ds_Visitor_visitWhileStmt(cursor, parent, client_data);
	case CXCursor_DoStmt: return ds_Visitor_visitDoStmt(cursor, parent, client_data);
	case CXCursor_ForStmt: return ds_Visitor_visitForStmt(cursor, parent, client_data);
	case CXCursor_GotoStmt: return ds_Visitor_visitGotoStmt(cursor, parent, client_data);
	case CXCursor_IndirectGotoStmt: return ds_Visitor_visitIndirectGotoStmt(cursor, parent, client_data);
	case CXCursor_ContinueStmt: return ds_Visitor_visitContinueStmt(cursor, parent, client_data);
	case CXCursor_BreakStmt: return ds_Visitor_visitBreakStmt(cursor, parent, client_data);
	case CXCursor_ReturnStmt: return ds_Visitor_visitReturnStmt(cursor, parent, client_data);
	//case CXCursor_GCCAsmStmt: return ds_Visitor_visitGCCAsmStmt(cursor, parent, client_data);
	//case CXCursor_AsmStmt: return ds_Visitor_visitAsmStmt(cursor, parent, client_data);
	//case CXCursor_ObjCAtTryStmt: return ds_Visitor_visitObjCAtTryStmt(cursor, parent, client_data);
	//case CXCursor_ObjCAtCatchStmt: return ds_Visitor_visitObjCAtCatchStmt(cursor, parent, client_data);
	//case CXCursor_ObjCAtFinallyStmt: return ds_Visitor_visitObjCAtFinallyStmt(cursor, parent, client_data);
	//case CXCursor_ObjCAtThrowStmt: return ds_Visitor_visitObjCAtThrowStmt(cursor, parent, client_data);
	//case CXCursor_ObjCAtSynchronizedStmt: return ds_Visitor_visitObjCAtSynchronizedStmt(cursor, parent, client_data);
	//case CXCursor_ObjCAutoreleasePoolStmt: return ds_Visitor_visitObjCAutoreleasePoolStmt(cursor, parent, client_data);
	//case CXCursor_ObjCForCollectionStmt: return ds_Visitor_visitObjCForCollectionStmt(cursor, parent, client_data);
	//case CXCursor_CXXCatchStmt: return ds_Visitor_visitCXXCatchStmt(cursor, parent, client_data);
	//case CXCursor_CXXTryStmt: return ds_Visitor_visitCXXTryStmt(cursor, parent, client_data);
	//case CXCursor_CXXForRangeStmt: return ds_Visitor_visitCXXForRangeStmt(cursor, parent, client_data);
	//case CXCursor_SEHTryStmt: return ds_Visitor_visitSEHTryStmt(cursor, parent, client_data);
	//case CXCursor_SEHExceptStmt: return ds_Visitor_visitSEHExceptStmt(cursor, parent, client_data);
	//case CXCursor_SEHFinallyStmt: return ds_Visitor_visitSEHFinallyStmt(cursor, parent, client_data);
	//case CXCursor_MSAsmStmt: return ds_Visitor_visitMSAsmStmt(cursor, parent, client_data);
	case CXCursor_NullStmt: return ds_Visitor_visitNullStmt(cursor, parent, client_data);
	case CXCursor_DeclStmt: return ds_Visitor_visitDeclStmt(cursor, parent, client_data);
	case CXCursor_TranslationUnit: return ds_Visitor_visitTranslationUnit(cursor, parent, client_data);
	//case CXCursor_IBActionAttr: return ds_Visitor_visitIBActionAttr(cursor, parent, client_data);
	//case CXCursor_IBOutletAttr: return ds_Visitor_visitIBOutletAttr(cursor, parent, client_data);
	//case CXCursor_IBOutletCollectionAttr: return ds_Visitor_visitIBOutletCollectionAttr(cursor, parent, client_data);
	//case CXCursor_CXXFinalAttr: return ds_Visitor_visitCXXFinalAttr(cursor, parent, client_data);
	//case CXCursor_CXXOverrideAttr: return ds_Visitor_visitCXXOverrideAttr(cursor, parent, client_data);
	//case CXCursor_AnnotateAttr: return ds_Visitor_visitAnnotateAttr(cursor, parent, client_data);
	//case CXCursor_AsmLabelAttr: return ds_Visitor_visitAsmLabelAttr(cursor, parent, client_data);
	//case CXCursor_PreprocessingDirective: return ds_Visitor_visitPreprocessingDirective(cursor, parent, client_data);
	//case CXCursor_MacroDefinition: return ds_Visitor_visitMacroDefinition(cursor, parent, client_data);
	//case CXCursor_MacroExpansion: return ds_Visitor_visitMacroExpansion(cursor, parent, client_data);
	//case CXCursor_InclusionDirective: return ds_Visitor_visitInclusionDirective(cursor, parent, client_data);
	//case CXCursor_ModuleImportDecl: return ds_Visitor_visitModuleImportDecl(cursor, parent, client_data);
    default:
        ds_Visitor_visitUnknown(cursor, parent, client_data);
    }

    return CXChildVisit_Continue;
}

// node-specific

//#define emitPostChildren() if (clang_visitChildren(cursor, &ds_Visitor_visit, &ds_Visitor_visitPost, client_data)) return CXChildVisit_Continue
#define emitChildren() if (clang_visitChildren(cursor, &ds_Visitor_visit, client_data)) return CXChildVisit_Continue
//#define emitChildren()

ds_VisitResult
ds_Visitor_visitUnknown(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    ds_CursorKind kind = clang_getCursorKind(cursor);

    if (clang_isPreprocessing(kind))
        return CXChildVisit_Continue;

    emit_STAG("drox", "dl");
    emit_NTAG("drox", "unimplemented");
    if (clang_isDeclaration(kind))
        emit_NTAG("c89", "declaration");
    if (clang_isReference(kind))
        emit_NTAG("c89", "reference");
    if (clang_isExpression(kind))
        emit_NTAG("c89", "expression");
    if (clang_isStatement(kind))
        emit_NTAG("c89", "statement");
    if (clang_isAttribute(kind))
        emit_NTAG("c89", "attribute");
    if (clang_isInvalid(kind))
        emit_NTAG("c89", "invalid");
    if (clang_isTranslationUnit(kind))
        emit_NTAG("c89", "translation_unit");
    emit_ETAG("drox", "dl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitUnexposedDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "dl");
    emit_NTAG("c89", "unexposed");
    emit_ETAG("drox", "dl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitStructDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "dl");
    emit_NTAG("c89", "struct");
    emitChildren();
    emit_ETAG("drox", "dl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitUnionDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "dl");
    emit_NTAG("c89", "union");
    emitChildren();
    emit_ETAG("drox", "dl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitClassDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "dl");
    emit_NTAG("cxx98", "class");
    emitChildren();
    emit_ETAG("drox", "dl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitEnumDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "dl");
    emit_NTAG("c89", "enum");
    emitChildren();
    emit_ETAG("drox", "dl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitFieldDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "dl");
    emit_NTAG("c89", "field");
    emitChildren();
    emit_ETAG("drox", "dl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitEnumConstantDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    long long value = clang_getEnumConstantDeclValue(cursor);
    emit_STAG("drox", "dt");
    emitChildren();
    emit_ETAG("drox", "dt");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitFunctionDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "dl");
    emit_NTAG("c89", "function");
    emitChildren();
    emit_ETAG("drox", "dl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitVarDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "dl");
    emit_NTAG("prog2", "local_var");
    emitChildren();
    emit_ETAG("drox", "dl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitParmDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("m", "bvar");
    emitChildren();
    emit_ETAG("m", "bvar");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitObjCInterfaceDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitObjCCategoryDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitObjCProtocolDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitObjCPropertyDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitObjCIvarDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitObjCInstanceMethodDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitObjCClassMethodDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitObjCImplementationDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitObjCCategoryImplDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitTypedefDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "dl");
    emit_NTAG("c89", "typedef");
    emitChildren();
    emit_ETAG("drox", "dl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitCXXMethod(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "dl");
    emit_NTAG("cxx98", "method");
    emitChildren();
    emit_ETAG("drox", "dl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitNamespace(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "dl");
    emit_NTAG("cxx98", "namespace");
    emitChildren();
    emit_ETAG("drox", "dl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitLinkageSpec(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "dl");
    emit_NTAG("cxx98", "linkage");

    switch (clang_getCursorLinkage(cursor)) {
    case CXLinkage_NoLinkage:
        emit_NTAG("c89", "no_linkage");
        break;
    case CXLinkage_Internal:
        emit_NTAG("c89", "internal");
        break;
    case CXLinkage_UniqueExternal:
        emit_NTAG("c89", "unique_external");
        break;
    case CXLinkage_External:
        emit_NTAG("c89", "external");
        break;
    case CXLinkage_Invalid:
    default:
        return CXChildVisit_Break;
    }

    emit_ETAG("drox", "dl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitConstructor(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "dl");
    emit_NTAG("cxx98", "constructor");
    emitChildren();
    emit_ETAG("drox", "dl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitDestructor(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "dl");
    emit_NTAG("cxx98", "destructor");
    emitChildren();
    emit_ETAG("drox", "dl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitConversionFunction(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "dl");
    emit_NTAG("cxx98", "conversion");
    emitChildren();
    emit_ETAG("drox", "dl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitTemplateTypeParameter(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitNonTypeTemplateParameter(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitTemplateTemplateParameter(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitFunctionTemplate(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitClassTemplate(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitClassTemplatePartialSpecialization(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitNamespaceAlias(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "dl");
    emit_NTAG("cxx98", "namespace_alias");
    emitChildren();
    emit_ETAG("drox", "dl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitUsingDirective(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "dl");
    emit_NTAG("cxx98", "using_directive");
    emitChildren();
    emit_ETAG("drox", "dl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitUsingDeclaration(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "dl");
    emit_NTAG("cxx98", "using_declaration");
    emitChildren();
    emit_ETAG("drox", "dl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitTypeAliasDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "dl");
    emit_NTAG("cxx98", "type_alias");
    emitChildren();
    emit_ETAG("drox", "dl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitObjCSynthesizeDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitObjCDynamicDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitCXXAccessSpecifier(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "dl");
    emit_NTAG("cxx98", "access");
    emitChildren();
    emit_ETAG("drox", "dl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitObjCSuperClassRef(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitObjCProtocolRef(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitObjCClassRef(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitTypeRef(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "dl");

    CXType type = clang_getCursorType(cursor);
    if (clang_isConstQualifiedType(type))
        emit_NTAG("c89", "const");
    if (clang_isVolatileQualifiedType(type))
        emit_NTAG("c89", "volatile");
    if (clang_isRestrictQualifiedType(type))
        emit_NTAG("c89", "restrict");

    emit_ETAG("drox", "dl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitCXXBaseSpecifier(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;

    switch (clang_getCXXAccessSpecifier(cursor)) {
    case CX_CXXPublic:    
        emit_NTAG("c89", "public");    
        break;
    case CX_CXXProtected: 
        emit_NTAG("c89", "protected"); 
        break;
    case CX_CXXPrivate:   
        emit_NTAG("c89", "private");   
        break;
    default:
        return CXChildVisit_Break;
    }

	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitTemplateRef(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitNamespaceRef(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitMemberRef(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitLabelRef(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitOverloadedDeclRef(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitVariableRef(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "dl");
    emit_NTAG("cxx98", "access");
    emitChildren();
    emit_ETAG("drox", "dl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitLastRef(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitFirstInvalid(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitInvalidFile(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitNoDeclFound(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitNotImplemented(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitInvalidCode(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitLastInvalid(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitFirstExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitUnexposedExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitDeclRefExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitMemberRefExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitCallExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("m", "apply");
    //emitChildren();
    emit_ETAG("m", "apply");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitObjCMessageExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitBlockExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "sl");
    emit_NTAG("objc1", "block");
    //emitChildren();
    emit_ETAG("drox", "sl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitIntegerLiteral(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    CXString textOb = clang_getCursorSpelling(cursor);
    emit_SETAG("m", "cn type=\"integer\"", clang_getCString(textOb));
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitFloatingLiteral(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitImaginaryLiteral(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitStringLiteral(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitCharacterLiteral(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitParenExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitUnaryOperator(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitArraySubscriptExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitBinaryOperator(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitCompoundAssignOperator(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitConditionalOperator(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitCStyleCastExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitCompoundLiteralExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitInitListExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitAddrLabelExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitStmtExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emitChildren();
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitGenericSelectionExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitGNUNullExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitCXXStaticCastExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitCXXDynamicCastExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitCXXReinterpretCastExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitCXXConstCastExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitCXXFunctionalCastExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitCXXTypeidExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitCXXBoolLiteralExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitCXXNullPtrLiteralExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitCXXThisExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitCXXThrowExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitCXXNewExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitCXXDeleteExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitUnaryExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitObjCStringLiteral(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitObjCEncodeExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitObjCSelectorExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitObjCProtocolExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitObjCBridgedCastExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitPackExpansionExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitSizeOfPackExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitLambdaExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitObjCBoolLiteralExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitLastExpr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitFirstStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitUnexposedStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "sl");
    emit_NTAG("drox", "unexposed");
    //emitChildren();
    emit_ETAG("drox", "sl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitLabelStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "sl");
    emit_NTAG("prog2", "label");
    //emitChildren();
    emit_ETAG("drox", "sl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitCompoundStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "sl");
    emit_NTAG("prog1", "block");
    emitChildren();
    emit_ETAG("drox", "sl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitCaseStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "si");
    emitChildren();
    emit_ETAG("drox", "si");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitDefaultStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "sd");
    emitChildren();
    emit_ETAG("drox", "sd");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitIfStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "sl");
    emit_NTAG("prog1", "if");
    //emitChildren();
    emit_ETAG("drox", "sl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitSwitchStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "sl");
    emit_NTAG("switch1", "case");
    //emitChildren();
    emit_ETAG("drox", "sl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitWhileStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "sl");
    emit_NTAG("prog2", "while");
    //emitChildren();
    emit_ETAG("drox", "sl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitDoStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "sl");
    emit_NTAG("prog2", "do_while");
    //emitChildren();
    emit_ETAG("drox", "sl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitForStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "sl");
    emit_NTAG("prog2", "for");
    //emitChildren();
    emit_ETAG("drox", "sl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitGotoStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "sl");
    emit_NTAG("prog2", "goto");
    //emitChildren();
    emit_ETAG("drox", "sl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitIndirectGotoStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "sl");
    emit_NTAG("c89", "indirect_goto");
    //emitChildren();
    emit_ETAG("drox", "sl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitContinueStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "sl");
    emit_NTAG("prog2", "continue");
    //emitChildren();
    emit_ETAG("drox", "sl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitBreakStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitReturnStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "sl");
    emit_NTAG("prog1", "return");
    emitChildren();
    emit_ETAG("drox", "sl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitGCCAsmStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitAsmStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitObjCAtTryStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitObjCAtCatchStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitObjCAtFinallyStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitObjCAtThrowStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitObjCAtSynchronizedStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitObjCAutoreleasePoolStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitObjCForCollectionStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitCXXCatchStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitCXXTryStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitCXXForRangeStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitSEHTryStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitSEHExceptStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitSEHFinallyStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitMSAsmStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitNullStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "sl");
    emit_NTAG("c89", "empty");
    //emitChildren();
    emit_ETAG("drox", "sl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitDeclStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emitChildren();
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitLastStmt(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "sl");
    emit_NTAG("c89", "last");
    //emitChildren();
    emit_ETAG("drox", "sl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitTranslationUnit(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "dl");
    emit_NTAG("c89", "translation_unit");
    emitChildren();
    emit_ETAG("drox", "dl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitFirstAttr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitUnexposedAttr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitIBActionAttr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitIBOutletAttr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitIBOutletCollectionAttr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitCXXFinalAttr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitCXXOverrideAttr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitAnnotateAttr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitAsmLabelAttr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitLastAttr(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitPreprocessingDirective(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_NTAG("c89", "preprocessing");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitMacroDefinition(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "dl");
    emit_NTAG("c89", "macro_definition");
    //emitChildren();
    emit_ETAG("drox", "dl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitMacroExpansion(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "dl");
    emit_NTAG("c89", "macro_expansion");
    //emitChildren();
    emit_ETAG("drox", "dl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitInclusionDirective(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "dl");
    emit_NTAG("c89", "include");
    //emitChildren();
    emit_ETAG("drox", "dl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitFirstPreprocessing(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitLastPreprocessing(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitModuleImportDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_STAG("drox", "dl");
    emit_NTAG("objc98", "import");
    //emitChildren();
    emit_ETAG("drox", "dl");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitFirstExtraDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_NTAG("drox", "extra");
	return CXChildVisit_Continue;
}

ds_VisitResult
ds_Visitor_visitLastExtraDecl(ds_Cursor cursor, ds_Cursor parent, ds_VisitorData client_data)
{
	ds_Visitor *my = (ds_Visitor *)client_data;
    emit_NTAG("drox", "extra");
	return CXChildVisit_Continue;
}

