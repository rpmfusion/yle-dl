
Name:		yle-dl
Version:	2.0.1
Release:	4%{?dist}
License:	GPLv2
Summary:	Command-line tool to download videos from Finnish broadcasting company
Group:		Applications/Multimedia
Url:		http://users.tkk.fi/~aajanki/rtmpdump-yle/
Source0:	http://users.tkk.fi/~aajanki/rtmpdump-yle/%{name}-%{version}.tar.gz

BuildRequires:	openssl-devel, json-c-devel, python-devel
Requires:		rtmpdump, python-crypto
BuildArch:		noarch


%description
yle-dl is a command-line program for downloading media files
from the two video streaming services of the Finnish national
broadcasting company YLE: Yle Areena (http://areena.yle.fi/), 
and Elävä Arkisto (http://www.yle.fi/elavaarkisto/).
It is an extension of RTMPDump (http://rtmpdump.mplayerhq.hu/), 
which is based on XBMC RTMP code used in RTMPDumper by team 
boxee. 


%prep
%setup -q -n %{name}-%{version}


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_docdir}
mkdir -p %{buildroot}/%{_datadir}/%{name}
make DESTDIR=%{buildroot} prefix=%{_usr}  install


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root)
%doc ChangeLog COPYING README README.fi
%{_bindir}/yle-dl
%{_datadir}/%{name}


%changelog
* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Aug 08 2012 Juha Tuomala <tuju@iki.fi> 2.0.1-3
- Minor pkg cleanups.

* Sun Aug 08 2012 Juha Tuomala <tuju@iki.fi> 2.0.1-2
- update to 2.0.1

* Sat Jun 4 2011 Juha Tuomala <tuju@iki.fi> 1.4.2-1
- Initial RPM creation.
