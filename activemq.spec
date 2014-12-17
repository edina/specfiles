Summary: Apache ActiveMQ
Name: activemq
Version: 5.9.1
Release: 2%{?dist}
License: ASL 2.0
Group: System Environment/Daemons
URL: http://activemq.apache.org/
Source0: http://apache.mirrors.pair.com/activemq/%{version}/apache-activemq-%{version}-bin.tar.gz
Source1: info-provider-activemq
Source2: activemq-httpd.conf
Source3: activemq.xml
Source4: jetty.xml
Source5: jetty-realm.properties
Source6: credentials.properties
Source7: log4j.properties
Source8: activemq.defaults
Source9: activemq.init
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildArch: noarch

%define homedir /usr/share/%{name}
%define libdir /var/lib/%{name}
%define libexecdir /usr/libexec/%{name}
%define cachedir /var/cache/%{name}
%define docsdir /usr/share/doc/%{name}-%{version}

%description
ApacheMQ is a JMS Compliant Messaging System

%package info-provider
Summary: An LDAP information provider for activemq
Group:grid/lcg
%description info-provider
An LDAP infomation provider for activemq

%package meta
Summary: A metapackage
Group:grid/lcg
Requires: activemq = %{version}-%{release}, activemq-info-provider = %{version}-%{release}
%description meta
A metapackage

%prep
%setup -q -n apache-activemq-%{version}

%build
install --directory ${RPM_BUILD_ROOT}

%install
rm -rf $RPM_BUILD_ROOT
install --directory ${RPM_BUILD_ROOT}%{homedir}
install --directory ${RPM_BUILD_ROOT}%{homedir}/bin
install --directory ${RPM_BUILD_ROOT}%{docsdir}
install --directory ${RPM_BUILD_ROOT}%{libdir}/lib
install --directory ${RPM_BUILD_ROOT}%{libexecdir}
install --directory ${RPM_BUILD_ROOT}%{libdir}/webapps
install --directory ${RPM_BUILD_ROOT}%{cachedir}
install --directory ${RPM_BUILD_ROOT}%{cachedir}/data
install --directory ${RPM_BUILD_ROOT}/var/log/%{name}
install --directory ${RPM_BUILD_ROOT}/var/run/%{name}
install --directory ${RPM_BUILD_ROOT}/etc/%{name}
install --directory ${RPM_BUILD_ROOT}%{_initrddir}
install --directory ${RPM_BUILD_ROOT}/etc/httpd/conf.d
install --directory ${RPM_BUILD_ROOT}/etc/sysconfig

# Info provider
install %{SOURCE1} ${RPM_BUILD_ROOT}/%{libexecdir}

# Config files
install %{SOURCE2} ${RPM_BUILD_ROOT}/etc/httpd/conf.d
install %{SOURCE3} ${RPM_BUILD_ROOT}/etc/%{name}
install %{SOURCE4} ${RPM_BUILD_ROOT}/etc/%{name}
install %{SOURCE5} ${RPM_BUILD_ROOT}/etc/%{name}
install %{SOURCE6} ${RPM_BUILD_ROOT}/etc/%{name}
install %{SOURCE7} ${RPM_BUILD_ROOT}/etc/%{name}

# startup script
install %{SOURCE8} ${RPM_BUILD_ROOT}/etc/sysconfig/%{name}
install %{SOURCE9} ${RPM_BUILD_ROOT}%{_initrddir}/%{name}

# Bin and doc dirs
install *.txt LICENSE NOTICE ${RPM_BUILD_ROOT}%{docsdir}
cp -r docs ${RPM_BUILD_ROOT}%{docsdir}

install bin/activemq.jar bin/activemq-admin ${RPM_BUILD_ROOT}%{homedir}/bin
install --directory ${RPM_BUILD_ROOT}/usr/bin
%{__ln_s} -f %{homedir}/bin/activemq-admin ${RPM_BUILD_ROOT}/usr/bin

# Runtime directory
cp -r lib ${RPM_BUILD_ROOT}%{libdir}
cp -r webapps/admin ${RPM_BUILD_ROOT}%{libdir}/webapps

pushd ${RPM_BUILD_ROOT}%{homedir}
    [ -d conf ] || %{__ln_s} -f /etc/%{name} conf
    [ -d data ] || %{__ln_s} -f %{cachedir}/data data
    [ -d docs ] || %{__ln_s} -f %{docsdir} docs
    [ -d lib ] || %{__ln_s} -f %{libdir}/lib lib
    [ -d log ] || %{__ln_s} -f /var/log/%{name} log
    [ -d tmp ] || %{__ln_s} -f /tmp tmp
    [ -d webapps ] || %{__ln_s} -f %{libdir}/webapps webapps
popd

#pushd $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}
#  for file in $(ls -1)
#  do
#    sed -i 's,${activemq.base},/usr/share/activemq/,g' $file
#  done
#popd


%pre
# Add the "activemq" user and group
# we need a shell to be able to use su - later
/usr/sbin/groupadd -g 92 -r activemq 2> /dev/null || :
/usr/sbin/useradd -c "Apache Activemq" -u 92 -g activemq \
    -s /bin/bash -r -d /usr/share/activemq activemq 2> /dev/null || :

%post
# install activemq (but don't activate)
/sbin/chkconfig --add activemq

%preun
if [ $1 = 0 ]; then
    [ -f /var/lock/subsys/activemq ] && %{_initrddir}/activemq stop
    [ -f %{_initrddir}/activemq ] && /sbin/chkconfig --del activemq
