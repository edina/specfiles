# used for CVS snapshots:
%define CVSDATE %{nil}
%if %{?WITH_SELINUX:0}%{!?WITH_SELINUX:1}
%define WITH_SELINUX 1
%endif
%define desktop_file 1
%if %{desktop_file}
%define desktop_file_utils_version 0.2.93
%endif

%define withnetbeans 1

%define withvimspell 0
%define withhunspell 0
%define withruby 1

%define baseversion 7.4
#used for pre-releases:
%define beta %{nil}
%define vimdir vim74%{?beta}
%define patchlevel 052

Summary: The VIM editor
URL:     http://www.vim.org/
Name: vim
Version: %{baseversion}.%{beta}%{patchlevel}
Release: 1.1%{?dist}
License: Vim and GPLv2+ and BSD and LGPLv2+ and Open Publication
Group: Applications/Editors
Source0: ftp://ftp.vim.org/pub/vim/unix/vim-%{baseversion}%{?beta}%{?CVSDATE}.tar.bz2
Source1: gvim.desktop
Source2: vimrc
#Source3: ftp://ftp.vim.org/pub/vim/patches/README.patches
Source4: gvim16.png
Source5: gvim32.png
Source6: gvim48.png
Source7: gvim64.png
Source8: Changelog.rpm
Source9: vi_help.txt
%if %{withvimspell}
Source10: vim-spell-files.tar.bz2
%endif
Source11: spec-template
Source12: http://www.cvjb.de/comp/vim/forth.vim

# remove this for the next major version, CVE fixes:
Source13: ftp://ftp.vim.org/vol/2/vim/runtime/plugin/netrwPlugin.vim
Source14: ftp://ftp.vim.org/vol/2/vim/runtime/plugin/gzip.vim
Source15: ftp://ftp.vim.org/vol/2/vim/runtime/filetype.vim
Source16: ftp://ftp.vim.org/vol/2/vim/runtime/autoload/zip.vim
Source17: ftp://ftp.vim.org/vol/2/vim/runtime/autoload/tar.vim
Source18: ftp://ftp.vim.org/vol/2/vim/runtime/autoload/netrwFileHandlers.vim
Source19: ftp://ftp.vim.org/vol/2/vim/runtime/autoload/netrw.vim
Source20: ftp://ftp.vim.org/vol/2/vim/runtime/autoload/netrwSettings.vim

Patch2002: vim-7.0-fixkeys.patch
Patch2003: vim-6.2-specsyntax.patch
%if %{withhunspell}
Patch2011: vim-7.0-hunspell.patch
BuildRequires: hunspell-devel
%endif
# Patches 001 < 999 are patches from the base maintainer.
# If you're as lazy as me, generate the list using
# for i in `seq 1 14`; do printf "Patch%03d: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.%03d\n" $i $i; done
Patch001: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.001
Patch002: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.002
Patch003: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.003
Patch004: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.004
Patch005: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.005
Patch006: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.006
Patch007: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.007
Patch008: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.008
Patch009: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.009
Patch010: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.010
Patch011: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.011
Patch012: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.012
Patch013: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.013
Patch014: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.014
Patch015: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.015
Patch016: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.016
Patch017: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.017
Patch018: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.018
Patch019: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.019
Patch020: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.020
Patch021: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.021
Patch022: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.022
Patch023: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.023
Patch024: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.024
Patch025: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.025
Patch026: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.026
Patch027: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.027
Patch028: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.028
Patch029: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.029
Patch030: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.030
Patch031: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.031
Patch032: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.032
Patch033: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.033
Patch034: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.034
Patch035: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.035
Patch036: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.036
Patch037: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.037
Patch038: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.038
Patch039: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.039
Patch040: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.040
Patch041: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.041
Patch042: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.042
Patch043: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.043
Patch044: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.044
Patch045: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.045
Patch046: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.046
Patch047: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.047
Patch048: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.048
Patch049: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.049
Patch050: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.050
Patch051: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.051
Patch052: ftp://ftp.vim.org/pub/vim/patches/7.4/7.4.052

Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: python-devel ncurses-devel gettext perl-devel
BuildRequires: perl(ExtUtils::Embed)
BuildRequires: libacl-devel gpm-devel autoconf
BuildRequires: libX11-devel
%if %{WITH_SELINUX}
BuildRequires: libselinux-devel
%endif
%if %{desktop_file}
# for /usr/bin/desktop-file-install
Requires: desktop-file-utils
BuildRequires: desktop-file-utils >= %{desktop_file_utils_version}
%endif
Epoch: 2

%description
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more.

%package common
Summary: The common files needed by any version of the VIM editor
Group: Applications/Editors
Conflicts: man-pages-fr < 0.9.7-14
Conflicts: man-pages-it < 0.3.0-17
Conflicts: man-pages-pl < 0.24-2

%description common
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more.  The
vim-common package contains files which every VIM binary will need in
order to run.

If you are installing vim-enhanced or vim-X11, you'll also need
to install the vim-common package.

%package spell
Summary: The dictionaries for spell checking. This package is optional
Group: Applications/Editors
Requires: vim-common = %{epoch}:%{version}-%{release}

