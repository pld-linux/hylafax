Summary:	HylaFAX(tm) is a sophisticated enterprise strength fax package
Name:		hylafax
Version:	4.1
Release:	0.1
License:	distributable
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
URL:		http://www.hylafax.org/
Source0:	ftp://ftp.hylafax.org/source/%{name}-%{version}.tar.gz
Source1:	%{name}-cron_entries.tar.gz
Source2:	%{name}-defaults.tar.gz
Source3:	%{name}-dialrules_extras.tar.gz
Source6:	%{name}-logrotate
Source7:	%{name}-init
Source8:	%{name}-hyla.conf
Patch1:		%{name}-dso.patch
Patch2:		%{name}-dso.chris.patch
Patch4:		%{name}-rings-cid-passing.patch
Patch5:		%{name}-mdk.patch
Patch6:		%{name}-topmargin.patch
Patch7:		%{name}-priority.patch
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	zlib-devel
Requires:	ghostscript
Requires:	libtiff
Requires:	%{name}-libs = %{version}
Requires:	libtiff-progs
Conflicts:	mgetty-sendfax
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define faxspool /var/spool/fax

%description
HylaFAX(tm) is a sophisticated enterprise-strength fax package for
class 1 and 2 fax modems on unix systems. It provides spooling
services and numerous supporting fax management tools. The fax clients
may reside on machines different from the server and client
implementations exist for a number of platforms including windows.

You need this package if you are going to install hylafax-client
and/or hylafax server.

%package 	server
Summary:	The files for the HylaFAX(tm) fax server.
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Requires:	%{name}

%description server
HylaFAX(tm) is a sophisticated enterprise-strength fax package for
class 1 and 2 fax modems on unix systems. It provides spooling
services and numerous supporting fax management tools. The fax clients
may reside on machines different from the server and client
implementations exist for a number of platforms including windows.

This is the server portion of HylaFAX.

%package 	client
Summary:	The files for the HylaFAX(tm) fax client.
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Requires:	%{name}

%description client
HylaFAX(tm) is a sophisticated enterprise-strength fax package for
class 1 and 2 fax modems on unix systems. It provides spooling
services and numerous supporting fax management tools. The fax clients
may reside on machines different from the server and client
implementations exist for a number of platforms including windows.

This is the client portion of HylaFAX.

%package 	libs
Summary:	Hylafax libraries
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja

%description libs
HylaFAX(tm) is a sophisticated enterprise-strength fax package for
class 1 and 2 fax modems on unix systems. It provides spooling
services and numerous supporting fax management tools. The fax clients
may reside on machines different from the server and client
implementations exist for a number of platforms including windows.

This is the shared librairies of HylaFAX.

%package	devel
Summary:	Hylafax libraries
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Requires:	%{name}-libs = %{version}

%description devel
HylaFAX(tm) is a sophisticated enterprise-strength fax package for
class 1 and 2 fax modems on unix systems. It provides spooling
services and numerous supporting fax management tools. The fax clients
may reside on machines different from the server and client
implementations exist for a number of platforms including windows.

This is the shared librairies of HylaFAX.

%prep
%setup -q -n %{name}-%{version} -a 1 -a 2 -a 3 -q
%patch1 -p1
%patch2 -p1
%patch4 
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
./configure \
	--with-DIR_BIN=%{_bindir} \
	--with-DIR_SBIN=%{_sbindir} \
	--with-DIR_LIBEXEC=%{_sbindir} \
	--with-DIR_LIBDATA=%{_datadir}/fax \
	--with-DIR_MAN=%{_mandir} \
	--with-DIR_SPOOL=%{faxspool} \
	--with-PATH_GSRIP=%{_bindir}/gs \
	--with-AFM=no \
	--with-DSO=LINUX \
	--with-DSOSUF=so \
	--with-PATH_VGETTY=/sbin/vgetty \
	--with-PATH_EGETTY=/sbin/egetty \
	--with-PATH_GETTY=/sbin/mgetty \
	--with-HTML=no \
	--with-PAGESIZE=A4 \
	--with-SYSVINIT=/etc/rc.d/init.d/hylafax \
	--with-INTERACTIVE=no \
	--with-SCRIPT_SH=/bin/sh

%{__make} OPTIMIZER="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sysconfdir}/{logrotate.d,cron.hourly,cron.daily,rc.d/init.d}
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_sbindir}
install -d $RPM_BUILD_ROOT%{_libdir}
install -d $RPM_BUILD_ROOT%{_datadir}/fax
install -d $RPM_BUILD_ROOT%{faxspool}/{etc,config/defaults,bin}
install -d $RPM_BUILD_ROOT%{_mandir}/{man1,man5,man8}

%{__make} install -e \
	FAXUSER=`id -u` \
	FAXGROUP=`id -g` \
	SYSUSER=`id -u` \
	SYSGROUP=`id -g` \
	BIN=$RPM_BUILD_ROOT%{_bindir} \
	SBIN=$RPM_BUILD_ROOT%{_sbindir} \
	LIBDATA=$RPM_BUILD_ROOT%{_datadir}/fax \
	LIBEXEC=$RPM_BUILD_ROOT%{_sbindir} \
	SPOOL=$RPM_BUILD_ROOT%{faxspool} \
	MAN=$RPM_BUILD_ROOT%{_mandir} \
	INSTALL_ROOT=$RPM_BUILD_ROOT

# some hacks
perl -pi -e 's!%{_prefix}%{_sysconfdir}/inetd.conf!%{_sysconfdir}/inetd.conf!g' $RPM_BUILD_ROOT%{_sbindir}/faxsetup
perl -pi -e 's!%{_libdir}/aliases!%{_sysconfdir}/aliases!g' $RPM_BUILD_ROOT%{_sbindir}/faxsetup


