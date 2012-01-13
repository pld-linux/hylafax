# TODO
# - unpackaged:
#   /usr/share/fax/faxcover_example_sgi.ps
#   /usr/share/man/README.hylafax-man-pages
#   /usr/share/man/diff.faxmsg.8c.gz
#   /usr/share/man/diff.typetest.8c.gz
Summary:	HylaFAX(tm) is a sophisticated enterprise strength fax package
Summary(pl.UTF-8):	HylaFAX(tm) to przemyślany, potężny pakiet do obsługi faksów
Name:		hylafax
Version:	4.4.7
Release:	2
License:	distributable
Group:		Applications/Communications
Source0:	ftp://ftp.hylafax.org/source/%{name}-%{version}.tar.gz
# Source0-md5:	023651ecb29014a16a19b7503f88d16a
#Source0:	http://dl.sourceforge.net/hylafax/%{name}-%{version}.tar.gz
Source1:	%{name}-cron_entries.tar.gz
# Source1-md5:	d5e2bd6447715654ba916b6f4d0d9343
Source2:	%{name}-defaults.tar.gz
# Source2-md5:	9fae3c4503ecd328a85cd23a430f4ddf
Source3:	%{name}-dialrules_extras.tar.gz
# Source3-md5:	092430f320963d31932b587152fb811b
Source4:	%{name}-man-pages.tar.bz2
# Source4-md5:	62772fbbce6cb3a918145ad8a836b4eb
Source6:	%{name}-logrotate
Source7:	%{name}-init
Source8:	%{name}-hyla.conf
Patch0:		%{name}-no_libgl_man.patch
Patch1:		%{name}-topmargin.patch
Patch2:		%{name}-pic.patch
Patch3:		%{name}-awk.patch
Patch4:		fchmod-prototype.patch
URL:		http://www.hylafax.org/
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtiff-progs
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	sed >= 4.1
BuildRequires:	zlib-devel
Requires:	%{name}-libs = %{version}-%{release}
Requires:	fonts-Type1-urw
Requires:	ghostscript
Requires:	libtiff-progs
Conflicts:	mgetty-sendfax
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		faxspool	/var/spool/fax

%description
HylaFAX(tm) is a sophisticated enterprise-strength fax package for
class 1 and 2 fax modems on Unix systems. It provides spooling
services and numerous supporting fax management tools. The fax clients
may reside on machines different from the server and client
implementations exist for a number of platforms including Windows.

You need this package if you are going to install hylafax-client
and/or hylafax server.

%description -l pl.UTF-8
HylaFAX(tm) to przemyślany, potężny pakiet do obsługi faksmodemów
klasy 1 i 2 na systemach uniksowych. Dostarcza usług kolejkowania i
wielu narzędzi do zarządzania faksami. Klienci mogą działać na
maszynach innych niż serwer, dostępne są implementacje klientów na
wiele platform, w tym na platformę Windows.

Ten pakiet zawiera pliki wspólne dla serwera i klienta HylaFAX.

%package server
Summary:	The files for the HylaFAX(tm) fax server
Summary(pl.UTF-8):	Pliki dla serwera faksów HylaFAX(tm)
Group:		Applications/Communications
Requires(post):	grep
Requires(post):	textutils
Requires(post,preun):	/sbin/chkconfig
Requires(preun):	/sbin/telinit
Requires(preun):	sed >= 4.0
Requires:	%{name} = %{version}-%{release}
Requires:	rc-scripts

%description server
HylaFAX(tm) is a sophisticated enterprise-strength fax package for
class 1 and 2 fax modems on Unix systems. It provides spooling
services and numerous supporting fax management tools. The fax clients
may reside on machines different from the server and client
implementations exist for a number of platforms including Windows.

This is the server portion of HylaFAX.

%description server -l pl.UTF-8
HylaFAX(tm) to przemyślany, potężny pakiet do obsługi faksmodemów
klasy 1 i 2 na systemach uniksowych. Dostarcza usług kolejkowania i
wielu narzędzi do zarządzania faksami. Klienci mogą działać na
maszynach innych niż serwer, implementacje klientów są dostępne na
wiele platform, w tym na platformę Windows.

Ten pakiet zawiera część serwerową HylaFAX.

%package client
Summary:	The files for the HylaFAX(tm) fax client
Summary(pl.UTF-8):	Pliki dla klienta faksów HylaFAX(tm)
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	metamail

%description client
HylaFAX(tm) is a sophisticated enterprise-strength fax package for
class 1 and 2 fax modems on Unix systems. It provides spooling
services and numerous supporting fax management tools. The fax clients
may reside on machines different from the server and client
implementations exist for a number of platforms including Windows.

