Summary:	Root crontab files used to schedule the execution of programs
Name:		crontabs
Version:	1.11
Release:	33
License:	GPLv2+
Group:		System/Configuration/Other
Source0:	crontab
Source1:	config
BuildArch:	noarch
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
mkdir -p %{buildroot}%{_sysconfdir}/cron.{hourly,daily,weekly,monthly,yearly} 
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
mkdir -p %{buildroot}%{_docdir}/%{name}

install -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/crontab

%files
%doc %{_docdir}/%{name}
%config(noreplace) %{_sysconfdir}/crontab
%config(noreplace) %{_sysconfdir}/sysconfig/crontab
%dir %{_sysconfdir}/cron.hourly
%dir %{_sysconfdir}/cron.daily
%dir %{_sysconfdir}/cron.weekly
%dir %{_sysconfdir}/cron.monthly
%dir %{_sysconfdir}/cron.yearly

