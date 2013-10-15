%global		gitver	51f30c8

Name:		yle-dl
Version:	2.1.0
Release:	0.2.git%{gitver}%{?dist}
License:	GPLv2
Summary:	Command-line tool to download videos from Finnish broadcasting company
Group:		Applications/Multimedia
Url:		http://users.tkk.fi/~aajanki/rtmpdump-yle/
Source0:	http://users.tkk.fi/~aajanki/rtmpdump-yle/%{name}-%{version}-0-g%{gitver}.tar.gz

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
%setup -q -n aajanki-yle-dl-%{gitver}


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
* Tue Oct 10 2013 Juha Tuomala <tuju@iki.fi> 2.1.0-0.2.git51f30c8
- bump for build.

* Fri Oct 10 2013 Juha Tuomala <tuju@iki.fi> 2.1.0-0-g51f30c8
- Update to 2.1.0-git51f30c8.

* Sun Aug 08 2012 Juha Tuomala <tuju@iki.fi> 2.0.1-3
- Minor pkg cleanups.

* Sun Aug 08 2012 Juha Tuomala <tuju@iki.fi> 2.0.1-2
- update to 2.0.1

* Sat Jun 4 2011 Juha Tuomala <tuju@iki.fi> 1.4.2-1
- Initial RPM creation.
