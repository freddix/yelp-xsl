Summary:	XSL stylesheets for the Yelp help browser
Name:		yelp-xsl
Version:	3.14.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/yelp-xsl/3.14/%{name}-%{version}.tar.xz
# Source0-md5:	8965c1363857f223a6b761af6a37363d
URL:		http://projects.gnome.org/yelp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRequires:	perl-XML-Parser
BuildRequires:	pkg-config
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains XSL stylesheets that are used by the Yelp help
browser.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--enable-doc
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_datadir}/yelp-xsl
%{_npkgconfigdir}/yelp-xsl.pc