This is the client portion of HylaFAX.

%description client -l pl.UTF-8
HylaFAX(tm) to przemyślany, potężny pakiet do obsługi faksmodemów
klasy 1 i 2 na systemach uniksowych. Dostarcza usług kolejkowania i
wielu narzędzi do zarządzania faksami. Klienci mogą działać na
maszynach innych niż serwer, implementacje klientów są dostępne na
wiele platform, w tym na platformę Windows.

Ten pakiet zawiera część kliencką HylaFAX.

%package libs
Summary:	Hylafax libraries
Summary(pl.UTF-8):	Biblioteki HylaFAX
Group:		Libraries

%description libs
HylaFAX(tm) is a sophisticated enterprise-strength fax package for
class 1 and 2 fax modems on Unix systems. It provides spooling
services and numerous supporting fax management tools. The fax clients
may reside on machines different from the server and client
implementations exist for a number of platforms including Windows.

This package contains the shared libraries of HylaFAX.

%description libs -l pl.UTF-8
HylaFAX(tm) to przemyślany, potężny pakiet do obsługi faksmodemów
klasy 1 i 2 na systemach uniksowych. Dostarcza usług kolejkowania i
wielu narzędzi do zarządzania faksami. Klienci mogą działać na
maszynach innych niż serwer, implementacje klientów są dostępne na
wiele platform, w tym na platformę Windows.

Ten pakiet zawiera biblioteki współdzielone HylaFAX.

%package devel
Summary:	Hylafax libraries development part
Summary(pl.UTF-8):	Pakiet dla programistów używających bibliotek HylaFAX
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This is development package for HylaFAX libraries.

%description devel -l pl.UTF-8
Pakiet dla programistów używających bibliotek HylaFAX.

%prep
%setup -q -a1 -a2 -a3
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%ifarch sparc64
sed -i -e 's/-fpic/-fPIC/g' configure
%endif

