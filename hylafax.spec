Summary:	HylaFAX(tm) is a sophisticated enterprise strength fax package
Summary(pl):	HylaFAX(tm) to przemy¶lany, potê¿ny pakiet do obs³ugi faksów
Name:		hylafax
Version:	4.1.5
Release:	0.3
License:	distributable
Group:		Applications/Communications
Source0:	ftp://ftp.hylafax.org/source/%{name}-%{version}.tar.gz
# Source0-md5:	67135ae721f7a927e0f9a96644694617
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
Patch2:		%{name}-new-libtiff.patch
URL:		http://www.hylafax.org/
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	zlib-devel
BuildRequires:	gcc-c++
BuildRequires:	libtiff-progs
Requires:	%{name}-libs = %{version}
Requires:	ghostscript
Requires:	ghostscript-fonts-std
Requires:	libtiff-progs
Conflicts:	mgetty-sendfax
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		faxspool	/var/spool/fax

%description
HylaFAX(tm) is a sophisticated enterprise-strength fax package for
class 1 and 2 fax modems on unix systems. It provides spooling
services and numerous supporting fax management tools. The fax clients
may reside on machines different from the server and client
implementations exist for a number of platforms including Windows.

You need this package if you are going to install hylafax-client
and/or hylafax server.

%description -l pl
HylaFAX(tm) to przemy¶lany, potê¿ny pakiet do obs³ugi faxmodemów klasy
1 i 2 na systemach uniksowych. Daje serwisy kolejkuj±ce i wiele
narzêdzi do zarz±dzania faksami. Klienci mog± dzia³aæ na maszynach
innych ni¿ serwer, implementacje klientów s± dostêpne na wiele
platform, w tym Windows.

Ten pakiet zawiera pliki wspólne dla serwera i klienta HylaFAX.

%package server
Summary:	The files for the HylaFAX(tm) fax server
Summary(pl):	Pliki dla serwera faksów HylaFAX(tm)
Group:		Applications/Communications
Requires:	%{name} = %{version}
Requires(post,preun):	/sbin/chkconfig
Requires(post):	grep
Requires(post):	textutils
Requires(preun):	perl
Requires(preun):	/sbin/telinit

%description server
HylaFAX(tm) is a sophisticated enterprise-strength fax package for
class 1 and 2 fax modems on unix systems. It provides spooling
services and numerous supporting fax management tools. The fax clients
may reside on machines different from the server and client
implementations exist for a number of platforms including Windows.

This is the server portion of HylaFAX.

%description server -l pl
HylaFAX(tm) to przemy¶lany, potê¿ny pakiet do obs³ugi faxmodemów klasy
1 i 2 na systemach uniksowych. Daje serwisy kolejkuj±ce i wiele
narzêdzi do zarz±dzania faksami. Klienci mog± dzia³aæ na maszynach
innych ni¿ serwer, implementacje klientów s± dostêpne na wiele
platform, w tym Windows.

Ten pakiet zawiera czê¶æ serwerow± HylaFAX.

%package client
Summary:	The files for the HylaFAX(tm) fax client
Summary(pl):	Pliki dla klienta faksów HylaFAX(tm)
Group:		Applications/Communications
Requires:	%{name} = %{version}

%description client
HylaFAX(tm) is a sophisticated enterprise-strength fax package for
class 1 and 2 fax modems on unix systems. It provides spooling
services and numerous supporting fax management tools. The fax clients
may reside on machines different from the server and client
implementations exist for a number of platforms including Windows.

This is the client portion of HylaFAX.

%description client -l pl
HylaFAX(tm) to przemy¶lany, potê¿ny pakiet do obs³ugi faxmodemów klasy
1 i 2 na systemach uniksowych. Daje serwisy kolejkuj±ce i wiele
narzêdzi do zarz±dzania faksami. Klienci mog± dzia³aæ na maszynach
innych ni¿ serwer, implementacje klientów s± dostêpne na wiele
platform, w tym Windows.

Ten pakiet zawiera czê¶æ klienck± HylaFAX.

%package libs
Summary:	Hylafax libraries
Summary(pl):	Biblioteki HylaFAX
Group:		Libraries

%description libs
HylaFAX(tm) is a sophisticated enterprise-strength fax package for
class 1 and 2 fax modems on unix systems. It provides spooling
services and numerous supporting fax management tools. The fax clients
may reside on machines different from the server and client
implementations exist for a number of platforms including Windows.

