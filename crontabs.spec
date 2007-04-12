Summary:	Root crontab files used to schedule the execution of programs
Name:		crontabs
Version:	1.10
Release:	%mkrel 7
License:	GPL
Group:		System/Configuration/Other
Source0:	crontab.bz2
Requires:	/usr/bin/run-parts
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The crontabs package contains root crontab files.  Crontab is the
program used to install, uninstall or list the tables used to drive the
cron daemon.  The cron daemon checks the crontab files to see when
particular commands are scheduled to be executed.  If commands are
scheduled, it executes them.

Crontabs handles a basic system function, so it should be installed on
your system.

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}%{_sysconfdir}/cron.{hourly,daily,weekly,monthly,yearly}

bzip2 -dc  %{SOURCE0} > %{buildroot}%{_sysconfdir}/crontab
chmod 644 %{buildroot}%{_sysconfdir}/crontab

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/crontab
%dir %{_sysconfdir}/cron.hourly
%dir %{_sysconfdir}/cron.daily
%dir %{_sysconfdir}/cron.weekly
%dir %{_sysconfdir}/cron.monthly
%dir %{_sysconfdir}/cron.yearly


