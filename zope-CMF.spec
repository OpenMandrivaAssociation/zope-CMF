%define product         CMF
%define version         1.6.2
%define release         1

%define zope_minver     2.7.3

%define zope_home       %{_prefix}/lib/zope
%define software_home   %{zope_home}/lib/python

Summary:        Zope Content Management Framework
Name:           zope-%{product}
Version:        %{version}
Release:        %mkrel %{release}
License:        ZPL
Group:          System/Servers
Source:         http://zope.org/Products/CMF/CMF-%{version}/CMF-%{version}.tar.bz2
URL:            http://www.zope.org/Products/CMF/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch
Requires:       zope >= %{zope_minver}
Provides:       zope-CMFActionIcons
Obsoletes:      zope-CMFActionIcons
Provides:       CMF = %{version}
Obsoletes:      CMF

%description
The Zope Content Management Framework provides a set of services and content
objects useful for building highly dynamic, content-oriented portal sites. As
packaged, the CMF generates a site much like the Zope.org site. The CMF is
intended to be easily customizable, in terms of both the types of content used
and the policies and services it provides.

%prep
%setup -q -n %{product}-%{version}

%build
# Not much, eh? :-)


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
%{__cp} -a CMF* %{buildroot}%{software_home}/Products/
%{__cp} -a DCWorkflow %{buildroot}%{software_home}/Products/


%clean
%{__rm} -rf %{buildroot}

%post
if [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
        service zope restart
fi

%postun
if [ -f "%{_prefix}/bin/zopectl" ] && [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
        service zope restart
fi

%files
%defattr(0644, root, root, 0755)
%{software_home}/Products/*
%doc docs *.txt

