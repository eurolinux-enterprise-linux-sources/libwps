%global apiversion 0.4

Name:		libwps
Version:	0.4.7
Release:	1%{?dist}
Summary:	A library for import of Microsoft Works documents

License:	LGPLv2+ or MPLv2.0
URL:		http://libwps.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz

BuildRequires:	doxygen
BuildRequires:	help2man
BuildRequires:	pkgconfig(librevenge-0.0)

%description
%{name} is a library for import of Microsoft Works text documents,
spreadsheets and (in a limited way) databases. Full list of supported
formats is available at
https://sourceforge.net/p/libwps/wiki/Home/#recognized-formats .

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package tools
Summary:	Tools to transform Microsoft Works documents into other formats
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description tools
Tools to transform Microsoft Works documents into other formats.
Currently supported: CSV, HTML, raw, text

%package doc
Summary:	Documentation of %{name} API
BuildArch:	noarch

%description doc
The %{name}-doc package contains documentation files for %{name}

%prep
%autosetup -p1

%build
%configure --disable-silent-rules --disable-static --disable-werror --with-sharedptr=c++11
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
make install INSTALL="install -p" DESTDIR="%{buildroot}" 
rm -f %{buildroot}%{_libdir}/*.la
# we install API docs directly from build
rm -rf %{buildroot}%{_defaultdocdir}/%{name}

export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
for tool in wks2csv wks2raw wks2text wps2html wps2raw wps2text; do
    help2man -S '%{name} %{version}' -N -o ${tool}.1 %{buildroot}%{_bindir}/${tool}
done
install -m 0755 -d %{buildroot}/%{_mandir}/man1
install -m 0644 wks2*.1 wps2*.1 %{buildroot}/%{_mandir}/man1

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc CREDITS NEWS README
%license COPYING.LGPL COPYING.MPL
%{_libdir}/%{name}-%{apiversion}.so.*

%files devel
%{_includedir}/%{name}-%{apiversion}
%{_libdir}/%{name}-%{apiversion}.so
%{_libdir}/pkgconfig/%{name}-%{apiversion}.pc

%files tools
%{_bindir}/wks2csv
%{_bindir}/wks2raw
%{_bindir}/wks2text
%{_bindir}/wps2html
%{_bindir}/wps2raw
%{_bindir}/wps2text
%{_mandir}/man1/wks2csv.1*
%{_mandir}/man1/wks2raw.1*
%{_mandir}/man1/wks2text.1*
%{_mandir}/man1/wps2html.1*
%{_mandir}/man1/wps2raw.1*
%{_mandir}/man1/wps2text.1*

%files doc
%license COPYING.LGPL COPYING.MPL
%doc docs/doxygen/html

%changelog
* Mon Sep 18 2017 David Tardon <dtardon@redhat.com> - 0.4.7-1
- Resolves: rhbz#1477108 rebase to 0.4.7

* Fri Apr 17 2015 David Tardon <dtardon@redhat.com> - 0.3.1-1
- Resolves: rhbz#1207762 rebase to 0.3.1

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