# init
cat %{SOURCE7} > $RPM_BUILD_ROOT/etc/rc.d/init.d/hylafax
chmod 755 $RPM_BUILD_ROOT/etc/rc.d/init.d/hylafax

# defaults 
install defaults/* $RPM_BUILD_ROOT%{faxspool}/config/defaults/

# hyla.conf
cat %{SOURCE8} > $RPM_BUILD_ROOT%{_datadir}/fax/hyla.conf

# cron entries
install -m 755 hylafax_daily.cron  $RPM_BUILD_ROOT%{_sysconfdir}/cron.daily/hylafax
install -m 755 hylafax_hourly.cron $RPM_BUILD_ROOT%{_sysconfdir}/cron.hourly/hylafax

# logrotate
cat %{SOURCE6} > $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/hylafax

# dialrules extras
install dialrules_extras/dialrules* $RPM_BUILD_ROOT%{faxspool}%{_sysconfdir}

(cd $RPM_BUILD_ROOT%{faxspool}/bin; ln -s ps2fax.gs ps2fax)


# The Makefile puts the .so file in /usr/sbin. Move them to /usr/lib
mv $RPM_BUILD_ROOT%{_sbindir}/*.so.* $RPM_BUILD_ROOT%{_libdir}
mv $RPM_BUILD_ROOT%{_sbindir}/*.so $RPM_BUILD_ROOT%{_libdir}

# put execute permission on .so so that RPM doesn't warn
chmod +x $RPM_BUILD_ROOT%{_libdir}/lib*.so.*
chmod +x $RPM_BUILD_ROOT%{_libdir}/lib*.so

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

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

#%preun client
#%_preun_service hylafax
#
#
#%post client
#%_post_service hylafax
#%{_sbindir}/faxsetup -client

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
echo "Run \"/sbin/init q\" to start faxgetty"

%preun server
if [ "$1" = "0" ] ; then
	if [ -f /var/lock/subsys/hylafax ]; then
		/etc/rc.d/init.d/hylafax stop >&2
	fi
	perl -pi -e 's!^.*faxgetty.*$!!g' %{_sysconfdir}/inittab > %{_sysconfdir}/inittab.$$
	/sbin/init q
fi

%files 
%defattr(644,root,root,755)
%doc README TODO VERSION COPYRIGHT
%attr(755,root,root) %{_sbindir}/faxsetup
%attr(755,root,root) %{_sbindir}/faxsetup.linux


%files client
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sendfax
%attr(755,root,root) %{_bindir}/sendpage
%attr(755,root,root) %{_bindir}/faxstat
%attr(755,root,root) %{_bindir}/faxalter
%attr(755,root,root) %{_bindir}/faxcover
%attr(755,root,root) %{_bindir}/faxmail
%attr(755,root,root) %{_bindir}/faxrm
%attr(755,root,root) %{_sbindir}/textfmt
%{_datadir}/fax/pagesizes
%{_datadir}/fax/faxcover.ps
%{_datadir}/fax/typerules
%{_datadir}/fax/hyla.conf
%{_mandir}/man1/*


%files server
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/hylafax
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/cron.daily/hylafax
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/cron.hourly/hylafax
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/logrotate.d/hylafax
%attr(-,uucp,uucp) %dir %{faxspool}
%attr(-,uucp,uucp) %dir %{faxspool}/bin
%attr(-,uucp,uucp) %dir %{faxspool}/client
%attr(-,uucp,uucp) %dir %{faxspool}/config
%attr(-,uucp,uucp) %dir %{faxspool}/dev
%attr(-,uucp,uucp) %dir %{faxspool}%{_sysconfdir}
%attr(-,uucp,uucp) %dir %{faxspool}/info
%attr(-,uucp,uucp) %dir %{faxspool}/log
%attr(-,uucp,uucp) %dir %{faxspool}/recvq
%attr(-,uucp,uucp) %dir %{faxspool}/status
%attr(-,uucp,uucp) %dir %{faxspool}/sendq
%attr(-,uucp,uucp) %dir %{faxspool}/doneq
%attr(-,uucp,uucp) %dir %{faxspool}/docq
%attr(-,uucp,uucp) %dir %{faxspool}/tmp
%attr(-,uucp,uucp) %dir %{faxspool}/pollq
%attr(-,uucp,uucp) %dir %{faxspool}/archive

%attr(-,uucp,uucp) %{faxspool}/FIFO
%attr(-,root,root) %{faxspool}/COPYRIGHT
%attr(-,uucp,uucp) %config(noreplace) %verify(not size mtime md5) %{faxspool}%{_sysconfdir}/xferfaxlog
%attr(-,uucp,uucp) %config(noreplace) %verify(not size mtime md5) %{faxspool}%{_sysconfdir}/hosts.hfaxd
%attr(-,uucp,uucp) %config(noreplace) %verify(not size mtime md5) %{faxspool}%{_sysconfdir}/lutRS18.pcf
%attr(-,uucp,uucp) %config(noreplace) %verify(not size mtime md5) %{faxspool}%{_sysconfdir}/dpsprinter.ps
%attr(-,uucp,uucp) %config(noreplace) %verify(not size mtime md5) %{faxspool}%{_sysconfdir}/cover.templ
%attr(-,uucp,uucp) %config(noreplace) %verify(not size mtime md5) %{faxspool}%{_sysconfdir}/dialrules*

%{faxspool}/bin/*
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
%{_datadir}/fax/hfaxd.conf

%{_mandir}/man5/* 
%{_mandir}/man8/*

%files devel
%defattr(644,root,root,755)
%doc html COPYRIGHT
%{_libdir}/*.so


%files libs
%defattr(644,root,root,755)
%doc COPYRIGHT
%{_libdir}/*.so.*
