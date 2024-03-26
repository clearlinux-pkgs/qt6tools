#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v5
# autospec commit: c02b2fe
#
%define keepstatic 1
Name     : qt6tools
Version  : 6.6.3
Release  : 59
URL      : https://download.qt.io/official_releases/qt/6.6/6.6.3/submodules/qttools-everywhere-src-6.6.3.tar.xz
Source0  : https://download.qt.io/official_releases/qt/6.6/6.6.3/submodules/qttools-everywhere-src-6.6.3.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause BSL-1.0 GFDL-1.3 GPL-2.0 GPL-3.0 LGPL-3.0 MIT
Requires: qt6tools-data = %{version}-%{release}
Requires: qt6tools-lib = %{version}-%{release}
Requires: qt6tools-libexec = %{version}-%{release}
Requires: qt6tools-license = %{version}-%{release}
BuildRequires : Vulkan-Headers-dev
BuildRequires : Vulkan-Loader-dev
BuildRequires : Vulkan-Tools
BuildRequires : buildreq-cmake
BuildRequires : glibc-dev
BuildRequires : libxkbcommon-dev
BuildRequires : libxkbfile-dev
BuildRequires : llvm-dev
BuildRequires : llvm-staticdev
BuildRequires : mesa-dev
BuildRequires : qt6base-dev
BuildRequires : zstd-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Qt Designer is a capable graphical user interface designer that lets you
create and configure forms without writing code. GUIs created with
Qt Designer can be compiled into an application or created at run-time.

%package data
Summary: data components for the qt6tools package.
Group: Data

%description data
data components for the qt6tools package.


%package dev
Summary: dev components for the qt6tools package.
Group: Development
Requires: qt6tools-lib = %{version}-%{release}
Requires: qt6tools-data = %{version}-%{release}
Provides: qt6tools-devel = %{version}-%{release}
Requires: qt6tools = %{version}-%{release}

%description dev
dev components for the qt6tools package.


%package lib
Summary: lib components for the qt6tools package.
Group: Libraries
Requires: qt6tools-data = %{version}-%{release}
Requires: qt6tools-libexec = %{version}-%{release}
Requires: qt6tools-license = %{version}-%{release}

%description lib
lib components for the qt6tools package.


%package libexec
Summary: libexec components for the qt6tools package.
Group: Default
Requires: qt6tools-license = %{version}-%{release}

%description libexec
libexec components for the qt6tools package.


%package license
Summary: license components for the qt6tools package.
Group: Default

%description license
license components for the qt6tools package.


