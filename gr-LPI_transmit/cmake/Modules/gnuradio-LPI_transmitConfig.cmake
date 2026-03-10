find_package(PkgConfig)

PKG_CHECK_MODULES(PC_GR_LPI_TRANSMIT gnuradio-LPI_transmit)

FIND_PATH(
    GR_LPI_TRANSMIT_INCLUDE_DIRS
    NAMES gnuradio/LPI_transmit/api.h
    HINTS $ENV{LPI_TRANSMIT_DIR}/include
        ${PC_LPI_TRANSMIT_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    GR_LPI_TRANSMIT_LIBRARIES
    NAMES gnuradio-LPI_transmit
    HINTS $ENV{LPI_TRANSMIT_DIR}/lib
        ${PC_LPI_TRANSMIT_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/gnuradio-LPI_transmitTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(GR_LPI_TRANSMIT DEFAULT_MSG GR_LPI_TRANSMIT_LIBRARIES GR_LPI_TRANSMIT_INCLUDE_DIRS)
MARK_AS_ADVANCED(GR_LPI_TRANSMIT_LIBRARIES GR_LPI_TRANSMIT_INCLUDE_DIRS)
