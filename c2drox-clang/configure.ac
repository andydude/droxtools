AC_INIT([clang2drox], [1.0])
AM_INIT_AUTOMAKE

AC_PROG_CC
AC_PROG_CXX

AC_CHECK_HEADER_STDBOOL
AC_CHECK_HEADER([clang-c/Index.h])
AC_CHECK_LIB([clang], [clang_createIndex])

AC_CONFIG_HEADERS([config.h])
AC_CONFIG_FILES([Makefile])
AC_CONFIG_FILES([src/Makefile])
AC_OUTPUT