%prep
%setup -q -n qttools-everywhere-src-6.6.3
cd %{_builddir}/qttools-everywhere-src-6.6.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1711496067
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1711496067
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qt6tools
cp %{_builddir}/qttools-everywhere-src-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/qt6tools/b073f11f0c81a95ab5e32aa6b5d23a5955a95274 || :
cp %{_builddir}/qttools-everywhere-src-%{version}/LICENSES/GFDL-1.3-no-invariants-only.txt %{buildroot}/usr/share/package-licenses/qt6tools/715f995f11805ee85601834220c43b082f457ea3 || :
cp %{_builddir}/qttools-everywhere-src-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/qt6tools/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/qttools-everywhere-src-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6tools/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/qttools-everywhere-src-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6tools/f45ee1c765646813b442ca58de72e20a64a7ddba || :
cp %{_builddir}/qttools-everywhere-src-%{version}/src/assistant/qlitehtml/LICENSES/Apache-2.0.txt %{buildroot}/usr/share/package-licenses/qt6tools/be561fe6eb626c2566b9a6c0885554b4ee4e6b74 || :
cp %{_builddir}/qttools-everywhere-src-%{version}/src/assistant/qlitehtml/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/qt6tools/b073f11f0c81a95ab5e32aa6b5d23a5955a95274 || :
cp %{_builddir}/qttools-everywhere-src-%{version}/src/assistant/qlitehtml/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6tools/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/qttools-everywhere-src-%{version}/src/assistant/qlitehtml/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/qt6tools/adadb67a9875aeeac285309f1eab6e47d9ee08a7 || :
cp %{_builddir}/qttools-everywhere-src-%{version}/src/assistant/qlitehtml/src/3rdparty/litehtml/LICENSE %{buildroot}/usr/share/package-licenses/qt6tools/e28ab474db38a338e29ca698348e02915867084c || :
cp %{_builddir}/qttools-everywhere-src-%{version}/src/assistant/qlitehtml/src/3rdparty/litehtml/src/gumbo/LICENSE %{buildroot}/usr/share/package-licenses/qt6tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/qttools-everywhere-src-%{version}/src/qdoc/catch/CATCH_LICENSE.txt %{buildroot}/usr/share/package-licenses/qt6tools/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90 || :
cp %{_builddir}/qttools-everywhere-src-%{version}/tests/manual/qtattributionsscanner/data/LICENSE %{buildroot}/usr/share/package-licenses/qt6tools/673921c2954e5b10a7388e0a2fc6be083a609bd3 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
## Remove excluded files
rm -f %{buildroot}*/usr/lib64/cmake/Qt5Designer/Qt5Designer_AnalogClockPlugin.cmake
rm -f %{buildroot}*/usr/lib64/cmake/Qt5Designer/Qt5Designer_MultiPageWidgetPlugin.cmake
rm -f %{buildroot}*/usr/lib64/cmake/Qt5Designer/Qt5Designer_TicTacToePlugin.cmake
rm -f %{buildroot}*/usr/lib64/cmake/Qt5Designer/Qt5Designer_WorldTimeClockPlugin.cmake
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qt6/phrasebooks/danish.qph
/usr/share/qt6/phrasebooks/dutch.qph
/usr/share/qt6/phrasebooks/finnish.qph
/usr/share/qt6/phrasebooks/french.qph
/usr/share/qt6/phrasebooks/german.qph
/usr/share/qt6/phrasebooks/hungarian.qph
/usr/share/qt6/phrasebooks/italian.qph
/usr/share/qt6/phrasebooks/japanese.qph
/usr/share/qt6/phrasebooks/norwegian.qph
/usr/share/qt6/phrasebooks/polish.qph
/usr/share/qt6/phrasebooks/russian.qph
/usr/share/qt6/phrasebooks/spanish.qph
/usr/share/qt6/phrasebooks/swedish.qph

