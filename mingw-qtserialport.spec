%?mingw_package_header

%global name1 qtserialport

%global commit 56ebaec
%global snapshot .git20170204.%{commit}

Name:           mingw-%{name1}
Summary:        MinGW Windows QtSerialPort Qt4 library
Version:        5.4.0
Release:        1.beta1%{snapshot}%{?dist}
URL:            https://wiki.qt.io/QtSerialPort
License:        LGPLv2.1
# git clone git://code.qt.io/qt/qtserialport.git
# cd qtserialport
# git checkout qt4-dev
# git archive --prefix=qtserialport/ qt4-dev | bzip2 >../qtserialport.tar.bz2
Source:         qtserialport.tar.bz2
# fix empty QMAKE_MKDIR
Patch0:         qtserialport-mkdir-workaround.patch
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw32-qt
BuildRequires:  mingw64-qt
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-gcc-c++
BuildArch:      noarch

%description
MinGW Windows QtSerialPort Qt4 library.


%package -n mingw32-%{name1}
Summary:        MinGW Windows QtSerialPort Qt4 library

%description -n mingw32-%{name1}
MinGW Windows QtSerialPort Qt4 library.

%package -n mingw64-%{name1}
Summary:        MinGW Windows QtSerialPort Qt4 library

%description -n mingw64-%{name1}
MinGW Windows QtSerialPort Qt4 library.


%?mingw_debug_package

%prep
%setup -qcn %{name1}
%patch0 -p0
mv %{name1} win32
cp -r win32 win64

%build
%if 0%{?mingw_build_win32} == 1
pushd win32
%mingw32_qmake_qt4
make qmake
make %{?_smp_mflags}
popd
%endif
%if 0%{?mingw_build_win64} == 1
pushd win64
%mingw64_qmake_qt4
make qmake
make %{?_smp_mflags}
popd
%endif

%install
%if 0%{?mingw_build_win32} == 1
pushd win32
make INSTALL_ROOT=$RPM_BUILD_ROOT install
popd
%endif
%if 0%{?mingw_build_win64} == 1
pushd win64
make INSTALL_ROOT=$RPM_BUILD_ROOT install
popd
%endif

# .prl files aren't interesting for us
find $RPM_BUILD_ROOT -name "*.prl" -delete
# the same files as go to bin
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/QtSerialPort4.dll
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/QtSerialPort4.dll

%files -n mingw32-%{name1}
%doc win32/LGPL_EXCEPTION.txt win32/LICENSE.FDL win32/LICENSE.LGPL win32/README
%{mingw32_bindir}/QtSerialPort4.dll
%{mingw32_includedir}/QtSerialPort/
%{mingw32_libdir}/libQtSerialPort4.a
%{mingw32_datadir}/qt4/mkspecs/features/serialport.*

%files -n mingw64-%{name1}
%doc win64/LGPL_EXCEPTION.txt win64/LICENSE.FDL win64/LICENSE.LGPL win64/README
%{mingw64_bindir}/QtSerialPort4.dll
%{mingw64_includedir}/QtSerialPort/
%{mingw64_libdir}/libQtSerialPort4.a
%{mingw64_datadir}/qt4/mkspecs/features/serialport.*

%changelog
* Sat Feb 04 2017 Jajauma's Packages <jajauma@yandex.ru> - 5.4.0-1.beta1.git20170204.56ebaec
- Initial release
