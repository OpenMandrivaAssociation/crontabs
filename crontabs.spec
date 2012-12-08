Name:		crontabs
Version:	1.10
Release:	%mkrel 19
Summary:	Root crontab files used to schedule the execution of programs
License:	GPLv2+
Group:		System/Configuration/Other
Source0:	crontab
Source1:	config
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}
Requires:	run-parts

%description
The crontabs package contains root crontab files.  Crontab is the
program used to install, uninstall or list the tables used to drive the
cron daemon.  The cron daemon checks the crontab files to see when
particular commands are scheduled to be executed.  If commands are
scheduled, it executes them.

Crontabs handles a basic system function, so it should be installed on
your system.

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_sysconfdir}/cron.{hourly,daily,weekly,monthly,yearly} 
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
mkdir -p %{buildroot}%{_docdir}/%{name}

install -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/crontab

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{_docdir}/%{name}
%config(noreplace) %{_sysconfdir}/crontab
%config(noreplace) %{_sysconfdir}/sysconfig/crontab
%dir %{_sysconfdir}/cron.hourly
%dir %{_sysconfdir}/cron.daily
%dir %{_sysconfdir}/cron.weekly
%dir %{_sysconfdir}/cron.monthly
%dir %{_sysconfdir}/cron.yearly




%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.10-17mdv2011.0
+ Revision: 663427
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 1.10-16mdv2011.0
+ Revision: 603860
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 1.10-15mdv2010.1
+ Revision: 520051
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 1.10-14mdv2010.0
+ Revision: 413277
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.10-13mdv2009.1
+ Revision: 350749
- rebuild

* Thu Aug 28 2008 Frederic Crozat <fcrozat@mandriva.com> 1.10-12mdv2009.0
+ Revision: 276936
- bump release
- Add sysconfig file from Fedora, to control delay of cron.daily, ...

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 1.10-11mdv2009.0
+ Revision: 220518
- rebuild

  + Toshihiro Yamagishi <toshihiro@turbolinux.co.jp>
    - added Requires: run-parts

* Sat Dec 29 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.10-9mdv2008.1
+ Revision: 139222
- decompress sources
- add sample delay script as documentation, as suggested by Florin <florinenator@gmail.com>

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Sep 14 2007 Adam Williamson <awilliamson@mandriva.org> 1.10-8mdv2008.0
+ Revision: 85777
- rebuild for 2008
- drop file dependency on /usr/bin/run-parts, which is indirectly required by basesystem in any case
- Fedora license policy


* Mon Feb 12 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.10-7mdv2007.0
+ Revision: 119951
- Import crontabs

* Thu Dec 29 2005 Oden Eriksson <oeriksson@mandriva.com> 1.10-6mdk
- added the /etc/cron.yearly directory as it is 
  supported by logrotate-3.7.3

* Sat Jul 16 2005 Oden Eriksson <oeriksson@mandriva.com> 1.10-5mdk
- fix #14863

* Sun Jan 23 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.10-4mdk
- rebuild
- fix summary-ended-with-dot