%description spell
This subpackage contains dictionaries for vim spell checking in
many different languages.

%package minimal
Summary: A minimal version of the VIM editor
Group: Applications/Editors
Provides: vi = %{version}-%{release}

%description minimal
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more. The
vim-minimal package includes a minimal version of VIM, which is
installed into /bin/vi for use when only the root partition is
present. NOTE: The online help is only available when the vim-common
package is installed.

%package enhanced
Summary: A version of the VIM editor which includes recent enhancements
Group: Applications/Editors
Requires: vim-common = %{epoch}:%{version}-%{release} which
Provides: vim = %{version}-%{release}
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description enhanced
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more.  The
vim-enhanced package contains a version of VIM with extra, recently
introduced features like Python and Perl interpreters.

Install the vim-enhanced package if you'd like to use a version of the
VIM editor which includes recently added enhancements like
interpreters for the Python and Perl scripting languages.  You'll also
need to install the vim-common package.

%package X11
Summary: The VIM version of the vi editor for the X Window System
Group: Applications/Editors
Requires: vim-common = %{epoch}:%{version}-%{release} libattr >= 2.4 gtk2 >= 2.6
Provides: gvim = %{version}-%{release}
BuildRequires: gtk2-devel libSM-devel libXt-devel libXpm-devel
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires: hicolor-icon-theme

%description X11
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and
more. VIM-X11 is a version of the VIM editor which will run within the
X Window System.  If you install this package, you can run VIM as an X
application with a full GUI interface and mouse support.

Install the vim-X11 package if you'd like to try out a version of vi
with graphics and mouse capabilities.  You'll also need to install the
vim-common package.

%prep
%setup -q -b 0 -n %{vimdir}
# fix rogue dependencies from sample code
chmod -x runtime/tools/mve.awk
%patch2002 -p1
%patch2003 -p1
%if %{withhunspell}
%patch2011 -p1
%endif
perl -pi -e "s,bin/nawk,bin/awk,g" runtime/tools/mve.awk

# Base patches...
# for i in `seq 1 14`; do printf "%%patch%03d -p0 \n" $i; done
%patch001 -p0
%patch002 -p0
%patch003 -p0
%patch004 -p0
%patch005 -p0
%patch006 -p0
%patch007 -p0
%patch008 -p0
%patch009 -p0
%patch010 -p0
%patch011 -p0
%patch012 -p0
%patch013 -p0
%patch014 -p0
%patch015 -p0
%patch016 -p0
%patch017 -p0
%patch018 -p0
%patch019 -p0
%patch020 -p0
%patch021 -p0
%patch022 -p0
%patch023 -p0
%patch024 -p0
%patch025 -p0
%patch026 -p0
%patch027 -p0
%patch028 -p0
%patch029 -p0
%patch030 -p0
%patch031 -p0
%patch032 -p0
%patch033 -p0
%patch034 -p0
%patch035 -p0
%patch036 -p0
%patch037 -p0
%patch038 -p0
%patch039 -p0
%patch040 -p0
%patch041 -p0
%patch042 -p0
%patch043 -p0
%patch044 -p0
%patch045 -p0
%patch046 -p0
%patch047 -p0
%patch048 -p0
%patch049 -p0
%patch050 -p0
%patch051 -p0
%patch052 -p0

# install spell files
%if %{withvimspell}
%{__tar} xjf %{SOURCE10}
%endif

cp -f %{SOURCE12} runtime/syntax/forth.vim
cp -f %{SOURCE13} runtime/plugin/netrwPlugin.vim
cp -f %{SOURCE14} runtime/plugin/gzip.vim
cp -f %{SOURCE15} runtime/plugin/filetype.vim
cp -f %{SOURCE16} runtime/autoload/zip.vim
cp -f %{SOURCE17} runtime/autoload/tar.vim
cp -f %{SOURCE18} runtime/autoload/netrwFileHandlers.vim
cp -f %{SOURCE19} runtime/autoload/netrw.vim
cp -f %{SOURCE20} runtime/autoload/netrwSettings.vim


%build
cd src
autoconf

export CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -D_FORTIFY_SOURCE=2"
export CXXFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -D_FORTIFY_SOURCE=2"

%configure --with-features=huge --enable-pythoninterp --enable-perlinterp \
  --disable-tclinterp --with-x=yes \
  --enable-xim --enable-multibyte \
  --with-tlib=tinfo \
  --enable-gtk2-check --enable-gui=gtk2 \
  --with-compiledby="<bugzilla@redhat.com>" --enable-cscope \
  --with-modified-by="<bugzilla@redhat.com>" \
%if "%{withnetbeans}" == "1"
  --enable-netbeans \
%else
  --disable-netbeans \
%endif
%if %{WITH_SELINUX}
  --enable-selinux \
%else
  --disable-selinux \
%endif
%if "%{withruby}" == "1"
  --enable-rubyinterp \
%else
  --disable-rubyinterp \
%endif

make %{?_smp_mflags}
cp vim gvim
make clean

