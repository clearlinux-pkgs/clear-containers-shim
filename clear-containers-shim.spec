#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clear-containers-shim
Version  : 7395241884095515189211
Release  : 1
URL      : https://github.com/clearcontainers/shim/archive/master/739e5e241f8c8409c5dfc5d15a189dbbfc2d1bd1.tar.gz
Source0  : https://github.com/clearcontainers/shim/archive/master/739e5e241f8c8409c5dfc5d15a189dbbfc2d1bd1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause ISC MIT
Requires: clear-containers-shim-bin
BuildRequires : go

%description
This repository holds supplemental Go packages for low-level interactions with the operating system.

%package bin
Summary: bin components for the clear-containers-shim package.
Group: Binaries

%description bin
bin components for the clear-containers-shim package.


%prep
%setup -q -n shim-master

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505415889
%autogen --disable-static
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1505415889
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/libexec/cc-shim