%files dev
%defattr(-,root,root,-)
/usr/include/QtDesigner/6.6.3/QtDesigner/private/abstractdialoggui_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/abstractintrospection_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/actioneditor_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/actionprovider_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/actionrepository_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/codedialog_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/connectionedit_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/csshighlighter_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/deviceprofile_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/dialoggui_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/extensionfactory_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/formbuilderextra_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/formlayoutmenu_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/formwindowbase_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/grid_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/gridpanel_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/htmlhighlighter_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/iconloader_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/iconselector_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/invisible_widget_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/layout_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/layoutinfo_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/metadatabase_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/morphmenu_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/newactiondialog_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/newformwidget_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/orderdialog_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/plaintexteditor_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/plugindialog_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/pluginmanager_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/previewconfigurationwidget_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/previewmanager_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/promotionmodel_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/promotiontaskmenu_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/properties_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/propertylineedit_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/qdesigner_command2_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/qdesigner_command_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/qdesigner_dnditem_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/qdesigner_dockwidget_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/qdesigner_formbuilder_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/qdesigner_formeditorcommand_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/qdesigner_formwindowcommand_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/qdesigner_formwindowmanager_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/qdesigner_introspection_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/qdesigner_membersheet_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/qdesigner_menu_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/qdesigner_menubar_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/qdesigner_objectinspector_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/qdesigner_promotion_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/qdesigner_promotiondialog_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/qdesigner_propertyeditor_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/qdesigner_propertysheet_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/qdesigner_qsettings_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/qdesigner_stackedbox_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/qdesigner_tabwidget_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/qdesigner_taskmenu_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/qdesigner_toolbar_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/qdesigner_toolbox_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/qdesigner_utils_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/qdesigner_widget_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/qdesigner_widgetbox_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/qdesigner_widgetitem_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/qlayout_widget_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/qsimpleresource_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/qtresourceeditordialog_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/qtresourcemodel_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/qtresourceview_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/rcc_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/resourcebuilder_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/richtexteditor_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/selectsignaldialog_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/shared_enums_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/shared_global_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/shared_settings_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/sheet_delegate_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/signalslotdialog_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/spacer_widget_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/stylesheeteditor_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/textbuilder_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/textpropertyeditor_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/ui4_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/widgetdatabase_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/widgetfactory_p.h
/usr/include/QtDesigner/6.6.3/QtDesigner/private/zoomwidget_p.h
/usr/include/QtDesigner/QAbstractExtensionFactory
/usr/include/QtDesigner/QAbstractExtensionManager
/usr/include/QtDesigner/QAbstractFormBuilder
/usr/include/QtDesigner/QDesignerActionEditorInterface
/usr/include/QtDesigner/QDesignerComponents
/usr/include/QtDesigner/QDesignerContainerExtension
/usr/include/QtDesigner/QDesignerCustomWidgetCollectionInterface
/usr/include/QtDesigner/QDesignerCustomWidgetInterface
/usr/include/QtDesigner/QDesignerDnDItemInterface
/usr/include/QtDesigner/QDesignerDynamicPropertySheetExtension
/usr/include/QtDesigner/QDesignerExportWidget
/usr/include/QtDesigner/QDesignerExtraInfoExtension
/usr/include/QtDesigner/QDesignerFormEditorInterface
/usr/include/QtDesigner/QDesignerFormEditorPluginInterface
/usr/include/QtDesigner/QDesignerFormWindowCursorInterface
/usr/include/QtDesigner/QDesignerFormWindowInterface
/usr/include/QtDesigner/QDesignerFormWindowManagerInterface
/usr/include/QtDesigner/QDesignerFormWindowToolInterface
/usr/include/QtDesigner/QDesignerIntegration
/usr/include/QtDesigner/QDesignerIntegrationInterface
/usr/include/QtDesigner/QDesignerLanguageExtension
/usr/include/QtDesigner/QDesignerLayoutDecorationExtension
/usr/include/QtDesigner/QDesignerMemberSheetExtension
/usr/include/QtDesigner/QDesignerMetaDataBaseInterface
/usr/include/QtDesigner/QDesignerMetaDataBaseItemInterface
/usr/include/QtDesigner/QDesignerNewFormWidgetInterface
/usr/include/QtDesigner/QDesignerObjectInspectorInterface
/usr/include/QtDesigner/QDesignerOptionsPageInterface
/usr/include/QtDesigner/QDesignerPromotionInterface
/usr/include/QtDesigner/QDesignerPropertyEditorInterface
/usr/include/QtDesigner/QDesignerPropertySheetExtension
/usr/include/QtDesigner/QDesignerResourceBrowserInterface
/usr/include/QtDesigner/QDesignerSettingsInterface
/usr/include/QtDesigner/QDesignerTaskMenuExtension
/usr/include/QtDesigner/QDesignerWidgetBoxInterface
/usr/include/QtDesigner/QDesignerWidgetDataBaseInterface
/usr/include/QtDesigner/QDesignerWidgetDataBaseItemInterface
/usr/include/QtDesigner/QDesignerWidgetFactoryInterface
/usr/include/QtDesigner/QExtensionFactory
/usr/include/QtDesigner/QExtensionManager
/usr/include/QtDesigner/QFormBuilder
/usr/include/QtDesigner/QtDesigner
/usr/include/QtDesigner/QtDesignerDepends
/usr/include/QtDesigner/QtDesignerVersion
/usr/include/QtDesigner/abstractactioneditor.h
/usr/include/QtDesigner/abstractdnditem.h
/usr/include/QtDesigner/abstractformbuilder.h
/usr/include/QtDesigner/abstractformeditor.h
/usr/include/QtDesigner/abstractformeditorplugin.h
/usr/include/QtDesigner/abstractformwindow.h
/usr/include/QtDesigner/abstractformwindowcursor.h
/usr/include/QtDesigner/abstractformwindowmanager.h
/usr/include/QtDesigner/abstractformwindowtool.h
/usr/include/QtDesigner/abstractintegration.h
/usr/include/QtDesigner/abstractlanguage.h
/usr/include/QtDesigner/abstractmetadatabase.h
/usr/include/QtDesigner/abstractnewformwidget.h
/usr/include/QtDesigner/abstractobjectinspector.h
/usr/include/QtDesigner/abstractoptionspage.h
/usr/include/QtDesigner/abstractpromotioninterface.h
/usr/include/QtDesigner/abstractpropertyeditor.h
/usr/include/QtDesigner/abstractresourcebrowser.h
/usr/include/QtDesigner/abstractsettings.h
/usr/include/QtDesigner/abstractwidgetbox.h
/usr/include/QtDesigner/abstractwidgetdatabase.h
/usr/include/QtDesigner/abstractwidgetfactory.h
/usr/include/QtDesigner/container.h
/usr/include/QtDesigner/customwidget.h
/usr/include/QtDesigner/default_extensionfactory.h
/usr/include/QtDesigner/dynamicpropertysheet.h
/usr/include/QtDesigner/extension.h
/usr/include/QtDesigner/extension_global.h
/usr/include/QtDesigner/extrainfo.h
/usr/include/QtDesigner/formbuilder.h
/usr/include/QtDesigner/layoutdecoration.h
/usr/include/QtDesigner/membersheet.h
/usr/include/QtDesigner/propertysheet.h
/usr/include/QtDesigner/qdesigner_components.h
/usr/include/QtDesigner/qdesigner_components_global.h
/usr/include/QtDesigner/qdesignerexportwidget.h
/usr/include/QtDesigner/qextensionmanager.h
/usr/include/QtDesigner/qtdesignerversion.h
/usr/include/QtDesigner/sdk_global.h
/usr/include/QtDesigner/taskmenu.h
/usr/include/QtDesigner/uilib_global.h
/usr/include/QtDesignerComponents/6.6.3/QtDesignerComponents/private/lib_pch.h
/usr/include/QtDesignerComponents/QtDesignerComponents
/usr/include/QtDesignerComponents/QtDesignerComponentsDepends
/usr/include/QtDesignerComponents/QtDesignerComponentsVersion
/usr/include/QtDesignerComponents/qtdesignercomponentsversion.h
/usr/include/QtHelp/6.6.3/QtHelp/private/qfilternamedialog_p.h
/usr/include/QtHelp/6.6.3/QtHelp/private/qhelpcollectionhandler_p.h
/usr/include/QtHelp/6.6.3/QtHelp/private/qhelpdbreader_p.h
/usr/include/QtHelp/6.6.3/QtHelp/private/qhelpengine_p.h
/usr/include/QtHelp/6.6.3/QtHelp/private/qhelpfiltersettings_p.h
/usr/include/QtHelp/6.6.3/QtHelp/private/qhelpsearchindexreader_default_p.h
/usr/include/QtHelp/6.6.3/QtHelp/private/qhelpsearchindexreader_p.h
/usr/include/QtHelp/6.6.3/QtHelp/private/qhelpsearchindexwriter_default_p.h
/usr/include/QtHelp/6.6.3/QtHelp/private/qoptionswidget_p.h
/usr/include/QtHelp/QCompressedHelpInfo
/usr/include/QtHelp/QHelpContentItem
/usr/include/QtHelp/QHelpContentModel
/usr/include/QtHelp/QHelpContentWidget
/usr/include/QtHelp/QHelpEngine
/usr/include/QtHelp/QHelpEngineCore
/usr/include/QtHelp/QHelpFilterData
/usr/include/QtHelp/QHelpFilterEngine
/usr/include/QtHelp/QHelpFilterSettingsWidget
/usr/include/QtHelp/QHelpGlobal
/usr/include/QtHelp/QHelpIndexModel
/usr/include/QtHelp/QHelpIndexWidget
/usr/include/QtHelp/QHelpLink
/usr/include/QtHelp/QHelpSearchEngine
/usr/include/QtHelp/QHelpSearchQuery
/usr/include/QtHelp/QHelpSearchQueryWidget
/usr/include/QtHelp/QHelpSearchResult
/usr/include/QtHelp/QHelpSearchResultWidget
/usr/include/QtHelp/QtHelp
/usr/include/QtHelp/QtHelpDepends
/usr/include/QtHelp/QtHelpVersion
/usr/include/QtHelp/qcompressedhelpinfo.h
/usr/include/QtHelp/qhelp_global.h
/usr/include/QtHelp/qhelpcontentwidget.h
/usr/include/QtHelp/qhelpengine.h
/usr/include/QtHelp/qhelpenginecore.h
/usr/include/QtHelp/qhelpfilterdata.h
/usr/include/QtHelp/qhelpfilterengine.h
/usr/include/QtHelp/qhelpfiltersettingswidget.h
/usr/include/QtHelp/qhelpindexwidget.h
/usr/include/QtHelp/qhelplink.h
/usr/include/QtHelp/qhelpsearchengine.h
/usr/include/QtHelp/qhelpsearchquerywidget.h
/usr/include/QtHelp/qhelpsearchresultwidget.h
/usr/include/QtHelp/qthelpversion.h
/usr/include/QtQDocCatch/QtQDocCatchDepends
/usr/include/QtQDocCatch/catch/catch.hpp
/usr/include/QtQDocCatchConversionsPrivate/QtQDocCatchConversionsPrivateDepends
/usr/include/QtQDocCatchConversionsPrivate/catch_conversions/qdoc_catch_conversions.h
/usr/include/QtQDocCatchConversionsPrivate/catch_conversions/qt_catch_conversions.h
/usr/include/QtQDocCatchConversionsPrivate/catch_conversions/std_catch_conversions.h
/usr/include/QtQDocCatchGeneratorsPrivate/QtQDocCatchGeneratorsPrivateDepends
/usr/include/QtQDocCatchGeneratorsPrivate/catch_generators/generators/combinators/cycle_generator.h
/usr/include/QtQDocCatchGeneratorsPrivate/catch_generators/generators/combinators/oneof_generator.h
/usr/include/QtQDocCatchGeneratorsPrivate/catch_generators/generators/k_partition_of_r_generator.h
/usr/include/QtQDocCatchGeneratorsPrivate/catch_generators/generators/path_generator.h
/usr/include/QtQDocCatchGeneratorsPrivate/catch_generators/generators/qchar_generator.h
/usr/include/QtQDocCatchGeneratorsPrivate/catch_generators/generators/qstring_generator.h
/usr/include/QtQDocCatchGeneratorsPrivate/catch_generators/namespaces.h
/usr/include/QtQDocCatchGeneratorsPrivate/catch_generators/utilities/semantics/copy_value.h
/usr/include/QtQDocCatchGeneratorsPrivate/catch_generators/utilities/semantics/generator_handler.h
/usr/include/QtQDocCatchGeneratorsPrivate/catch_generators/utilities/semantics/move_into_vector.h
/usr/include/QtQDocCatchGeneratorsPrivate/catch_generators/utilities/statistics/distribution.h
/usr/include/QtQDocCatchGeneratorsPrivate/catch_generators/utilities/statistics/percentages.h
/usr/include/QtTools/6.6.3/QtTools/private/qttools-config_p.h
/usr/include/QtTools/QtTools
/usr/include/QtTools/QtToolsDepends
/usr/include/QtTools/QtToolsVersion
/usr/include/QtTools/qttools-config.h
/usr/include/QtTools/qttoolsversion.h
/usr/include/QtUiPlugin/QDesignerCustomWidgetCollectionInterface
/usr/include/QtUiPlugin/QDesignerCustomWidgetInterface
/usr/include/QtUiPlugin/QDesignerExportWidget
/usr/include/QtUiPlugin/QtUiPlugin
/usr/include/QtUiPlugin/QtUiPluginDepends
/usr/include/QtUiPlugin/QtUiPluginVersion
/usr/include/QtUiPlugin/customwidget.h
/usr/include/QtUiPlugin/qdesignerexportwidget.h
/usr/include/QtUiPlugin/qtuipluginversion.h
/usr/include/QtUiTools/6.6.3/QtUiTools/private/quiloader_p.h
/usr/include/QtUiTools/QUiLoader
/usr/include/QtUiTools/QtUiTools
/usr/include/QtUiTools/QtUiToolsDepends
/usr/include/QtUiTools/QtUiToolsVersion
/usr/include/QtUiTools/qtuitoolsglobal.h
/usr/include/QtUiTools/qtuitoolsversion.h
/usr/include/QtUiTools/quiloader.h
/usr/lib64/cmake/Qt6/FindWrapLibClang.cmake
/usr/lib64/cmake/Qt6BuildInternals/StandaloneTests/QtToolsTestsConfig.cmake
/usr/lib64/cmake/Qt6Designer/Qt6DesignerAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Designer/Qt6DesignerConfig.cmake
/usr/lib64/cmake/Qt6Designer/Qt6DesignerConfigVersion.cmake
/usr/lib64/cmake/Qt6Designer/Qt6DesignerConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Designer/Qt6DesignerDependencies.cmake
/usr/lib64/cmake/Qt6Designer/Qt6DesignerPlugins.cmake
/usr/lib64/cmake/Qt6Designer/Qt6DesignerTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Designer/Qt6DesignerTargets.cmake
/usr/lib64/cmake/Qt6Designer/Qt6DesignerVersionlessTargets.cmake
/usr/lib64/cmake/Qt6DesignerComponentsPrivate/Qt6DesignerComponentsPrivateAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6DesignerComponentsPrivate/Qt6DesignerComponentsPrivateConfig.cmake
/usr/lib64/cmake/Qt6DesignerComponentsPrivate/Qt6DesignerComponentsPrivateConfigVersion.cmake
/usr/lib64/cmake/Qt6DesignerComponentsPrivate/Qt6DesignerComponentsPrivateConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6DesignerComponentsPrivate/Qt6DesignerComponentsPrivateDependencies.cmake
/usr/lib64/cmake/Qt6DesignerComponentsPrivate/Qt6DesignerComponentsPrivateTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6DesignerComponentsPrivate/Qt6DesignerComponentsPrivateTargets.cmake
/usr/lib64/cmake/Qt6DesignerComponentsPrivate/Qt6DesignerComponentsPrivateVersionlessTargets.cmake
/usr/lib64/cmake/Qt6Help/Qt6HelpAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Help/Qt6HelpConfig.cmake
/usr/lib64/cmake/Qt6Help/Qt6HelpConfigVersion.cmake
/usr/lib64/cmake/Qt6Help/Qt6HelpConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Help/Qt6HelpDependencies.cmake
/usr/lib64/cmake/Qt6Help/Qt6HelpTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Help/Qt6HelpTargets.cmake
/usr/lib64/cmake/Qt6Help/Qt6HelpVersionlessTargets.cmake
/usr/lib64/cmake/Qt6Linguist/Qt6LinguistAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Linguist/Qt6LinguistConfig.cmake
/usr/lib64/cmake/Qt6Linguist/Qt6LinguistConfigVersion.cmake
/usr/lib64/cmake/Qt6Linguist/Qt6LinguistConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Linguist/Qt6LinguistDependencies.cmake
/usr/lib64/cmake/Qt6Linguist/Qt6LinguistTargets.cmake
/usr/lib64/cmake/Qt6Linguist/Qt6LinguistVersionlessTargets.cmake
/usr/lib64/cmake/Qt6LinguistTools/GenerateLUpdateProject.cmake
/usr/lib64/cmake/Qt6LinguistTools/Qt6LinguistToolsAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6LinguistTools/Qt6LinguistToolsConfig.cmake
/usr/lib64/cmake/Qt6LinguistTools/Qt6LinguistToolsConfigVersion.cmake
/usr/lib64/cmake/Qt6LinguistTools/Qt6LinguistToolsConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6LinguistTools/Qt6LinguistToolsDependencies.cmake
/usr/lib64/cmake/Qt6LinguistTools/Qt6LinguistToolsMacros.cmake
/usr/lib64/cmake/Qt6LinguistTools/Qt6LinguistToolsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6LinguistTools/Qt6LinguistToolsTargets.cmake
/usr/lib64/cmake/Qt6LinguistTools/Qt6LinguistToolsVersionlessTargets.cmake
/usr/lib64/cmake/Qt6QDocCatchConversionsPrivate/Qt6QDocCatchConversionsPrivateAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6QDocCatchConversionsPrivate/Qt6QDocCatchConversionsPrivateConfig.cmake
/usr/lib64/cmake/Qt6QDocCatchConversionsPrivate/Qt6QDocCatchConversionsPrivateConfigVersion.cmake
/usr/lib64/cmake/Qt6QDocCatchConversionsPrivate/Qt6QDocCatchConversionsPrivateConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6QDocCatchConversionsPrivate/Qt6QDocCatchConversionsPrivateTargets.cmake
/usr/lib64/cmake/Qt6QDocCatchConversionsPrivate/Qt6QDocCatchConversionsPrivateVersionlessTargets.cmake
/usr/lib64/cmake/Qt6QDocCatchGeneratorsPrivate/Qt6QDocCatchGeneratorsPrivateAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6QDocCatchGeneratorsPrivate/Qt6QDocCatchGeneratorsPrivateConfig.cmake
/usr/lib64/cmake/Qt6QDocCatchGeneratorsPrivate/Qt6QDocCatchGeneratorsPrivateConfigVersion.cmake
/usr/lib64/cmake/Qt6QDocCatchGeneratorsPrivate/Qt6QDocCatchGeneratorsPrivateConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6QDocCatchGeneratorsPrivate/Qt6QDocCatchGeneratorsPrivateTargets.cmake
/usr/lib64/cmake/Qt6QDocCatchGeneratorsPrivate/Qt6QDocCatchGeneratorsPrivateVersionlessTargets.cmake
/usr/lib64/cmake/Qt6QDocCatchPrivate/Qt6QDocCatchPrivateAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6QDocCatchPrivate/Qt6QDocCatchPrivateConfig.cmake
/usr/lib64/cmake/Qt6QDocCatchPrivate/Qt6QDocCatchPrivateConfigVersion.cmake
/usr/lib64/cmake/Qt6QDocCatchPrivate/Qt6QDocCatchPrivateConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6QDocCatchPrivate/Qt6QDocCatchPrivateTargets.cmake
/usr/lib64/cmake/Qt6QDocCatchPrivate/Qt6QDocCatchPrivateVersionlessTargets.cmake
/usr/lib64/cmake/Qt6Tools/Qt6ToolsAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Tools/Qt6ToolsConfig.cmake
/usr/lib64/cmake/Qt6Tools/Qt6ToolsConfigVersion.cmake
/usr/lib64/cmake/Qt6Tools/Qt6ToolsConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Tools/Qt6ToolsDependencies.cmake
/usr/lib64/cmake/Qt6Tools/Qt6ToolsTargets.cmake
/usr/lib64/cmake/Qt6Tools/Qt6ToolsVersionlessTargets.cmake
/usr/lib64/cmake/Qt6ToolsTools/Qt6ToolsToolsAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6ToolsTools/Qt6ToolsToolsConfig.cmake
/usr/lib64/cmake/Qt6ToolsTools/Qt6ToolsToolsConfigVersion.cmake
/usr/lib64/cmake/Qt6ToolsTools/Qt6ToolsToolsConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6ToolsTools/Qt6ToolsToolsDependencies.cmake
/usr/lib64/cmake/Qt6ToolsTools/Qt6ToolsToolsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6ToolsTools/Qt6ToolsToolsTargets.cmake
/usr/lib64/cmake/Qt6ToolsTools/Qt6ToolsToolsVersionlessTargets.cmake
/usr/lib64/cmake/Qt6UiPlugin/Qt6UiPluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6UiPlugin/Qt6UiPluginConfig.cmake
/usr/lib64/cmake/Qt6UiPlugin/Qt6UiPluginConfigVersion.cmake
/usr/lib64/cmake/Qt6UiPlugin/Qt6UiPluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6UiPlugin/Qt6UiPluginDependencies.cmake
/usr/lib64/cmake/Qt6UiPlugin/Qt6UiPluginTargets.cmake
/usr/lib64/cmake/Qt6UiPlugin/Qt6UiPluginVersionlessTargets.cmake
/usr/lib64/cmake/Qt6UiTools/Qt6UiToolsAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6UiTools/Qt6UiToolsConfig.cmake
/usr/lib64/cmake/Qt6UiTools/Qt6UiToolsConfigVersion.cmake
/usr/lib64/cmake/Qt6UiTools/Qt6UiToolsConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6UiTools/Qt6UiToolsDependencies.cmake
/usr/lib64/cmake/Qt6UiTools/Qt6UiToolsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6UiTools/Qt6UiToolsTargets.cmake
/usr/lib64/cmake/Qt6UiTools/Qt6UiToolsVersionlessTargets.cmake
/usr/lib64/libQt6Designer.prl
/usr/lib64/libQt6Designer.so
/usr/lib64/libQt6DesignerComponents.prl
/usr/lib64/libQt6DesignerComponents.so
/usr/lib64/libQt6Help.prl
/usr/lib64/libQt6Help.so
/usr/lib64/libQt6UiTools.prl
/usr/lib64/libQt6UiTools.so
/usr/lib64/pkgconfig/Qt6Designer.pc
/usr/lib64/pkgconfig/Qt6Help.pc
/usr/lib64/pkgconfig/Qt6Linguist.pc
/usr/lib64/pkgconfig/Qt6QDocCatchConversionsPrivate.pc
/usr/lib64/pkgconfig/Qt6QDocCatchGeneratorsPrivate.pc
/usr/lib64/pkgconfig/Qt6UiPlugin.pc
/usr/lib64/pkgconfig/Qt6UiTools.pc
/usr/lib64/qt6/mkspecs/modules/qt_lib_designer.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_designer_private.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_designercomponents_private.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_help.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_help_private.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_linguist.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_linguist_private.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_qdoccatch_private.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_qdoccatchconversionsprivate.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_qdoccatchconversionsprivate_private.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_qdoccatchgeneratorsprivate.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_qdoccatchgeneratorsprivate_private.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_tools_private.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_uiplugin.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_uitools.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_uitools_private.pri

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libQt6Designer.so.6.6.3
/V3/usr/lib64/libQt6DesignerComponents.so.6.6.3
/V3/usr/lib64/libQt6Help.so.6.6.3
/V3/usr/lib64/libQt6UiTools.so.6.6.3
/V3/usr/lib64/qt6/bin/assistant
/V3/usr/lib64/qt6/bin/designer
/V3/usr/lib64/qt6/bin/lconvert
/V3/usr/lib64/qt6/bin/linguist
/V3/usr/lib64/qt6/bin/lrelease
/V3/usr/lib64/qt6/bin/lupdate
/V3/usr/lib64/qt6/bin/pixeltool
/V3/usr/lib64/qt6/bin/qdbus
/V3/usr/lib64/qt6/bin/qdbusviewer
/V3/usr/lib64/qt6/bin/qtdiag
/V3/usr/lib64/qt6/bin/qtdiag6
/V3/usr/lib64/qt6/bin/qtplugininfo
/usr/lib64/libQt6Designer.so.6
/usr/lib64/libQt6Designer.so.6.6.3
/usr/lib64/libQt6DesignerComponents.so.6
/usr/lib64/libQt6DesignerComponents.so.6.6.3
/usr/lib64/libQt6Help.so.6
/usr/lib64/libQt6Help.so.6.6.3
/usr/lib64/libQt6UiTools.so.6
/usr/lib64/libQt6UiTools.so.6.6.3
/usr/lib64/qt6/bin/assistant
/usr/lib64/qt6/bin/designer
/usr/lib64/qt6/bin/lconvert
/usr/lib64/qt6/bin/linguist
/usr/lib64/qt6/bin/lrelease
/usr/lib64/qt6/bin/lupdate
/usr/lib64/qt6/bin/pixeltool
/usr/lib64/qt6/bin/qdbus
/usr/lib64/qt6/bin/qdbusviewer
/usr/lib64/qt6/bin/qtdiag
/usr/lib64/qt6/bin/qtdiag6
/usr/lib64/qt6/bin/qtplugininfo
/usr/lib64/qt6/metatypes/qt6designer_relwithdebinfo_metatypes.json
/usr/lib64/qt6/metatypes/qt6designercomponentsprivate_relwithdebinfo_metatypes.json
/usr/lib64/qt6/metatypes/qt6help_relwithdebinfo_metatypes.json
/usr/lib64/qt6/metatypes/qt6uitools_relwithdebinfo_metatypes.json
/usr/lib64/qt6/modules/Designer.json
/usr/lib64/qt6/modules/DesignerComponentsPrivate.json
/usr/lib64/qt6/modules/Help.json
/usr/lib64/qt6/modules/Linguist.json
/usr/lib64/qt6/modules/QDocCatchConversionsPrivate.json
/usr/lib64/qt6/modules/QDocCatchGeneratorsPrivate.json
/usr/lib64/qt6/modules/QDocCatchPrivate.json
/usr/lib64/qt6/modules/Tools.json
/usr/lib64/qt6/modules/UiPlugin.json
/usr/lib64/qt6/modules/UiTools.json

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/lprodump
/V3/usr/libexec/lrelease-pro
/V3/usr/libexec/lupdate-pro
/V3/usr/libexec/qhelpgenerator
/V3/usr/libexec/qtattributionsscanner
/usr/libexec/lprodump
/usr/libexec/lrelease-pro
/usr/libexec/lupdate-pro
/usr/libexec/qhelpgenerator
/usr/libexec/qtattributionsscanner

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qt6tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/qt6tools/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90
/usr/share/package-licenses/qt6tools/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/qt6tools/673921c2954e5b10a7388e0a2fc6be083a609bd3
/usr/share/package-licenses/qt6tools/715f995f11805ee85601834220c43b082f457ea3
/usr/share/package-licenses/qt6tools/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qt6tools/adadb67a9875aeeac285309f1eab6e47d9ee08a7
/usr/share/package-licenses/qt6tools/b073f11f0c81a95ab5e32aa6b5d23a5955a95274
/usr/share/package-licenses/qt6tools/be561fe6eb626c2566b9a6c0885554b4ee4e6b74
/usr/share/package-licenses/qt6tools/e28ab474db38a338e29ca698348e02915867084c
/usr/share/package-licenses/qt6tools/f45ee1c765646813b442ca58de72e20a64a7ddba
