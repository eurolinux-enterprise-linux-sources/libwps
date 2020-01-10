%global apiversion 0.2

Name:		libwps
Version:	0.2.9
Release:	8%{?dist}
Summary:	Library for reading and converting Microsoft Works word processor documents

Group:		System Environment/Libraries
License:	LGPLv2+ or MPLv2.0
URL:		http://libwps.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz

BuildRequires:	boost-devel
BuildRequires:	doxygen
BuildRequires:	libwpd-devel

%description
Library that handles Microsoft Works documents.

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package tools
Summary:	Tools to transform Works documents into other formats
Group:		Applications/Publishing
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description tools
Tools to transform Works documents into other formats.
Currently supported: html, raw, text

%package doc
Summary:	Documentation of %{name} API
Group:		Documentation
BuildArch:	noarch

%description doc
The %{name}-doc package contains documentation files for %{name}

%prep
%setup -q
# Prevent autotools from being rerun
touch -r aclocal.m4 configure configure.in

%build
%configure --disable-silent-rules --disable-static --disable-werror
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
make install INSTALL="install -p" DESTDIR="%{buildroot}" 

find %{buildroot} -name '*.la' -exec rm -f {} ';'

# we install API docs directly from build
rm -rf %{buildroot}%{_defaultdocdir}/%{name}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc COPYING.LGPL COPYING.MPL CREDITS NEWS README
%{_libdir}/%{name}-%{apiversion}.so.*

%files devel
%doc HACKING
%{_includedir}/%{name}-%{apiversion}
%{_libdir}/%{name}-%{apiversion}.so
%{_libdir}/pkgconfig/%{name}-%{apiversion}.pc

%files tools
%{_bindir}/wps2html
%{_bindir}/wps2raw
%{_bindir}/wps2text

%files doc
%doc COPYING.LGPL COPYING.MPL
%doc docs/doxygen/html

%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 0.2.9-8
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.2.9-7
- Mass rebuild 2013-12-27

* Mon Sep 09 2013 David Tardon <dtardon@redhat.com> - 0.2.9-6
- Resolves: rhbz#1005711 do not compile in C++11 mode

* Mon Aug 19 2013 David Tardon <dtardon@redhat.com> - 0.2.9-5
- Resolves: rhbz#98166 Duplicated documentation

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 30 2013 David Tardon <dtardon@redhat.com> - 0.2.9-3
- drop build req. on cppunit

* Thu May 30 2013 David Tardon <dtardon@redhat.com> - 0.2.9-2
- libwps does not have any test suite

* Sat May 25 2013 David Tardon <dtardon@redhat.com> - 0.2.9-1
- new release

* Sun Apr 21 2013 David Tardon <dtardon@redhat.com> - 0.2.8-1
- new release

* Tue Apr 16 2013 Caolán McNamara <caolanm@redhat.com> - 0.2.7-5
- Resolves: rhbz#925931 support aarch64

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 27 2012 David Tardon <dtardon@redhat.com> - 0.2.7-3
- rebuilt for boost 1.50

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 29 2012 David Tardon <dtardon@redhat.com> - 0.2.7-1
- new release

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-3
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 01 2011 David Tardon <dtardon@redhat.com> - 0.2.4-1
- latest version

* Fri Nov 18 2011 David Tardon <dtardon@redhat.com> - 0.2.3-1
- latest version
- remove obsoleted patch

* Wed Jul 13 2011 David Tardon <dtardon@redhat.com> - 0.2.2-1
- latest version

* Tue Jun 28 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.2.0-3
- Remove -Werror from CFLAGS/CXXFLAGS (Add libwps-0.2.0-werror.patch)
  (Fix FTBFS BZ#715767).

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Dec 05 2010 Caolán McNamara <caolanm@redhat.com> - 0.2.0-1
- latest version

* Sat Jan 30 2010 Chen Lei <supercyper@163.com> - 0.1.2-7
- Add noarch to -doc subpackage

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 10 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 0.1.2-5
- Correct DOC issues (again) RHBZ: #484933 / C14

* Sun Feb 15 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 0.1.2-4
- Correct path for CHECK section

* Sun Feb 15 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 0.1.2-3
- Add CHECK section
- Add cppunit-devel to BuildRequires

* Sun Feb 15 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 0.1.2-2
- Correct DOC issues
- Delete wrong pkgconfig pathes 

* Tue Feb 10 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 0.1.2-1
- Initial Package build 