This package contains the shared libraries of HylaFAX.

%description libs -l pl
HylaFAX(tm) to przemy¶lany, potê¿ny pakiet do obs³ugi faxmodemów klasy
1 i 2 na systemach uniksowych. Daje serwisy kolejkuj±ce i wiele
narzêdzi do zarz±dzania faksami. Klienci mog± dzia³aæ na maszynach
innych ni¿ serwer, implementacje klientów s± dostêpne na wiele
platform, w tym Windows.

Ten pakiet zawiera biblioteki wspó³dzielone HylaFAX

%package devel
Summary:	Hylafax libraries development part
Summary(pl):	Pakiet dla programistów u¿ywaj±cych bibliotek HylaFAX
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}

%description devel
HylaFAX(tm) is a sophisticated enterprise-strength fax package for
class 1 and 2 fax modems on unix systems. It provides spooling
services and numerous supporting fax management tools. The fax clients
may reside on machines different from the server and client
implementations exist for a number of platforms including Windows.

This is development package for HylaFAX libraries.

%description devel -l pl
Pakiet dla programistów u¿ywaj±cych bibliotek HylaFAX.

%prep
%setup -q -n %{name}-%{version} -a 1 -a 2 -a 3 -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
./configure \
	--with-DIR_BIN=%{_bindir} \
	--with-DIR_SBIN=%{_sbindir} \
	--with-DIR_LIBEXEC=%{_bindir} \
	--with-DIR_LIBDATA=%{_datadir}/fax \
	--with-DIR_MAN=%{_mandir} \
	--with-DIR_SPOOL=%{faxspool} \
	--with-PATH_GSRIP=%{_bindir}/gs \
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

%{__make} OPTIMIZER="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/{logrotate.d,cron.hourly,cron.daily,rc.d/init.d} \
	$RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_libdir},%{_datadir}/fax} \
	$RPM_BUILD_ROOT%{faxspool}/{etc,config/defaults,bin} \
	$RPM_BUILD_ROOT%{_mandir}/{man1,man5,man8}

%{__make} install -e \
	FAXUSER=`id -u` \
	FAXGROUP=`id -g` \
	SYSUSER=`id -u` \
	SYSGROUP=`id -g` \
	BIN=$RPM_BUILD_ROOT%{_bindir} \
	SBIN=$RPM_BUILD_ROOT%{_sbindir} \
	LIBDATA=$RPM_BUILD_ROOT%{_datadir}/fax \
	LIBEXEC=$RPM_BUILD_ROOT%{_bindir} \
	SPOOL=$RPM_BUILD_ROOT%{faxspool} \
	MAN=$RPM_BUILD_ROOT%{_mandir} \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir} \
	INSTALL_ROOT=$RPM_BUILD_ROOT

bzip2 -dc %{SOURCE4} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

# some hacks
perl -pi -e 's!%{_prefix}%{_sysconfdir}/inetd.conf!%{_sysconfdir}/inetd.conf!g' $RPM_BUILD_ROOT%{_sbindir}/faxsetup
perl -pi -e 's!%{_libdir}/aliases!%{_sysconfdir}/aliases!g' $RPM_BUILD_ROOT%{_sbindir}/faxsetup

# init
install %{SOURCE7} $RPM_BUILD_ROOT/etc/rc.d/init.d/hylafax

