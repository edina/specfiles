Name: mcollective-utilities-agent
Version: 1.0
Release: 1%{?dist}
Summary: MCollective Agent for interacting with misc utilities

Group: System Tools
License: Apache License, Version 2
Packager: Andrew Seales
Source: mc-util-%{version}.tar.gz
BuildArch: noarch

Requires: mcollective-common

%define plugindir %{_libexecdir}/mcollective/mcollective
%define agentdir %{plugindir}/agent
%define appdir %{plugindir}/application

%description
MCollective Agent for interacting with the utilities

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{plugindir}
install -d -m 755 %{buildroot}%{plugindir}/agent
install -d -m 755 %{buildroot}%{plugindir}/application
cp -a misc/agent/misc.rb %{buildroot}%{plugindir}/agent
cp -a misc/agent/misc.ddl %{buildroot}%{plugindir}/agent
cp -a misc/application/misc.rb %{buildroot}%{plugindir}/application


%files
%{plugindir}/agent/misc.rb
%{plugindir}/agent/misc.ddl
%{plugindir}/application/misc.rb

%changelog
* Fri Feb 6 2015 Andrew Seales <andrew.seales@ed.ac.uk>
  Initial release
