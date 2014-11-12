# Copyright (c) 2000-2007, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%bcond_without native
%if "%{?rhel}" == "6"
%bcond_without zip
%else
%bcond_with zip
%endif

%define base_name   daemon
%define short_name  commons-%{base_name}

Name:           apache-commons-daemon-jsvc-eap6
Version:        1.0.15
Release:        6.redhat_2%{?dist}
Epoch:          1
Summary:        Defines API to support an alternative invocation mechanism
License:        ASL 2.0
Group:          Applications/System
URL:            http://commons.apache.org/daemon/
Source0:        http://www.apache.org/dist/commons/daemon/source/commons-daemon-1.0.15-src.tar.gz
Patch0:          %{name}-crosslink.patch
#based on http://pkgs.fedoraproject.org/cgit/apache-commons-daemon.git/tree/apache-commons-daemon-secondary.patch
Patch1:          %{name}-secondary.patch
#Not needed for EAP build
#Patch2:          %{name}-ia64-configure.patch
#Patch3:          %{name}-s390x-configure.patch
#Patch4:          %{name}-ppc64-configure.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
%if "%{?rhel}" == "7"
#64 bit only natives on RHEL 7
ExcludeArch:   i686 i386
%endif

%if %with native
%if "%{?rhel}" == "7"
BuildRequires:  java6-devel
%else
BuildRequires:  java-devel >= 1.6.0
%endif
BuildRequires:  libcap-devel
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  docbook-utils
BuildRequires:  xmlto
BuildRequires:  unzip
%endif
BuildRequires:  jpackage-utils >= 0:1.6

Requires:       libcap
Requires:       apache-commons-daemon-eap6

%description
The scope of this package is to define an API in line with the current
Java(tm) Platform APIs to support an alternative invocation mechanism
which could be used instead of the above mentioned public static void
main(String[]) method.  This specification cover the behavior and life
cycle of what we define as Java(tm) daemons, or, in other words, non
interactive Java(tm) applications.

%if %with zip
%package src-zip
Summary:     Container for the source distribution of %{name}
Group:       Development

%description src-zip
Container for the source distribution of %{name}.
%endif

%prep
%setup -q -n %{short_name}-%{version}-src
%patch0 -p0
%patch1 -p1
#Not needed for EAP build
#%patch2 -p0
#%patch3 -p0 -b .s390x
#%patch4 -p0 -b .ppc
chmod 644 src/samples/*
%if %with native
# use the one from docbook instead of getting it from the net
catalogfile=`xmlcatalog /etc/xml/catalog "-//OASIS//DTD DocBook XML V4.1.2//EN"|sed -e s:"file\://"::`
sed -i -e s:"http\://www.oasis-open.org/docbook/xml/4.1.2/docbookx.dtd":$catalogfile: src/native/unix/man/jsvc.1.xml

pushd src/native/unix
###%%%%if 0%{?rhel} >= 6
#work with docbook-xsl (from docbook-maven on rhel 6)
unzip -q %{_javadir}/docbook-xsl-resources.zip
export XSL_DIR=$XSL_DIR:`pwd`/docbook/html:`pwd`/docbook/manpages:`pwd`/docbook/common
xmlto -x docbook/manpages/docbook.xsl man man/jsvc.1.xml
###%%%else
###xmlto man man/jsvc.1.xml
###%%%endif
popd
%endif
sed -i -e '2425s/powerpc/powerpc*/' src/native/unix/configure

zip -q -r ../%{name}-%{version}-src.zip *

%build
%if %with native
cd src/native/unix
%configure --with-java=%{java_home}
make %{?_smp_mflags}
%endif


%install
rm -rf $RPM_BUILD_ROOT
%if %with native
install -Dpm 0644 src/native/unix/jsvc.1 $RPM_BUILD_ROOT%{_mandir}/man1/jsvc.eap6.1
install -Dpm 755 src/native/unix/jsvc $RPM_BUILD_ROOT%{_bindir}/jsvc-eap6/jsvc
%endif

