#
# spec file for package apache2-mod_jk (Version 1.2.30)
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild


Name:           apache2-mod_jk

%if 0%{?suse_version}
BuildRequires:  apache2-devel pcre-devel gcc-c++
%if 0%{?suse_version} > 1210
BuildRequires:  java-1_7_0-openjdk-devel
%else
BuildRequires:  java-1_6_0-openjdk-devel
%endif
%endif

%if 0%{?rhel_version} || 0%{?centos_version}
BuildRequires:  httpd >= 2.2 httpd-devel >= 2.2 pcre-devel java-1.6.0-openjdk-devel gcc-c++ ruby-libs
%endif

%define section        free
%define       connectors_root  		tomcat-connectors-%{version}-src
%if 0%{?suse_version}
%define       apache2_sysconfdir        %(/usr/sbin/apxs2 -q SYSCONFDIR)
%define       apache2_libexecdir        %(/usr/sbin/apxs2 -q LIBEXECDIR)
%define       apache2_cflags            %(/usr/sbin/apxs2 -q CFLAGS)
%endif
%if 0%{?rhel_version} || 0%{?centos_version}
%define       apache2_sysconfdir        %(/usr/sbin/apxs -q SYSCONFDIR)
%define       apache2_libexecdir        %(/usr/sbin/apxs -q LIBEXECDIR)
%define       apache2_cflags            %(/usr/sbin/apxs -q CFLAGS)
%endif
Summary:        Connectors between Apache and Tomcat Servlet Container
Version:        1.2.37
Release:        4.1
License:        Apache Software License ..
Group:          Productivity/Networking/Web/Frontends
%if 0%{?suse_version}
Requires:       apache2
%endif
%if 0%{?rhel_version} || 0%{?centos_version}
Requires:       httpd >= 2.2
%endif
Provides:       mod_jk = %{version}-%{release}
Provides:       mod_jk-ap20
%if 0%{?suse_version}
Provides:       mod_jk-ap20:%{_libdir}/apache2/mod_jk.so
%endif
%if 0%{?rhel_version} || 0%{?centos_version}
Provides:       mod_jk-ap20:%{_libdir}/httpd/modules/mod_jk.so
%endif
Obsoletes:      mod_jk-ap20 < %{version}
Obsoletes:      tomcat-mod  < %{version}
Url:            http://jakarta.apache.org
Source0:        http://www.apache.org/dist/tomcat/tomcat-connectors/jk/source/jk-%{version}/tomcat-connectors-%{version}-src.tar.gz
Source1:        jk.conf
Source2:        README.SUSE
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package provides modules for Apache to invisibly integrate Tomcat
capabilities into an existing Apache installation.

To load the module into Apache, run the command "a2enmod jk" as root.



Authors:
--------
    Hans Bergsten <hans@gefionsoftware.com>
    James Duncan <Davidson duncan@x180.com>
    Pierpaolo Fumagalli <pier@apache.org>
    Craig McClanahan <cmcclanahan@mytownnet.com>
    Sam Ruby <rubys@us.ibm.com>
    Jon Stevens <jon@clearink.com>
    Anil Vijendran <akv@eng.sun.com>
    Brian Behlendorf <brian@behlendorf.com>
    Kevin Burton <burton@relativity.yi.org>
    Danno Ferrin <shemnon@earthlink.net>
    Jason Hunter <jh@servlets.com>
    Ramesh Mandava <rmandava@talentportal.com>
    Stefano Mazzocchi <stefano@apache.org>
    Rajiv Mordani <mode@chinet.com>
    Harish Prabhandham <harishp@onebox.com>
    Jean-Luc Rochat <shachor@il.ibm.com>
    James Todd <jwtodd@pacbell.net>

%prep
%setup -q -n %{connectors_root}

%build
# prepare apr
export APACHE2_CFLAGS="%{apache2_cflags}"
cd $RPM_BUILD_DIR/%{connectors_root}/native
%if 0%{?rhel_version} || 0%{?centos_version}
./configure --with-apxs=/usr/sbin/apxs
%else if 0%{?suse_version}
./configure --with-apxs=/usr/sbin/apxs2
%endif
make

%install
# AJP Connector jk
install -d -m 755 $RPM_BUILD_ROOT%{apache2_libexecdir}
pushd $RPM_BUILD_DIR/%{connectors_root}
install -m 755 native/apache-2.0/.libs/mod_jk.so $RPM_BUILD_ROOT%{apache2_libexecdir}/
popd
cp %{SOURCE1} .
cp %{SOURCE2} .

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%if 0%{?suse_version}
%doc LICENSE README.SUSE
%else
%doc LICENSE
%endif
#mod_jk.conf.sample workers.properties.sample
%doc conf/workers.properties
%doc jk.conf
%{apache2_libexecdir}/*

%changelog
* Thu Aug 18 2011 stoppe@gmx.de
- Initial release