%configure --prefix=%{_prefix} --with-features=huge --enable-pythoninterp \
 --enable-perlinterp --disable-tclinterp --with-x=no \
 --enable-gui=no --exec-prefix=%{_prefix} --enable-multibyte \
 --enable-cscope --with-modified-by="<bugzilla@redhat.com>" \
 --with-tlib=tinfo --with-x \
 --with-compiledby="<bugzilla@redhat.com>" \
%if "%{withnetbeans}" == "1"
  --enable-netbeans \
%else
  --disable-netbeans \
%endif
%if %{WITH_SELINUX}
  --enable-selinux \
%else
  --disable-selinux \
%endif
%if "%{withruby}" == "1"
  --enable-rubyinterp \
%else
  --disable-rubyinterp \
%endif

make %{?_smp_mflags}
cp vim enhanced-vim
make clean

perl -pi -e "s/help.txt/vi_help.txt/"  os_unix.h ex_cmds.c
perl -pi -e "s/\/etc\/vimrc/\/etc\/virc/"  os_unix.h
%configure --prefix=%{_prefix} --with-features=small --with-x=no \
  --enable-multibyte \
  --disable-netbeans \
%if %{WITH_SELINUX}
  --enable-selinux \
%else
  --disable-selinux \
%endif
  --disable-pythoninterp --disable-perlinterp --disable-tclinterp \
  --with-tlib=tinfo --enable-gui=no --disable-gpm --exec-prefix=/ \
  --with-compiledby="<bugzilla@redhat.com>" \
  --with-modified-by="<bugzilla@redhat.com>"

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/bin
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}/vimfiles/{after,autoload,colors,compiler,doc,ftdetect,ftplugin,indent,keymap,lang,plugin,print,spell,syntax,tutor}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}/vimfiles/after/{autoload,colors,compiler,doc,ftdetect,ftplugin,indent,keymap,lang,plugin,print,spell,syntax,tutor}
cp -f %{SOURCE8} .
cp -f %{SOURCE11} $RPM_BUILD_ROOT/%{_datadir}/%{name}/vimfiles/template.spec
cp runtime/doc/uganda.txt LICENSE
# Those aren't Linux info files but some binary files for Amiga:
rm -f README*.info


cd src
make install DESTDIR=$RPM_BUILD_ROOT BINDIR=/bin
make installgtutorbin  DESTDIR=$RPM_BUILD_ROOT BINDIR=/bin
mv $RPM_BUILD_ROOT/bin/xxd $RPM_BUILD_ROOT/%{_bindir}/xxd
mv $RPM_BUILD_ROOT/bin/gvimtutor $RPM_BUILD_ROOT/%{_bindir}/gvimtutor
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/{16x16,32x32,48x48,64x64}/apps
install -m755 gvim $RPM_BUILD_ROOT/%{_bindir}/gvim
install -p -m644 %{SOURCE4} \
   $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/gvim.png
install -p -m644 %{SOURCE5} \
   $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/gvim.png
install -p -m644 %{SOURCE6} \
   $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/gvim.png
install -p -m644 %{SOURCE7} \
   $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/gvim.png
install -m755 enhanced-vim $RPM_BUILD_ROOT/%{_bindir}/vim

( cd $RPM_BUILD_ROOT
  mv ./bin/vimtutor ./%{_bindir}/vimtutor
  mv ./bin/vim ./bin/vi
  rm -f ./bin/rvim
  ln -sf vi ./bin/ex
  ln -sf vi ./bin/rvi
  ln -sf vi ./bin/rview
  ln -sf vi ./bin/view
  ln -sf vim ./%{_bindir}/ex
  ln -sf vim ./%{_bindir}/rvim
  ln -sf vim ./%{_bindir}/vimdiff
  perl -pi -e "s,$RPM_BUILD_ROOT,," .%{_mandir}/man1/vim.1 .%{_mandir}/man1/vimtutor.1
  rm -f .%{_mandir}/man1/rvim.1
  ln -sf vim.1.gz .%{_mandir}/man1/vi.1.gz
  ln -sf vim.1.gz .%{_mandir}/man1/rvi.1.gz
  ln -sf vim.1.gz .%{_mandir}/man1/vimdiff.1.gz
  ln -sf gvim ./%{_bindir}/gview
  ln -sf gvim ./%{_bindir}/gex
  ln -sf gvim ./%{_bindir}/evim
  ln -sf gvim ./%{_bindir}/gvimdiff
  ln -sf gvim ./%{_bindir}/vimx
  %if "%{desktop_file}" == "1"
    mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications
    desktop-file-install --vendor fedora \
        --dir $RPM_BUILD_ROOT/%{_datadir}/applications \
        %{SOURCE1}
        # --add-category "Development;TextEditor;X-Red-Hat-Base"
  %else
    mkdir -p ./%{_sysconfdir}/X11/applnk/Applications
    cp %{SOURCE1} ./%{_sysconfdir}/X11/applnk/Applications/gvim.desktop
  %endif
  # ja_JP.ujis is obsolete, ja_JP.eucJP is recommended.
  ( cd ./%{_datadir}/%{name}/%{vimdir}/lang; \
    ln -sf menu_ja_jp.ujis.vim menu_ja_jp.eucjp.vim )
)