# defaults
install defaults/* $RPM_BUILD_ROOT%{faxspool}/config/defaults/

# hyla.conf
install %{SOURCE8} $RPM_BUILD_ROOT%{_datadir}/fax/hyla.conf

# cron entries
install hylafax_daily.cron  $RPM_BUILD_ROOT%{_sysconfdir}/cron.daily/hylafax
install hylafax_hourly.cron $RPM_BUILD_ROOT%{_sysconfdir}/cron.hourly/hylafax

# logrotate
install %{SOURCE6} $RPM_BUILD_ROOT/etc/logrotate.d/hylafax

# dialrules extras
install dialrules_extras/dialrules* $RPM_BUILD_ROOT%{faxspool}%{_sysconfdir}

(cd $RPM_BUILD_ROOT%{faxspool}/bin; ln -sf ps2fax.gs ps2fax)

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

#%preun client
#%_preun_service hylafax
#
#%post client
#%_post_service hylafax
#%%{_sbindir}/faxsetup -client

%post server
/sbin/chkconfig --add hylafax
if [ -f /var/lock/subsys/hylafax ]; then
	/etc/rc.d/init.d/hylafax restart
else
	echo "Run \"/etc/rc.d/init.d/hylafax start\" to start hylafax daemons." >&2
fi

cat %{_sysconfdir}/inittab | grep -i "faxgetty entry" || \
echo -e "# FaxGetty Entry\n#t0:23:respawn:%{_sbindir}/faxgetty ttyS0" >> %{_sysconfdir}/inittab
echo "Please check if new fax entry in %{_sysconfdir}/inittab is correct."
echo "Run \"%{_sbindir}/faxsetup -server\" to configure your fax server"
echo "Run \"/sbin/telinit q\" to start faxgetty"

%preun server
if [ "$1" = "0" ] ; then
	if [ -f /var/lock/subsys/hylafax ]; then
		/etc/rc.d/init.d/hylafax stop >&2
	fi
	/sbin/chkconfig --del hylafax
	perl -pi -e 's!^.*faxgetty.*$!!g' %{_sysconfdir}/inittab > %{_sysconfdir}/inittab.$$
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
%attr(755,root,root) %{_bindir}/textfmt
%{_datadir}/fax/pagesizes
%{_datadir}/fax/faxcover.ps
%{_datadir}/fax/typerules
%{_datadir}/fax/hyla.conf
%{_mandir}/man1/*

%files server
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/hylafax
%attr(750,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/cron.daily/hylafax
%attr(750,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/cron.hourly/hylafax
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/logrotate.d/hylafax
%dir %{faxspool}
%dir %{faxspool}/bin
%attr(755,uucp,uucp) %dir %{faxspool}/client
%dir %{faxspool}/config
%dir %{faxspool}/dev
%dir %{faxspool}%{_sysconfdir}
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
%attr(644,uucp,uucp) %config(noreplace) %verify(not size mtime md5) %{faxspool}%{_sysconfdir}/xferfaxlog
%config(noreplace) %verify(not size mtime md5) %{faxspool}%{_sysconfdir}/hosts.hfaxd
%config(noreplace) %verify(not size mtime md5) %{faxspool}%{_sysconfdir}/lutRS18.pcf
%config(noreplace) %verify(not size mtime md5) %{faxspool}%{_sysconfdir}/dpsprinter.ps
%config(noreplace) %verify(not size mtime md5) %{faxspool}%{_sysconfdir}/cover.templ
%config(noreplace) %verify(not size mtime md5) %{faxspool}%{_sysconfdir}/dialrules*

%attr(755,root,root) %{faxspool}/bin/*
%{faxspool}/config/*

%attr(755,root,root) %{_bindir}/hfaxd
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
%attr(755,root,root) %{_bindir}/faxgetty
%attr(755,root,root) %{_sbindir}/faxinfo
%attr(755,root,root) %{_sbindir}/faxlock
%attr(755,root,root) %{_sbindir}/faxmodem
%attr(755,root,root) %{_sbindir}/faxmsg
%attr(755,root,root) %{_sbindir}/faxq
%attr(755,root,root) %{_sbindir}/faxqclean
%attr(755,root,root) %{_sbindir}/faxquit
%attr(755,root,root) %{_bindir}/faxsend
%attr(755,root,root) %{_sbindir}/faxstate
%attr(755,root,root) %{_sbindir}/faxwatch
%attr(755,root,root) %{_bindir}/lockname
%attr(755,root,root) %{_bindir}/ondelay
%attr(755,root,root) %{_bindir}/pagesend
%attr(755,root,root) %{_sbindir}/probemodem
%attr(755,root,root) %{_sbindir}/recvstats
%attr(755,root,root) %{_sbindir}/tagtest
%attr(755,root,root) %{_sbindir}/tiffcheck
%attr(755,root,root) %{_sbindir}/tsitest
%attr(755,root,root) %{_sbindir}/typetest
%attr(755,root,root) %{_sbindir}/xferfaxstats

%{_datadir}/fax/faxmail.ps
%{_datadir}/fax/hfaxd.conf

%{_mandir}/man5/*
%{_mandir}/man8/*

%files libs
%defattr(644,root,root,755)
%doc COPYRIGHT
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc html
%attr(755,root,root) %{_libdir}/*.so
