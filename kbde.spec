%define my_name        kbde
%define my_version     1.0.0
%define my_release     1

Name:        %{my_name}
Version:     %{my_version}
Release:     %{my_release}
License:     GPL
Group:       Applications/System
Summary:     Keyboard emulation utility
Packager:    Valery Reznic <valery_reznic@users.sourceforge.net>
Source:      %{name}-%{version}.tar.gz
Url:         http://kbde.sourceforge.net
BuildRoot:   %{_builddir}/%{buildsubdir}-install-root

%description
Keyboard emulation utility supposed to work with kbde-driver
to emulate keybiard input on the x86 computer.

%prep
%setup

%build
make all

%install
if [ "$RPM_BUILD_ROOT" != "/" ]; then
   rm -rf $RPM_BUILD_ROOT
else
   :
fi
make install DESTDIR="$RPM_BUILD_ROOT" MANPAGE_SUFFIX=".gz"

%clean
if [ "$RPM_BUILD_ROOT" != "/" ]; then
   rm -rf $RPM_BUILD_ROOT
else
   :
fi

%files
%defattr(-,root,root)

/usr/bin/kbde
%doc %{_mandir}/man1/kbde.1*

%doc AUTHORS
%doc ChangeLog
%doc INSTALL
%doc LICENSE
%doc NEWS
%doc README

#### Devel Package ####

%package devel
Summary: keyboard emulation development library
Group:   System Environment/Libraries

%description devel
Library for generate strings that can be send to the 
keyboard emulation driver for emulate keyboard input

%files devel
%defattr(-,root,root)
/usr/include/kbde/kbde.h
/usr/lib/libkbde.a

%doc %{_mandir}/man3/kbde.3*
%doc %{_mandir}/man3/kbde_ascii.3*
%doc %{_mandir}/man3/kbde_misc.3*
%doc %{_mandir}/man7/xt_kbde_scancode.7*

%doc LICENSE.LIB

%changelog
* Thu Nov 20 2003 <valery_reznic@users.sourceforge.net> 1.0.0-1
- Initial public release.
