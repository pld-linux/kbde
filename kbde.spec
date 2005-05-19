Summary:	Keyboard emulation utility
Summary(pl):	Narzêdzie do emulacji klawiatury
Name:		kbde
Version:	1.1.2
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/kbde/%{name}-%{version}.tar.gz
# Source0-md5:	2217c2b1aaae2c5ef5dcd800bbde0021
URL:		http://kbde.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Keyboard emulation utility supposed to work with kbde-driver to
emulate keyboard input on the x86 computer.

%description -l pl
Narzêdzie do emulacji klawiatury, które powinno dzia³aæ ze
sterownikiem kbde-driver, emuluj±c wej¶cie z klawiatury na komputerach
x86.

%package devel
Summary:	Keyboard emulation development library
Summary(pl):	Biblioteka do emulacji klawiatury
License:	LGPL
Group:		Development/Libraries

%description devel
Library for generate strings that can be send to the keyboard
emulation driver for emulate keyboard input.

%description devel -l pl
Biblioteka s³u¿±ca do generowania ³añcuchów, które mog± byæ wys³ane
do sterownika emulacji klawiatury.

%prep
%setup -q

%build
%{__make} \
	CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/kbde
%{_mandir}/man1/kbde.1*

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/kbde
%{_includedir}/kbde/kbde.h
%{_libdir}/libkbde.a
%{_mandir}/man3/kbde.3*
%{_mandir}/man3/kbde_ascii.3*
%{_mandir}/man3/kbde_misc.3*
%{_mandir}/man7/xt_kbde_scancode.7*