pushd $RPM_BUILD_ROOT/%{_datadir}/%{name}/%{vimdir}/tutor
mkdir conv
   iconv -f CP1252 -t UTF8 tutor.ca > conv/tutor.ca
   iconv -f CP1252 -t UTF8 tutor.it > conv/tutor.it
   #iconv -f CP1253 -t UTF8 tutor.gr > conv/tutor.gr
   iconv -f CP1252 -t UTF8 tutor.fr > conv/tutor.fr
   iconv -f CP1252 -t UTF8 tutor.es > conv/tutor.es
   iconv -f CP1252 -t UTF8 tutor.de > conv/tutor.de
   #iconv -f CP737 -t UTF8 tutor.gr.cp737 > conv/tutor.gr.cp737
   #iconv -f EUC-JP -t UTF8 tutor.ja.euc > conv/tutor.ja.euc
   #iconv -f SJIS -t UTF8 tutor.ja.sjis > conv/tutor.ja.sjis
   iconv -f UTF8 -t UTF8 tutor.ja.utf-8 > conv/tutor.ja.utf-8
   iconv -f UTF8 -t UTF8 tutor.ko.utf-8 > conv/tutor.ko.utf-8
   iconv -f CP1252 -t UTF8 tutor.no > conv/tutor.no
   iconv -f ISO-8859-2 -t UTF8 tutor.pl > conv/tutor.pl
   iconv -f ISO-8859-2 -t UTF8 tutor.sk > conv/tutor.sk
   iconv -f KOI8R -t UTF8 tutor.ru > conv/tutor.ru
   iconv -f CP1252 -t UTF8 tutor.sv > conv/tutor.sv
   mv -f tutor.ja.euc tutor.ja.sjis tutor.ko.euc tutor.pl.cp1250 tutor.zh.big5 tutor.ru.cp1251 tutor.zh.euc conv/
   rm -f tutor.ca tutor.de tutor.es tutor.fr tutor.gr tutor.it tutor.ja.utf-8 tutor.ko.utf-8 tutor.no tutor.pl tutor.sk tutor.ru tutor.sv
