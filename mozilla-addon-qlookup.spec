Summary:	Search tool in context menu
Summary(pl):	Wyszukiwarka w menu kontekstowym
Name:		mozilla-addon-qlookup
%define		_realname	qlookup
Version:	0.1.0
Release:	3
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://www.xenolinguistics.com/qlookup.mozdev/qlookup/www/%{_realname}.xpi
Source1:	%{_realname}-installed-chrome.txt
URL:		http://qlookup.mozdev.org/
BuildRequires:	unzip
BuildRequires:	zip
Requires(post,postun):	textutils
Requires:	mozilla >= 1.0-7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_libdir}/mozilla/chrome

%description
A tool for simple and quick searching of text selected in browser
window, accessible from context menu.

%description -l pl
Proste i szybkie wyszukiwanie zaznaczanego tekstu w oknie przegl±darki
po wywo³aniu menu kontekstowego.

%prep
%setup -q -c %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

cd %{_realname}
rm -r CVS
rm -r content/CVS
rm content/*~
zip -r -9 -m ../%{_realname}.jar ./
cd -

install %{_realname}.jar $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%postun
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
