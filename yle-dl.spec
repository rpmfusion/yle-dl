Name:		yle-dl
Version:	2.7.0
Release:	2%{?dist}
License:	GPLv2
Summary:	Command-line tool to download videos from Finnish broadcasting company
Group:		Applications/Multimedia
Url:		http://aajanki.github.io/yle-dl/
#Source0:   https://github.com/aajanki/%{name}/archive/%{name}-%{version}.tar.gz
Source0:    http://github.srcurl.net/aajanki/%{name}/%{version}/%{name}-%{version}.tar.gz
Source1:    https://raw.githubusercontent.com/K-S-V/Scripts/master/AdobeHDS.php

BuildRequires:	openssl-devel, json-c-devel, python-devel
Requires:		rtmpdump, python-crypto, php
BuildArch:		noarch

#global commit 158c026271198696a7a329b3c2de3e2197de3e25
#global shortcommit %(c=%{commit}; echo ${c:0:7})

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
%setup -q

%build
sed -i 's|/usr/local/share/yle-dl/AdobeHDS.php|/usr/share/yle-dl/AdobeHDS.php|g' %{_builddir}/%{name}-%{version}/yle-dl

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_docdir}
mkdir -p %{buildroot}/%{_datadir}/%{name}
make DESTDIR=%{buildroot} prefix=%{_usr}  install
install -m 0644 -D %{SOURCE1} \
    %{buildroot}/%{_datadir}/%{name}
make DESTDIR=%{buildroot} prefix=%{_usr}  install-adobehds

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README.md README.fi
%{_bindir}/yle-dl
%{_datadir}/%{name}


%changelog
* Tue May 12 2015 Sérgio Basto <sergio@serjux.com> - 2.7.0-2
- Include file named AdobeHDS.php , instead download it every build.

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

