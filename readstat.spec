%define major 0
%define libname %mklibname readstat
%define devname %mklibname readstat -d

Name: readstat
Version: 1.1.8
Release: 1
Source0: https://github.com/WizardMac/ReadStat/releases/download/v%{version}/readstat-%{version}.tar.gz
Patch0: readstat-1.1.8-clang15-warnings.patch
Summary: Command-line tool and C library for converting SAS, Stata and SPSS files
URL: https://github.com/WizardMac/ReadStat
License: MIT
Group: System/Libraries

%description
Command-line tool and C library for converting SAS, Stata and SPSS files

%package -n %{libname}
Summary: C library for converting SAS, Stata and SPSS files
Group: System/Libraries

%description -n %{libname}
C library for converting SAS, Stata and SPSS files

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}, a
C library for converting SAS, Stata and SPSS files

%prep
%autosetup -p1
%configure

%build
%make_build

%install
%make_install

%files
%{_bindir}/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
