Name:           vmtouch
Version:        1.3.1
Release:        1%{?dist}
Summary:        Portable file system cache diagnostics and control

License:        BSD
URL:            http://hoytech.com/vmtouch/
Source0:        https://github.com/hoytech/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  /usr/bin/pod2man
BuildRequires:  perl-generators


%description
Vmtouch is a tool for learning about and controlling the file system cache of
Unix and Unix-like systems.


%prep
%setup -q


%build
make CFLAGS='%{optflags}'


%install
make install PREFIX=%{buildroot}%{_prefix} MANDIR=%{buildroot}%{_mandir}/man8


%files
%doc CHANGES README.md TODO TUNING.md
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*


%changelog
* Mon Dec 01 2020 Ioannis Giannakopulos <v-igiannakopoulos@eurobank.gr> - 1.3.1-1
- Initial package