%if %with zip
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/jbossas-fordev
install -p -m 644 ../%{name}-%{version}-src.zip \
        $RPM_BUILD_ROOT%{_javadir}/jbossas-fordev/
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %with native
%files
%defattr(-,root,root,-)
%doc LICENSE*
%dir %{_bindir}/jsvc-eap6
%{_bindir}/jsvc-eap6/jsvc
%{_mandir}/man1/jsvc.eap6.1*
%endif

%if %with zip
%files src-zip
%defattr(-,root,root,-)
%{_javadir}/jbossas-fordev/*
%endif

%changelog
* Fri Jul 11 2014 Permaine Cheung <pcheung@redhat.com> - 1:1.0.15-6.redhat_2
- Rebuild

* Wed Apr 02 2014 Permaine Cheung <pcheung@redhat.com> - 1:1.0.15-5.redhat_2
- Rebuild

* Mon Mar 31 2014 Permaine Cheung <pcheung@redhat.com> - 1:1.0.15-4.redhat_2
- Rebuild

* Thu Mar 27 2014 Permaine Cheung <pcheung@redhat.com> - 1:1.0.15-3.redhat_2
- Specify BR :  java-devel >= 1.6.0, rebuild as ppc64 builders are enabled
- Add secondary patch (based on the fedora one) for ppc64 build

* Thu Jul 04 2013 Permaine Cheung <pcheung@redhat.com> - 1:1.0.15-2.redhat_2
- Fix R:libcap (BZ #971866)

* Thu Apr 11 2013 Permaine Cheung <pcheung@redhat.com> - 1:1.0.15-1.redhat_1
- 1.0.15

* Mon Mar 18 2013 Permaine Cheung <pcheung@redhat.com> - 1:1.0.14-1.redhat_1
- 1.0.14
- Remove the patch that has been incorporated in the new tag

* Thu Mar 07 2013 Permaine Cheung <pcheung@redhat.com> - 1:1.0.13-2.redhat_1
- Add R: apache-commons-daemon-eap6

* Wed Feb 13 2013 Permaine Cheung <pcheung@redhat.com> - 1:1.0.13-1.redhat_1
- 1.0.13

* Thu Jan 31 2013 Permaine Cheung <pcheung@redhat.com> - 1:1.0.12-1.redhat_1
- 1.0.12
- Merge ep-5-rhel-5 specific into this branch for ease of maintanence
- Add .redhat_1 to Release

* Thu Sep 06 2012 Permaine Cheung <pcheung@redhat.com> - 1:1.0.10-3
- Add missing man page
- Add zip subpackage

* Tue May 29 2012 Permaine Cheung <pcheung@redhat.com> - 1:1.0.10-2
- Keep name as jsvc

* Mon May 28 2012 Permaine Cheung <pcheung@redhat.com> - 1:1.0.10-1
- Rename to apache-commons-daemon-jsvc-eap6

* Tue Feb 28 2012 Permaine Cheung <pcheung@redhat.com> - 1:1.0.10-1
- Upgrade to 1.0.10

* Fri Nov 25 2011 Permaine Cheung <pcheung@redhat.com> - 1:1.0.8-1
- Upgrade to 1.0.8
- Remove patches that are already incorporated

* Mon Aug 15 2011 Permaine Cheung <pcheung@redhat.com> - 1:1.0.5-1.5.patch01
- Add fix for CVE-2011-2729

* Mon Mar 21 2011 Permaine Cheung <pcheung@redhat.com> - 1:1.0.5-1.4
- Fix BZ669259 (JBPAPP-6136)

* Wed Jan 26 2011 Permaine Cheung <pcheung@redhat.com> - 1:1.0.5-1.2
- Add patch for DAEMON-194

* Mon Jan 17 2011 Permaine Cheung <pcheung@redhat.com> - 1:1.0.5-1.1
- Upgrade to 1.0.5
- Split this from jakarta-commons-daemon into its own build
