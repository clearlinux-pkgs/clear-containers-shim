#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clear-containers-shim
Version  : 3.0.3
Release  : 8
URL      : https://github.com/clearcontainers/shim/archive/3.0.3.tar.gz
Source0  : https://github.com/clearcontainers/shim/archive/3.0.3.tar.gz
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
%setup -q -n shim-3.0.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507938622
%autogen --disable-static --libexecdir=/usr/libexec/clear-containers
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1507938622
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/libexec/clear-containers/cc-shim