mv -f conv/* .
rmdir conv
popd

# Dependency cleanups
chmod 644 $RPM_BUILD_ROOT/%{_datadir}/%{name}/%{vimdir}/doc/vim2html.pl \
 $RPM_BUILD_ROOT/%{_datadir}/%{name}/%{vimdir}/tools/*.pl \
 $RPM_BUILD_ROOT/%{_datadir}/%{name}/%{vimdir}/tools/vim132
chmod 644 ../runtime/doc/vim2html.pl

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d
cat >$RPM_BUILD_ROOT/%{_sysconfdir}/profile.d/vim.sh <<EOF
if [ -n "\$BASH_VERSION" -o -n "\$KSH_VERSION" -o -n "\$ZSH_VERSION" ]; then
  [ -x %{_bindir}/id ] || return
  ID=\`%{_bindir}/id -u\`
  [ -n "\$ID" -a "\$ID" -le 200 ] && return
  # for bash and zsh, only if no alias is already set
  alias vi >/dev/null 2>&1 || alias vi=vim
fi
EOF
cat >$RPM_BUILD_ROOT/%{_sysconfdir}/profile.d/vim.csh <<EOF
if ( -x %{_bindir}/id ) then
  if ( "\`%{_bindir}/id -u\`" > 200 ) then
    alias vi vim
  endif
endif
EOF
chmod 0644 $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d/*
install -p -m644 %{SOURCE2} $RPM_BUILD_ROOT/%{_sysconfdir}/vimrc
install -p -m644 %{SOURCE2} $RPM_BUILD_ROOT/%{_sysconfdir}/virc
(cd $RPM_BUILD_ROOT/%{_datadir}/%{name}/%{vimdir}/doc;
 gzip -9 -n *.txt
 gzip -d help.txt.gz version7.txt.gz sponsor.txt.gz
 cp %{SOURCE9} .
 cat tags | sed -e 's/\t\(.*.txt\)\t/\t\1.gz\t/;s/\thelp.txt.gz\t/\thelp.txt\t/;s/\tversion7.txt.gz\t/\tversion7.txt\t/;s/\tsponsor.txt.gz\t/\tsponsor.txt\t/' > tags.new; mv -f tags.new tags
cat >> tags << EOF
vi_help.txt	vi_help.txt	/*vi_help.txt*
vi-author.txt	vi_help.txt	/*vi-author*
vi-Bram.txt	vi_help.txt	/*vi-Bram*
vi-Moolenaar.txt	vi_help.txt	/*vi-Moolenaar*
vi-credits.txt	vi_help.txt	/*vi-credits*
EOF
 )
(cd ../runtime; rm -rf doc; ln -svf ../../vim/%{vimdir}/doc docs;) 
rm -f $RPM_BUILD_ROOT/%{_datadir}/vim/%{vimdir}/macros/maze/maze*.c
rm -rf $RPM_BUILD_ROOT/%{_datadir}/vim/%{vimdir}/tools
rm -rf $RPM_BUILD_ROOT/%{_datadir}/vim/%{vimdir}/doc/vim2html.pl
rm -f $RPM_BUILD_ROOT/%{_datadir}/vim/%{vimdir}/tutor/tutor.gr.utf-8~
( cd $RPM_BUILD_ROOT/%{_mandir}
  for i in `find ??/ -type f`; do
    bi=`basename $i`
    iconv -f latin1 -t UTF8 $i > $RPM_BUILD_ROOT/$bi
    mv -f $RPM_BUILD_ROOT/$bi $i
  done
)

# Remove not UTF-8 manpages
for i in pl.ISO8859-2 it.ISO8859-1 ru.KOI8-R fr.ISO8859-1; do
  rm -rf $RPM_BUILD_ROOT/%{_mandir}/$i
done

# use common man1/ru directory
mv $RPM_BUILD_ROOT/%{_mandir}/ru.UTF-8 $RPM_BUILD_ROOT/%{_mandir}/ru

# Remove duplicate man pages
for i in fr.UTF-8 it.UTF-8 pl.UTF-8; do
  rm -rf $RPM_BUILD_ROOT/%{_mandir}/$i
done

for i in rvim.1 gvim.1 gvimdiff.1; do 
  echo ".so man1/vim.1" > $RPM_BUILD_ROOT/%{_mandir}/man1/$i
done

%post X11
touch --no-create %{_datadir}/icons/hicolor
if [ -x /%{_bindir}/gtk-update-icon-cache ]; then
  gtk-update-icon-cache --ignore-theme-index -q %{_datadir}/icons/hicolor
fi
update-desktop-database &> /dev/null ||:

%postun X11
touch --no-create %{_datadir}/icons/hicolor
if [ -x /%{_bindir}/gtk-update-icon-cache ]; then
  gtk-update-icon-cache --ignore-theme-index -q %{_datadir}/icons/hicolor
fi
update-desktop-database &> /dev/null ||:

%clean
rm -rf $RPM_BUILD_ROOT

%files common
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/vimrc
%doc README* LICENSE
%doc runtime/docs
%doc Changelog.rpm
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/%{vimdir}
%dir %{_datadir}/%{name}/vimfiles
%dir %{_datadir}/%{name}/vimfiles/after
%dir %{_datadir}/%{name}/vimfiles/after/*
%dir %{_datadir}/%{name}/vimfiles/autoload
%dir %{_datadir}/%{name}/vimfiles/colors
%dir %{_datadir}/%{name}/vimfiles/compiler
%dir %{_datadir}/%{name}/vimfiles/doc
%dir %{_datadir}/%{name}/vimfiles/ftdetect
%dir %{_datadir}/%{name}/vimfiles/ftplugin
%dir %{_datadir}/%{name}/vimfiles/indent
%dir %{_datadir}/%{name}/vimfiles/keymap
%dir %{_datadir}/%{name}/vimfiles/lang
%dir %{_datadir}/%{name}/vimfiles/plugin
%dir %{_datadir}/%{name}/vimfiles/print
%dir %{_datadir}/%{name}/vimfiles/spell
%dir %{_datadir}/%{name}/vimfiles/syntax
%dir %{_datadir}/%{name}/vimfiles/tutor
%{_datadir}/%{name}/vimfiles/template.spec
%{_datadir}/%{name}/%{vimdir}/autoload
%{_datadir}/%{name}/%{vimdir}/colors
%{_datadir}/%{name}/%{vimdir}/compiler
%{_datadir}/%{name}/%{vimdir}/doc
%{_datadir}/%{name}/%{vimdir}/*.vim
%{_datadir}/%{name}/%{vimdir}/ftplugin
%{_datadir}/%{name}/%{vimdir}/indent
%{_datadir}/%{name}/%{vimdir}/keymap
%{_datadir}/%{name}/%{vimdir}/lang/*.vim
%{_datadir}/%{name}/%{vimdir}/lang/*.txt
%dir %{_datadir}/%{name}/%{vimdir}/lang
%{_datadir}/%{name}/%{vimdir}/macros
%{_datadir}/%{name}/%{vimdir}/plugin
%{_datadir}/%{name}/%{vimdir}/print
%{_datadir}/%{name}/%{vimdir}/syntax
%{_datadir}/%{name}/%{vimdir}/tutor
%if ! %{withvimspell}
%{_datadir}/%{name}/%{vimdir}/spell
%endif
%lang(af) %{_datadir}/%{name}/%{vimdir}/lang/af
%lang(ca) %{_datadir}/%{name}/%{vimdir}/lang/ca
%lang(cs) %{_datadir}/%{name}/%{vimdir}/lang/cs
%lang(cs.CP1250) %{_datadir}/%{name}/%{vimdir}/lang/cs.cp1250
%lang(de) %{_datadir}/%{name}/%{vimdir}/lang/de
%lang(en_GB) %{_datadir}/%{name}/%{vimdir}/lang/en_GB
%lang(eo) %{_datadir}/%{name}/%{vimdir}/lang/eo
%lang(es) %{_datadir}/%{name}/%{vimdir}/lang/es
%lang(fi) %{_datadir}/%{name}/%{vimdir}/lang/fi
%lang(fr) %{_datadir}/%{name}/%{vimdir}/lang/fr
%lang(ga) %{_datadir}/%{name}/%{vimdir}/lang/ga
%lang(it) %{_datadir}/%{name}/%{vimdir}/lang/it
%lang(ja) %{_datadir}/%{name}/%{vimdir}/lang/ja
%lang(ja.EUC-JP) %{_datadir}/%{name}/%{vimdir}/lang/ja.euc-jp
%lang(ja.SJIS) %{_datadir}/%{name}/%{vimdir}/lang/ja.sjis
%lang(ko) %{_datadir}/%{name}/%{vimdir}/lang/ko
%lang(ko.UTF-8) %{_datadir}/%{name}/%{vimdir}/lang/ko.UTF-8
%lang(nb) %{_datadir}/%{name}/%{vimdir}/lang/nb
%lang(nl) %{_datadir}/%{name}/%{vimdir}/lang/nl
%lang(no) %{_datadir}/%{name}/%{vimdir}/lang/no
%lang(pl) %{_datadir}/%{name}/%{vimdir}/lang/pl
%lang(pl.CP1250) %{_datadir}/%{name}/%{vimdir}/lang/pl.cp1250
%lang(pl.UTF-8) %{_datadir}/%{name}/%{vimdir}/lang/pl.UTF-8
%lang(pt_BR) %{_datadir}/%{name}/%{vimdir}/lang/pt_BR
%lang(ru) %{_datadir}/%{name}/%{vimdir}/lang/ru
%lang(ru.CP1251) %{_datadir}/%{name}/%{vimdir}/lang/ru.cp1251
%lang(sk) %{_datadir}/%{name}/%{vimdir}/lang/sk
%lang(sk.CP1250) %{_datadir}/%{name}/%{vimdir}/lang/sk.cp1250
%lang(sv) %{_datadir}/%{name}/%{vimdir}/lang/sv
%lang(uk) %{_datadir}/%{name}/%{vimdir}/lang/uk
%lang(uk.CP1251) %{_datadir}/%{name}/%{vimdir}/lang/uk.cp1251
%lang(vi) %{_datadir}/%{name}/%{vimdir}/lang/vi
%lang(zh_CN) %{_datadir}/%{name}/%{vimdir}/lang/zh_CN
%lang(zh_CN.CP936) %{_datadir}/%{name}/%{vimdir}/lang/zh_CN.cp936
%lang(zh_CN.UTF-8) %{_datadir}/%{name}/%{vimdir}/lang/zh_CN.UTF-8
%lang(zh_TW) %{_datadir}/%{name}/%{vimdir}/lang/zh_TW
%lang(zh_TW.UTF-8) %{_datadir}/%{name}/%{vimdir}/lang/zh_TW.UTF-8
/%{_bindir}/xxd
%{_mandir}/man1/vim.*
%{_mandir}/man1/ex.*
%{_mandir}/man1/vi.*
%{_mandir}/man1/view.*
%{_mandir}/man1/rvi.*
%{_mandir}/man1/rview.*
%{_mandir}/man1/xxd.*
%lang(fr) %{_mandir}/fr/man1/*
%lang(it) %{_mandir}/it/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%lang(ru) %{_mandir}/ru/man1/*

%if %{withvimspell}
%files spell
%defattr(-,root,root)
%dir %{_datadir}/%{name}/%{vimdir}/spell
%{_datadir}/%{name}/vim70/spell/cleanadd.vim
%lang(af) %{_datadir}/%{name}/%{vimdir}/spell/af.*
%lang(am) %{_datadir}/%{name}/%{vimdir}/spell/am.*
%lang(bg) %{_datadir}/%{name}/%{vimdir}/spell/bg.*
%lang(ca) %{_datadir}/%{name}/%{vimdir}/spell/ca.*
%lang(cs) %{_datadir}/%{name}/%{vimdir}/spell/cs.*
%lang(cy) %{_datadir}/%{name}/%{vimdir}/spell/cy.*
%lang(da) %{_datadir}/%{name}/%{vimdir}/spell/da.*
%lang(de) %{_datadir}/%{name}/%{vimdir}/spell/de.*
%lang(el) %{_datadir}/%{name}/%{vimdir}/spell/el.*
%lang(en) %{_datadir}/%{name}/%{vimdir}/spell/en.*
%lang(eo) %{_datadir}/%{name}/%{vimdir}/spell/eo.*
%lang(es) %{_datadir}/%{name}/%{vimdir}/spell/es.*
%lang(fo) %{_datadir}/%{name}/%{vimdir}/spell/fo.*
%lang(fr) %{_datadir}/%{name}/%{vimdir}/spell/fr.*
%lang(ga) %{_datadir}/%{name}/%{vimdir}/spell/ga.*
%lang(gd) %{_datadir}/%{name}/%{vimdir}/spell/gd.*
%lang(gl) %{_datadir}/%{name}/%{vimdir}/spell/gl.*
%lang(he) %{_datadir}/%{name}/%{vimdir}/spell/he.*
%lang(hr) %{_datadir}/%{name}/%{vimdir}/spell/hr.*
%lang(hu) %{_datadir}/%{name}/%{vimdir}/spell/hu.*
%lang(id) %{_datadir}/%{name}/%{vimdir}/spell/id.*
%lang(it) %{_datadir}/%{name}/%{vimdir}/spell/it.*
%lang(ku) %{_datadir}/%{name}/%{vimdir}/spell/ku.*
%lang(la) %{_datadir}/%{name}/%{vimdir}/spell/la.*
%lang(lt) %{_datadir}/%{name}/%{vimdir}/spell/lt.*
%lang(lv) %{_datadir}/%{name}/%{vimdir}/spell/lv.*
%lang(mg) %{_datadir}/%{name}/%{vimdir}/spell/mg.*
%lang(mi) %{_datadir}/%{name}/%{vimdir}/spell/mi.*
%lang(ms) %{_datadir}/%{name}/%{vimdir}/spell/ms.*
%lang(nb) %{_datadir}/%{name}/%{vimdir}/spell/nb.*
%lang(nl) %{_datadir}/%{name}/%{vimdir}/spell/nl.*
%lang(nn) %{_datadir}/%{name}/%{vimdir}/spell/nn.*
%lang(ny) %{_datadir}/%{name}/%{vimdir}/spell/ny.*
%lang(pl) %{_datadir}/%{name}/%{vimdir}/spell/pl.*
%lang(pt) %{_datadir}/%{name}/%{vimdir}/spell/pt.*
%lang(ro) %{_datadir}/%{name}/%{vimdir}/spell/ro.*
%lang(ru) %{_datadir}/%{name}/%{vimdir}/spell/ru.*
%lang(rw) %{_datadir}/%{name}/%{vimdir}/spell/rw.*
%lang(sk) %{_datadir}/%{name}/%{vimdir}/spell/sk.*
%lang(sl) %{_datadir}/%{name}/%{vimdir}/spell/sl.*
%lang(sv) %{_datadir}/%{name}/%{vimdir}/spell/sv.*
%lang(sw) %{_datadir}/%{name}/%{vimdir}/spell/sw.*
%lang(tet) %{_datadir}/%{name}/%{vimdir}/spell/tet.*
%lang(th) %{_datadir}/%{name}/%{vimdir}/spell/th.*
%lang(tl) %{_datadir}/%{name}/%{vimdir}/spell/tl.*
%lang(tn) %{_datadir}/%{name}/%{vimdir}/spell/tn.*
%lang(uk) %{_datadir}/%{name}/%{vimdir}/spell/uk.*
%lang(yi) %{_datadir}/%{name}/%{vimdir}/spell/yi.*
%lang(yi-tr) %{_datadir}/%{name}/%{vimdir}/spell/yi-tr.*
%lang(zu) %{_datadir}/%{name}/%{vimdir}/spell/zu.*
%endif

%files minimal
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/virc
/bin/ex
/bin/vi
/bin/view
/bin/rvi
/bin/rview

%files enhanced
%defattr(-,root,root)
%{_bindir}/vim
%{_bindir}/rvim
%{_bindir}/vimdiff
%{_bindir}/ex
%{_bindir}/vimtutor
%config(noreplace) %{_sysconfdir}/profile.d/vim.*
%{_mandir}/man1/rvim.*
%{_mandir}/man1/vimdiff.*
%{_mandir}/man1/vimtutor.*

%files X11
%defattr(-,root,root)
%if "%{desktop_file}" == "1"
/%{_datadir}/applications/*
%else
/%{_sysconfdir}/X11/applnk/*/gvim.desktop
%endif
%{_bindir}/gvimtutor
%{_bindir}/gvim
%{_bindir}/gvimdiff
%{_bindir}/gview
%{_bindir}/gex
%{_bindir}/vimx
%{_bindir}/evim
%{_mandir}/man1/evim.*
%{_mandir}/man1/gvim*
%{_datadir}/icons/hicolor/*/apps/*

%changelog
* Mon Jul 20 2015 Andrew Seales <andrew.seales@ed.ac.uk> 7.4.052-1.1
- Add X11 support so copy&paste works through SSH using local X clipboard
* Mon Oct 07 2013 Andrew Seales <andrew.seales@ed.ac.uk> 7.4.052-1.0
- Upgrade to Vim 7.4 + patches
* Fri Feb 17 2012 Karsten Hopp <karsten@redhat.com> 7.2.411-1.8
- avoid multilib conflict with compressed text files (gzip -n)

* Fri Feb 17 2012 Karsten Hopp <karsten@redhat.com> 7.2.411-1.7
- fix syntax highlighting of httpd config files (663753)
- fix vimexplorer directory listings, i.e. vim .. (652610)
- don't print an additional 'e' in zh_CN.gbk vimexplorer (594997)
- fix macro usage in specfile template (634902)

* Mon Feb 14 2011 Karsten Hopp <karsten@redhat.com> 7.2.411-1.6
- upstream fix for #629568

* Wed Feb 02 2011 Karsten Hopp <karsten@redhat.com> 7.2.411-1.5
- fix syntax error when editing a text file containing "\c"

* Wed May 19 2010 Karsten Hopp <karsten@redhat.com> 7.2.411-1.4
- fix vim.sh scripts as id -u might return an empty string (#578795)

* Mon May 03 2010 Karsten Hopp <karsten@redhat.com> 7.2.411-1.3
- remove duplicate entry in menu (#587940)

* Tue Apr 20 2010 Karsten Hopp <karsten@redhat.com> 7.2.411-1.2
- fix rvim manpage
- Resolves: #583940

* Mon Apr 19 2010 Karsten Hopp <karsten@redhat.com> 7.2.411-1.1
- augroup "fedora" in /etc/vimrc renamed to "redhat"
- Resolves: #578785
- fix vim.csh  'tcsh -e' scripts
- Resolves: #578795

* Wed Mar 24 2010 Karsten Hopp <karsten@redhat.com> 7.2.411-1
- patchlevel 411

* Fri Feb 26 2010 Karsten Hopp <karsten@redhat.com> 7.2.245-3.3
- rebuild

* Mon Feb 22 2010 Karsten Hopp <karsten@redhat.com> 7.2.245-3.2
- update licenses and tarball

* Thu Dec 03 2009 Dennis Gregorovic <dgregor@redhat.com> - 2:7.2.245-3.1
- Rebuilt for RHEL 6

* Thu Aug 20 2009 Karsten Hopp <karsten@redhat.com> 7.2.245-3
- change range of system ids in /etc/profile.d/vim/* (#518555)

* Mon Aug 03 2009 Karsten Hopp <karsten@redhat.com> 7.2.245-2
- add fix for glibc fortify segfault (#514717, Adam Tkac)

* Sat Aug 01 2009 Karsten Hopp <karsten@redhat.com> 7.2.245-1
- add 97 upstream patches to get to patchlevel 245

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:7.2.148-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 27 2009 Karsten Hopp <karsten@redhat.com> 7.2.148-1
- patchlevel 148, fixes #461417

* Tue Mar 10 2009 Karsten Hopp <karsten@redhat.com> 7.2.132-1
- patchlevel 132, fixes accesses to freed memory

* Wed Mar 04 2009 Karsten Hopp <karsten@redhat.com> 7.2.131-1
- patchlevel 131

* Tue Feb 24 2009 Karsten Hopp <karsten@redhat.com> 7.2.127-1
- patchlevel 127

* Mon Feb 23 2009 Karsten Hopp <karsten@redhat.com> 7.2.124-1
- patchlevel 124

* Mon Jan 26 2009 Karsten Hopp <karsten@redhat.com> 7.2.088-1
- patchlevel 88

* Thu Jan 08 2009 Karsten Hopp <karsten@redhat.com> 7.2.079-2
- patchlevel 79

* Thu Dec 04 2008 Jesse Keating <jkeating@redhat.com> - 7.2.060-2
- Rebuild for new python.

* Mon Dec 01 2008 Karsten Hopp <karsten@redhat.com> 7.2.060-1
- patchlevel 60

* Mon Nov 10 2008 Karsten Hopp <karsten@redhat.com> 7.2.032-1
- patchlevel 32

* Mon Nov 03 2008 Karsten Hopp <karsten@redhat.com> 7.2.026-2
- add more /usr/share/vim/vimfiles directories (#444387)

* Mon Nov 03 2008 Karsten Hopp <karsten@redhat.com> 7.2.026-1
- patchlevel 26
- own some directories in /usr/share/vim/vimfiles (#469491)

* Tue Oct 21 2008 Karsten Hopp <karsten@redhat.com> 7.2.025-2
- re-enable clean

* Mon Oct 20 2008 Karsten Hopp <karsten@redhat.com> 7.2.025-1
- patchlevel 25
- add Categories tag to desktop file (#226526)
- add requirement on hicolor-icon-theme to vim-X11 (#226526)
- drop Amiga info files (#226526)
- remove non-utf8 man pages (#226526)
- drop Application from categories (#226526)

* Tue Sep 30 2008 Karsten Hopp <karsten@redhat.com> 7.2.022-1
- patchlevel 22

* Mon Sep 08 2008 Karsten Hopp <karsten@redhat.com> 7.2.013-1
- patchlevel 13

* Mon Aug 25 2008 Karsten Hopp <karsten@redhat.com> 7.2.006-1
- patchlevel 6

* Mon Aug 18 2008 Karsten Hopp <karsten@redhat.com> 7.2.002-1
- patchlevel 2
- fix specfile template (#446070)
- old specfile changelog moved to Changelog.rpm

* Fri Aug 14 2008 Karsten Hopp <karsten@redhat.com> 7.2.000-1
- vim 7.2
- drop 330 patches

# vim:nrformats-=octal
