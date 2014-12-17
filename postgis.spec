%{!?javabuild:%define	javabuild 1}
%{!?utils:%define	utils 1}
%{!?gcj_support:%define	gcj_support 1}

%global majorversion 1.5

Summary:	Geographic Information Systems Extensions to PostgreSQL
Name:		postgis
Version:	1.5.3
Release:	1%{?dist}
License:	GPLv2+
Group:		Applications/Databases
Source0:	http://postgis.refractions.net/download/%{name}-%{version}.tar.gz
Source2:	http://www.postgis.org/download/%{name}-%{version}.pdf
Source4:	filter-requires-perl-Pg.sh
URL:		http://postgis.refractions.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	postgresql-devel >= 8.2, proj-devel, geos-devel >= 3.1.1, byacc, proj-devel, flex, sinjdoc, java, java-devel, ant
BuildRequires:	gtk2-devel, libxml2-devel
Requires:	postgresql >= 8.2, geos >= 3.1.1, proj

%description
PostGIS adds support for geographic objects to the PostgreSQL object-relational
database. In effect, PostGIS "spatially enables" the PostgreSQL server,
allowing it to be used as a backend spatial database for geographic information
systems (GIS), much like ESRI's SDE or Oracle's Spatial extension. PostGIS 
follows the OpenGIS "Simple Features Specification for SQL" and has been 
certified as compliant with the "Types and Functions" profile.

%package docs
Summary:	Extra documentation for PostGIS
Group:		Applications/Databases
%description docs
The postgis-docs package includes PDF documentation of PostGIS.

%if %javabuild
%package jdbc
Summary:	The JDBC driver for PostGIS
Group:		Applications/Databases
License:	LGPLv2+
Requires:	%{name} = %{version}-%{release}, postgresql-jdbc
BuildRequires:	ant >= 0:1.6.2, junit >= 0:3.7, postgresql-jdbc

%if %{gcj_support}
BuildRequires:		gcc-java
BuildRequires:		java-1.5.0-gcj-devel
Requires(post):		%{_bindir}/rebuild-gcj-db
Requires(postun):	%{_bindir}/rebuild-gcj-db
%endif

%description jdbc
The postgis-jdbc package provides the essential jdbc driver for PostGIS.
%endif

%if %utils
%package utils
Summary:	The utils for PostGIS
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}, perl-DBD-Pg

%description utils
The postgis-utils package provides the utilities for PostGIS.
%endif

%define __perl_requires %{SOURCE4}

%prep
%setup -q -n %{name}-%{version}
# Copy .pdf file to top directory before installing.
cp -p %{SOURCE2} .

%build
%configure --with-gui
#make %{?_smp_mflags} LPATH=`pg_config --pkglibdir` shlib="%{name}.so"
make LPATH=`pg_config --pkglibdir` shlib="%{name}.so"

%if %javabuild
export BUILDXML_DIR=%{_builddir}/%{name}-%{version}/java/jdbc
JDBC_VERSION_RPM=`rpm -ql postgresql-jdbc| grep 'jdbc2.jar$'|awk -F '/' '{print $5}'`
sed 's/postgresql.jar/'${JDBC_VERSION_RPM}'/g' $BUILDXML_DIR/build.xml > $BUILDXML_DIR/build.xml.new
mv -f $BUILDXML_DIR/build.xml.new $BUILDXML_DIR/build.xml
pushd java/jdbc
ant
popd
%endif

%if %utils
 make -C utils
%endif

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
install -d %{buildroot}%{_libdir}/pgsql/
install -d  %{buildroot}%{_datadir}/pgsql/contrib/
install -m 644 *.sql %{buildroot}%{_datadir}/pgsql/contrib/
install -m 755 loader/shp2pgsql loader/shp2pgsql-gui %{buildroot}%{_bindir}/
rm -f  %{buildroot}%{_datadir}/*.sql

if [ "%{_libdir}" = "/usr/lib64" ] ; then
	mv %{buildroot}%{_datadir}/pgsql/contrib/%{name}-%{majorversion}/postgis.sql %{buildroot}%{_datadir}/pgsql/contrib/postgis-64.sql
	mv %{buildroot}%{_datadir}/pgsql/contrib/%{name}-%{majorversion}/postgis_upgrade_13_to_15.sql %{buildroot}%{_datadir}/pgsql/contrib/%{name}-%{majorversion}/postgis_upgrade_13_to_15-64.sql
	mv %{buildroot}%{_datadir}/pgsql/contrib/%{name}-%{majorversion}/postgis_upgrade_14_to_15.sql %{buildroot}%{_datadir}/pgsql/contrib/%{name}-%{majorversion}/postgis_upgrade_14_to_15-64.sql
fi

%if %javabuild
install -d %{buildroot}%{_javadir}
install -m 755 java/jdbc/%{name}-%{version}.jar %{buildroot}%{_javadir}
%if %{gcj_support}
aot-compile-rpm
%endif
strip %{buildroot}/%{_libdir}/gcj/%{name}/*.jar.so
%endif

%if %utils
install -d %{buildroot}%{_datadir}/%{name}
install -m 755 utils/*.pl %{buildroot}%{_datadir}/%{name}
%endif

%clean
rm -rf %{buildroot}

%if %javabuild
%if %gcj_support
%post -p %{_bindir}/rebuild-gcj-db
%postun -p %{_bindir}/rebuild-gcj-db
%endif
%endif

%files
%defattr(-,root,root)
%doc COPYING CREDITS NEWS TODO README.%{name} doc/html loader/README.* doc/%{name}.xml doc/ZMSgeoms.txt 
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/pgsql/postgis-*.so
%{_datadir}/pgsql/contrib/*.sql
%{_datadir}/pgsql/contrib/%{name}-%{majorversion}/*.sql

%if %javabuild
%files jdbc
%defattr(-,root,root)
%doc java/jdbc/COPYING_LGPL java/jdbc/README
%attr(755,root,root) %{_javadir}/%{name}-%{version}.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/*.jar.so
%{_libdir}/gcj/%{name}/*.jar.db
%endif
%endif

%if %utils
%files utils
%defattr(755,root,root)
%doc utils/README
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/test_estimation.pl
%{_datadir}/%{name}/profile_intersects.pl
%{_datadir}/%{name}/test_joinestimation.pl
%{_datadir}/%{name}/create_undef.pl
%{_datadir}/%{name}/%{name}_proc_upgrade.pl
%{_datadir}/%{name}/%{name}_restore.pl
%{_datadir}/%{name}/new_postgis_restore.pl
%{_datadir}/%{name}/read_scripts_version.pl
%{_datadir}/%{name}/test_geography_estimation.pl
%{_datadir}/%{name}/test_geography_joinestimation.pl
%endif

%files docs
%defattr(-,root,root)
%doc postgis*.pdf

%changelog
* Tue Oct 4 2011 Devrim GÜNDÜZ <devrim@gunduz.org> - 1.5.3-1
- Update to 1.5.3

* Thu Jul 1 2010 Devrim GÜNDÜZ <devrim@gunduz.org> - 1.5.1-1
- Initial packaging for EL-6.
