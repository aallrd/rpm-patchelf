Name:           internal-patchelf
Version:        0.9
Release:        1%{?dist}
Summary:        PatchELF is a small utility to modify the dynamic linker and RPATH of ELF executables.
License:        GPL
URL:            http://nixos.org/patchelf.html
Source0:        https://nixos.org/releases/patchelf/patchelf-%{version}/patchelf-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot

# sysroot's configuration
#------------------------
%define _prefix         /opt/internal/root
%define _exec_prefix    %{_prefix}
%define _bindir         %{_exec_prefix}/bin
%define _libdir         %{_exec_prefix}/lib
%define _includedir     %{_prefix}/include
%define _sysconfdir     %{_prefix}/etc
%define _datadir        %{_prefix}/share
%define _mandir         %{_datadir}/man
%define _docdir         %{_datadir}/doc
%define _infodir        %{_datadir}/info
%define _localstatedir  %{_prefix}/var
#------------------------

%description
PatchELF is a simple utility for modifying existing ELF executables and
libraries.  It can change the dynamic loader ("ELF interpreter") of
executables and change the RPATH of executables and libraries.

%prep
%setup -qn patchelf-%{version}

%build
./configure --prefix=%{_prefix}
make
make check

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/patchelf
%doc %{_docdir}/patchelf/README
%{_mandir}/man1/patchelf.1

%changelog
* Thu Jan 17 2019 Antoine Allard <antoine.allard@internal.com>
- Copied and adpated RPM spec from the patchelf Github
