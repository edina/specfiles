# To Build: 
#
# sudo yum -y install rpmdevtools && rpmdev-setuptree
#
# wget http://apache.petsads.us/maven/maven-3/3.0.5/binaries/apache-maven-3.0.5-bin.tar.gz -O ~/rpmbuild/SOURCES/apache-maven-3.0.5-bin.tar.gz
# wget https://raw.github.com/nmilford/rpm-maven/master/maven.spec -O ~/rpmbuild/SPECS/maven.spec
# rpmbuild -bb ~/rpmbuild/SPECS/maven.spec

Name:           maven
Version:        3.0.5
Release:        2
Summary:        Apache Maven software project management and comprehension tool.
License:        Apache Software License
URL:            http://maven.apache.org/
Group:          Development/Build Tools
Source0:        apache-maven-%{version}-bin.tar.gz
Requires:       jdk
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Apache Maven is a software project management and comprehension tool. Based on the concept of a project object model (POM), Maven can manage a project's build, reporting and documentation from a central piece of information.

%prep
%setup -q -n apache-maven-%{version}

%build

install -d -m 755 %{buildroot}/opt/%{name}-%{version}
cp -R %{_builddir}/apache-maven-%{version}/* %{buildroot}/opt/%{name}-%{version}/

# Make it the default
install -d -m 755 %{buildroot}/etc/profile.d/
echo 'export M2_HOME=/opt/%{name}-%{version}' > %{buildroot}/etc/profile.d/%{name}.sh
# echo 'export PATH=/opt/%{name}/bin:$PATH' >> %{buildroot}/etc/profile.d/%{name}.sh

%install

install -d -m 755 %{buildroot}/usr/bin/
ln -sf /opt/%{name}-%{version}/bin/mvn %{buildroot}/usr/bin/mvn

%clean
rm -rf %{buildroot}

%post
echo
echo "You will need to exit your shell to have mvn in your default path."
echo

%files
/usr/bin/mvn
/opt/%{name}-%{version}/
/etc/profile.d/%{name}.sh

%changelog
* Wed Sep 25 2013 Andrew Seales <andrew.seales@ed.ac.uk> - 3.0.5-2
- Update to use the Oracle JDK
* Sun Jun 30 2013 Nathan Milford <nathan@milford.io> - 3.0.5-1
- First go at it.
