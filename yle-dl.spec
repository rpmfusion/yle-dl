Name:		yle-dl
Epoch:      1
Version:	2.26
Release:	6%{?dist}
License:	GPLv3
Summary:	Command-line tool to download videos from Finnish broadcasting company
URL:		http://aajanki.github.io/yle-dl/
Source0:    https://github.com/aajanki/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	python2-devel
BuildRequires:	python2-setuptools
BuildRequires:	sed
Requires:		rtmpdump
Requires:		python2-crypto
Requires:		python2-requests
Requires:		python-progress
Requires:		python2-lxml
Requires:		php-cli
Requires:		php-bcmath
Requires:		php-xml
Requires:		php-mcrypt

BuildArch:		noarch

%description
yle-dl is a command-line program for downloading media files
from the two video streaming services of the Finnish national
broadcasting company YLE: Yle Areena (http://areena.yle.fi/),
and Elävä Arkisto (http://yle.fi/aihe/elava-arkisto/) and
partial support for Yle Arkivet (http://svenska.yle.fi/arkivet).
The videos are saved in Flash video (FLV) format.
yle-dl is an extension of RTMPDump (http://rtmpdump.mplayerhq.hu/),
which is based on XBMC RTMP code used in RTMPDumper by team
boxee.


%prep
%autosetup
sed -i -e 's@/usr/bin/env python2@/usr/bin/python2@g' yledl/yledl.py

%build
%py2_build

%install
%py2_install
chmod a+x %{buildroot}%{python2_sitelib}/yledl/yledl.py

%files
%doc ChangeLog README.md README.fi
%license COPYING
%{_bindir}/yle-dl
%{python2_sitelib}/yledl/
%{python2_sitelib}/yle_dl-%{version}-py2.7.egg-info/


%changelog
* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:2.26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 1:2.26-5
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:2.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1:2.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Leigh Scott <leigh123linux@googlemail.com> - 1:2.26-2
- Epoch back to 2.26 as python-pyamf isn't available in fedora

* Mon Jan 01 2018 Sérgio Basto <sergio@serjux.com> - 2.30-1
- Update to 2.30

* Sun Oct 08 2017 Leigh Scott <leigh123linux@googlemail.com> - 2.24-1
- Update to 2.24
- Clean up spec file

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 21 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 07 2016 Sérgio Basto <sergio@serjux.com> - 2.13-1
- Update to 2.13

* Sat Jul 23 2016 Sérgio Basto <sergio@serjux.com> - 2.10.2-1
- Update yle-dl 2.10.2

* Tue Jan 12 2016 Sérgio Basto <sergio@serjux.com> - 2.10.0-1
- Update yle-dl to 2.10.0

* Wed Nov 18 2015 Sérgio Basto <sergio@serjux.com> - 2.9.0-1
- Update yle-dl to 2.9.0
- adobehds is no longer needed

* Sun Oct 18 2015 Sérgio Basto <sergio@serjux.com> - 2.8.1-2
- Added to Requires php-mcrypt

* Tue Sep 22 2015 Sérgio Basto <sergio@serjux.com> - 2.8.1-1
- Update to 2.8.1 and AdobeHDS.php also updated

* Sun Jun 07 2015 Sérgio Basto <sergio@serjux.com> - 2.7.2-1
- Update to 2.7.2 .
- Update Requires dependencies .

* Sat May 16 2015 Sérgio Basto <sergio@serjux.com> - 2.7.1-1
- Update to 2.7.1 .
- Update BuildRequires .

* Tue May 12 2015 Sérgio Basto <sergio@serjux.com> - 2.7.0-2
- Include file named AdobeHDS.php, instead download it in every build.

* Thu May 07 2015 Sérgio Basto <sergio@serjux.com> - 2.7.0-1
- Update to 2.7.0 .

* Wed Mar 04 2015 Jani Patanen <ceuatjtm63@snkmail.com> - 2.6.0-1
- update to 2.6.0

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug 08 2012 Juha Tuomala <tuju@iki.fi> 2.0.1-3
- Minor pkg cleanups.

* Wed Aug 08 2012 Juha Tuomala <tuju@iki.fi> 2.0.1-2
- update to 2.0.1

* Sat Jun 4 2011 Juha Tuomala <tuju@iki.fi> 1.4.2-1
- Initial RPM creation.