fi
%postun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{homedir}
%docdir %{docsdir}
%{docsdir}
%{libdir}
%defattr(644,root,root)
%{libdir}/webapps/admin/WEB-INF/web.xml
%config(noreplace) /etc/httpd/conf.d/activemq-httpd.conf
%config(noreplace) /etc/%{name}/*
%config(noreplace) /etc/sysconfig/%{name}
%attr(755,root,root) /usr/bin/activemq-admin
%attr(755,activemq,activemq) %dir /var/log/%{name}
%attr(755,activemq,activemq) %dir /var/run/%{name}
%attr(775,root,activemq) %dir %{cachedir}/data
%attr(755,root,root) %{_initrddir}/activemq

%files info-provider
%defattr(-,root,root)
%attr(755,root,root) %{libexecdir}/info-provider-activemq

%changelog
* Wed Dec 17 2014 Andrew Seales <andrew.seales@ed.ac.uk> - 5.9.1-2
- Fix an issue with Queue JSP page with a bug preventing "Move" from working

* Fri Oct 03 2014 Richard Clamp <richardc@unixbeard.net> - 5.9.1-1
- Updated to 5.9.1 (CPR-32)
- Packaging cleanups as suggested by Jo Rhett in CPR-32
  - Unpack the magic wclg tarball and use the contents explicitly
  - Fix activemq init script status action (CPR-17)
  - Fix jetty admin password loading (CPR-32)
- Remove dependency on tanukiwrapper (CPR-47)

* Thu Oct 17 2013 Melissa Stone <melissa@puppetlabs.com> - 5.8.0-3
- Fix defattr on subpackages, remove broken link

* Wed Oct 16 2013 Melissa Stone <melissa@puppetlabs.com> - 5.8.0-2
- Conf file fixes that were initially missed

* Tue Oct 15 2013 Melissa Stone <melissa@puppetlabs.com> - 5.8.0-1
- Update for 5.8.0

* Fri Sep 02 2011 Michael Stahnke <stahnma@fedoraproject.org> - 5.5.0-1
- Update for 5.5.0

* Sat Jan 16 2010 R.I.Pienaar <rip@devco.net> 5.3.0
- Adjusted for ActiveMQ 5.3.0

* Wed Oct 29 2008 James Casey <james.casey@cern.ch> 5.2.0-2
- fixed defattr on subpackages

* Tue Sep 02 2008 James Casey <james.casey@cern.ch> 5.2.0-1
- Upgraded to activemq 5.2.0

* Tue Sep 02 2008 James Casey <james.casey@cern.ch> 5.1.0-7
- Added separate logging of messages whenever the logging interceptor is enabled in the config file
- removed BrokerRegistry messages casued by REST API
- now we don't log messages to stdout (so no duplicates in wrapper log).
- upped the number and size of the rolling logs

* Fri Aug 29 2008 James Casey <james.casey@cern.ch> 5.1.0-6
- make ServiceData be correct LDIF

* Wed Aug 27 2008 James Casey <james.casey@cern.ch> 5.1.0-5
- changed glue path from mds-vo-name=local to =resource
* Tue Aug 05 2008 James Casey <james.casey@cern.ch> 5.1.0-4
- fixed up info-provider to give both REST and STOMP endpoints

* Mon Aug 04 2008 James Casey <james.casey@cern.ch> 5.1.0-3
- reverted out APP_NAME change to ActiveMQ from init.d since it
  causes too many problems

* Mon Aug 04 2008 James Casey <james.casey@cern.ch> 5.1.0-2
- Added info-provider
- removed mysql as a requirement

* Thu Mar 20 2008 Daniel RODRIGUES <daniel.rodrigues@cern.ch> - 5.1-SNAPSHOT-1
- Changed to version 5.1 SNAPSHOT of 18 Mar, fizing AMQ Message Store
- small fixes to makefile

* Fri Dec 14 2007 James CASEY <james.casey@cern.ch> - 5.0.0-3rc4
- Added apache config file to forward requests to Jetty

* Thu Dec 13 2007 James CASEY <james.casey@cern.ch> - 5.0.0-2rc4
- fixed /usr/bin symlink
- added useJmx to the default config

* Thu Dec 13 2007 James CASEY <james.casey@cern.ch> - 5.0.0-RC4.1
- Moved to RC4 of the 5.0.0 release candidates

* Mon Dec 10 2007 James CASEY <james.casey@cern.ch> - 5.0-SNAPSHOT-7
- added symlink in /usr/bin for activemq-admin

* Wed Nov 26 2007 James CASEY <james.casey@cern.ch> - 5.0-SNAPSHOT-6
- fix bug with group name setting in init.d script

* Wed Nov 26 2007 James CASEY <jamesc@lxb6118.cern.ch> - 5.0-SNAPSHOT-5
- fix typos in config file for activemq

* Wed Nov 26 2007 James CASEY <jamesc@lxb6118.cern.ch> - 5.0-SNAPSHOT-4
- add support for lib64 version of tanukiwrapper in config
- turned off mysql persistence in the "default" config

* Wed Oct 17 2007 James CASEY <jamesc@lxb6118.cern.ch> - 5.0-SNAPSHOT-2
- more re-org to mirror how tomcat is installed.
- support for running as activemq user

* Tue Oct 16 2007 James CASEY <jamesc@lxb6118.cern.ch> - 5.0-SNAPSHOT-1
- Initial Version
