%define Product CMF
%define product cmf
%define name    zope-%{Product}
%define version 2.1.0
%define release %mkrel 7

%define zope_minver     2.7.3
%define zope_home       %{_prefix}/lib/zope
%define software_home   %{zope_home}/lib/python

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    Zope Content Management Framework
License:    ZPL
Group:      System/Servers
URL:        http://www.zope.org/Products/%{Product}
Source:     http://zope.org/Products/%{Product}/%{Product}-%{version}/%{Product}-%{version}.tar.gz
Requires:   zope >= %{zope_minver}
Provides:   zope-CMFActionIcons = %{version}-%{release}
Provides:   zope-CMFCalendar = %{version}-%{release}
Provides:   zope-CMFCore = %{version}-%{release}
Provides:   zope-CMFDefault = %{version}-%{release}
Provides:   zope-CMFTopic = %{version}-%{release}
Provides:   zope-CMFUid = %{version}-%{release}
Provides:   zope-DCWorkflow = %{version}-%{release}
Provides:   zope-GenericSetup = %{version}-%{release}
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
The Zope Content Management Framework provides a set of services and content
objects useful for building highly dynamic, content-oriented portal sites. As
packaged, the CMF generates a site much like the Zope.org site. The CMF is
intended to be easily customizable, in terms of both the types of content used
and the policies and services it provides.

%prep
%setup -q -n %{Product}-%{version}

%build
# Not much, eh? :-)

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
%{__cp} -a CMF* %{buildroot}%{software_home}/Products/
%{__cp} -a DCWorkflow %{buildroot}%{software_home}/Products/
%{__cp} -a GenericSetup %{buildroot}%{software_home}/Products/

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
%defattr(-,root,root)
%doc docs *.txt
%{software_home}/Products/*