%build
# set dummy GCOPTS,GCXXOPTS to avoid adding "-g"
# the configure is too stupid to keep spaces in CC/CXX, so strip ccache if any
CC="%{__cc}"
CCXX="%{__cxx}"
CC=${CC#ccache } \
CXX=${CXX#ccache } \
GCOPTS=" " \
GCXXOPTS=" " \
./configure \
	--with-DIR_BIN=%{_bindir} \
	--with-DIR_SBIN=%{_sbindir} \
	--with-DIR_LIBEXEC=%{_sbindir} \
	--with-DIR_LIBDIR=%{_libdir} \
	--with-DIR_LIBDATA=%{_datadir}/fax \
	--with-DIR_MAN=%{_mandir} \
	--with-DIR_SPOOL=%{faxspool} \
	--with-PATH_GSRIP=/usr/bin/gs \
	--with-AFM=no \
	--with-DSO=auto \
	--with-PATH_VGETTY=/sbin/vgetty \
	--with-PATH_EGETTY=/sbin/egetty \
	--with-PATH_GETTY=/sbin/mgetty \
	--with-HTML=no \
	--with-PAGESIZE=A4 \
	--with-SYSVINIT=/etc/rc.d/init.d/hylafax \
	--with-INTERACTIVE=no \
	--with-SCRIPT_SH=/bin/bash \
	--with-PATH_SENDMAIL=/usr/sbin/sendmail

%{__make} -j1 \
	OPTIMIZER="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{logrotate.d,cron.hourly,cron.daily,rc.d/init.d} \
	$RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_libdir},%{_datadir}/fax} \
	$RPM_BUILD_ROOT%{faxspool}/{etc,config/defaults,bin} \
	$RPM_BUILD_ROOT%{_mandir}/{man1,man5,man8}

%{__make} install -e \
	FAXUSER=$(id -u) \
	FAXGROUP=$(id -g) \
	SYSUSER=$(id -u) \
	SYSGROUP=$(id -g) \
	BIN=$RPM_BUILD_ROOT%{_bindir} \
	SBIN=$RPM_BUILD_ROOT%{_sbindir} \
	LIBDATA=$RPM_BUILD_ROOT%{_datadir}/fax \
	LIBEXEC=$RPM_BUILD_ROOT%{_sbindir} \
	SPOOL=$RPM_BUILD_ROOT%{faxspool} \
	MAN=$RPM_BUILD_ROOT%{_mandir} \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir} \
	INSTALL_ROOT=$RPM_BUILD_ROOT

bzip2 -dc %{SOURCE4} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

# some hacks
sed -i -e 's!%{_prefix}%{_sysconfdir}/inetd.conf!%{_sysconfdir}/inetd.conf!g' $RPM_BUILD_ROOT%{_sbindir}/faxsetup
sed -i -e 's!%{_libdir}/aliases!%{_sysconfdir}/aliases!g' $RPM_BUILD_ROOT%{_sbindir}/faxsetup

# init
install -p %{SOURCE7} $RPM_BUILD_ROOT/etc/rc.d/init.d/hylafax

# defaults
install -p defaults/* $RPM_BUILD_ROOT%{faxspool}/config/defaults

# hyla.conf
cp -a %{SOURCE8} $RPM_BUILD_ROOT%{_datadir}/fax/hyla.conf

# cron entries
install -p hylafax_daily.cron  $RPM_BUILD_ROOT/etc/cron.daily/hylafax
install -p hylafax_hourly.cron $RPM_BUILD_ROOT/etc/cron.hourly/hylafax

# logrotate
cp -a %{SOURCE6} $RPM_BUILD_ROOT/etc/logrotate.d/hylafax

# dialrules extras
install -p dialrules_extras/dialrules* $RPM_BUILD_ROOT%{faxspool}/etc

ln -sf ps2fax.gs $RPM_BUILD_ROOT%{faxspool}/bin/ps2fax

# The Makefile puts the .so file in /usr/sbin. Move them to /usr/lib
#mv -f $RPM_BUILD_ROOT%{_sbindir}/*.so.* $RPM_BUILD_ROOT%{_libdir}
#mv -f $RPM_BUILD_ROOT%{_sbindir}/*.so $RPM_BUILD_ROOT%{_libdir}

# Since now the html doc dir is managed by the doc macro and not installed
# by HylaFAX, the CVS stuff need to be deleted
rm -rf $(find ./html -type d -name CVS)
rm -f ./html/{.cvsignore,Makefile.in}

# Some tools (manpage, man2html, unquote)
rm -f html/tools/{unquote,man2html}

# If Linux, what else...? :-), delete unnecessary files
%ifos linux
rm -f $RPM_BUILD_ROOT%{_sbindir}/{faxsetup.irix,faxsetup.bsdi}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%if 0
%preun client
%_preun_service hylafax

%post client
%_post_service hylafax
%{_sbindir}/faxsetup -client
%endif

%post server
/sbin/chkconfig --add hylafax
%service hylafax restart

if [ "$1" = 1 ]; then
	grep -q -i "faxgetty entry" /etc/inittab || \
	echo -e "# FaxGetty Entry\n#t0:23:respawn:%{_sbindir}/faxgetty ttyS0" >> /etc/inittab
	echo "Please check if new fax entry in /etc/inittab is correct."
	echo "Run \"%{_sbindir}/faxsetup -server\" to configure your fax server"
	echo "Run \"/sbin/telinit q\" to start faxgetty"
fi

%preun server
if [ "$1" = "0" ] ; then
	%service hylafax stop
	/sbin/chkconfig --del hylafax
	%{__sed} -i -e 's!^.*[Ff]ax[Gg]etty.*$!!' /etc/inittab
	/sbin/telinit q
fi

%files
%defattr(644,root,root,755)
%doc README TODO VERSION
%attr(755,root,root) %{_sbindir}/faxsetup
%attr(755,root,root) %{_sbindir}/faxsetup.linux
%dir %{_datadir}/fax

%files client
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sendfax
%attr(755,root,root) %{_bindir}/sendpage
%attr(755,root,root) %{_bindir}/faxstat
%attr(755,root,root) %{_bindir}/faxalter
%attr(755,root,root) %{_bindir}/faxcover
%attr(755,root,root) %{_bindir}/faxmail
%attr(755,root,root) %{_bindir}/faxrm
%attr(755,root,root) %{_sbindir}/edit-faxcover
%attr(755,root,root) %{_sbindir}/textfmt
%attr(755,root,root) %{_sbindir}/faxlock
%{_datadir}/fax/pagesizes
%config(noreplace) %verify(not md5 mtime size) %{_datadir}/fax/faxcover.ps
%config(noreplace) %verify(not md5 mtime size) %{_datadir}/fax/typerules
%config(noreplace) %verify(not md5 mtime size) %{_datadir}/fax/hyla.conf
%{_mandir}/man1/*

%files server
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/hylafax
%attr(750,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/cron.daily/hylafax
%attr(750,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/cron.hourly/hylafax
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/hylafax
%dir %{faxspool}
%dir %{faxspool}/bin
%attr(755,uucp,uucp) %dir %{faxspool}/client
%dir %{faxspool}/config
%dir %{faxspool}/dev
%dir %{faxspool}/etc
%dir %{faxspool}/etc/templates
%{faxspool}/etc/templates/README
%{faxspool}/etc/templates/html-sample1
%{faxspool}/etc/templates/en
%lang(de) %{faxspool}/etc/templates/de
%lang(es) %{faxspool}/etc/templates/es
%lang(fr) %{faxspool}/etc/templates/fr
%lang(it) %{faxspool}/etc/templates/it
%lang(pl) %{faxspool}/etc/templates/pl
%lang(pt) %{faxspool}/etc/templates/pt
%lang(pt_BR) %{faxspool}/etc/templates/pt_BR
%lang(ro) %{faxspool}/etc/templates/ro
%attr(755,uucp,uucp) %dir %{faxspool}/info
%attr(755,uucp,uucp) %dir %{faxspool}/log
%attr(755,uucp,uucp) %dir %{faxspool}/recvq
%attr(755,uucp,uucp) %dir %{faxspool}/status
%attr(755,uucp,uucp) %dir %{faxspool}/sendq
%attr(755,uucp,uucp) %dir %{faxspool}/doneq
%attr(755,uucp,uucp) %dir %{faxspool}/docq
%attr(755,uucp,uucp) %dir %{faxspool}/tmp
%attr(755,uucp,uucp) %dir %{faxspool}/pollq
%attr(755,uucp,uucp) %dir %{faxspool}/archive

%attr(600,uucp,uucp) %{faxspool}/FIFO
%{faxspool}/COPYRIGHT
%attr(644,uucp,uucp) %config(noreplace) %verify(not md5 mtime size) %{faxspool}/etc/xferfaxlog
%attr(600,uucp,root) %config(noreplace) %verify(not md5 mtime size) %{faxspool}/etc/hosts.hfaxd
%config(noreplace) %verify(not md5 mtime size) %{faxspool}/etc/lutRS18.pcf
%config(noreplace) %verify(not md5 mtime size) %{faxspool}/etc/dpsprinter.ps
%config(noreplace) %verify(not md5 mtime size) %{faxspool}/etc/cover.templ
%config(noreplace) %verify(not md5 mtime size) %{faxspool}/etc/dialrules*

%attr(755,root,root) %{faxspool}/bin/*
%{faxspool}/config/*

%attr(755,root,root) %{_sbindir}/hfaxd
%attr(755,root,root) %{_sbindir}/hylafax
%attr(755,root,root) %{_sbindir}/faxdeluser
%attr(755,root,root) %{_sbindir}/faxadduser
%attr(755,root,root) %{_sbindir}/choptest
%attr(755,root,root) %{_sbindir}/cqtest
%attr(755,root,root) %{_sbindir}/dialtest
%attr(755,root,root) %{_sbindir}/faxabort
%attr(755,root,root) %{_sbindir}/faxaddmodem
%attr(755,root,root) %{_sbindir}/faxanswer
%attr(755,root,root) %{_sbindir}/faxconfig
%attr(755,root,root) %{_sbindir}/faxcron
%attr(755,root,root) %{_sbindir}/faxgetty
%attr(755,root,root) %{_sbindir}/faxinfo
%attr(755,root,root) %{_sbindir}/faxlock
%attr(755,root,root) %{_sbindir}/faxmodem
%attr(755,root,root) %{_sbindir}/faxmsg
%attr(755,root,root) %{_sbindir}/faxq
%attr(755,root,root) %{_sbindir}/faxqclean
%attr(755,root,root) %{_sbindir}/faxquit
%attr(755,root,root) %{_sbindir}/faxsend
%attr(755,root,root) %{_sbindir}/faxstate
%attr(755,root,root) %{_sbindir}/faxwatch
%attr(755,root,root) %{_sbindir}/lockname
%attr(755,root,root) %{_sbindir}/ondelay
%attr(755,root,root) %{_sbindir}/pagesend
%attr(755,root,root) %{_sbindir}/probemodem
%attr(755,root,root) %{_sbindir}/recvstats
%attr(755,root,root) %{_sbindir}/tagtest
%attr(755,root,root) %{_sbindir}/tiffcheck
%attr(755,root,root) %{_sbindir}/tsitest
%attr(755,root,root) %{_sbindir}/typetest
%attr(755,root,root) %{_sbindir}/xferfaxstats

%{_datadir}/fax/faxmail.ps
%config(noreplace) %verify(not md5 mtime size) %{_datadir}/fax/hfaxd.conf

%{_mandir}/man5/*
%{_mandir}/man8/*

%files libs
%defattr(644,root,root,755)
%doc COPYRIGHT
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
#%doc html
%attr(755,root,root) %{_libdir}/*.so
