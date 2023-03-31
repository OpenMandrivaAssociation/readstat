%define major 1
%define libname %mklibname readstat
%define devname %mklibname readstat -d

Name: readstat
Version: 1.1.8
Release: 2
Source0: https://github.com/WizardMac/ReadStat/releases/download/v%{version}/readstat-%{version}.tar.gz
Patch0: readstat-1.1.8-clang15-warnings.patch
Summary: Command-line tool and C library for converting SAS, Stata and SPSS files
URL: https://github.com/WizardMac/ReadStat
License: MIT
Group: System/Libraries
BuildRequires: gettext-devel
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: make
# So configure can detect iconv() works
BuildRequires: locales-extra-charsets

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
Provides: %{name}-devel = %{EVRD}

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
%{_mandir}/man1/*.1*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
