%global debug_package %{nil}

Name:           bashtop
Version:        0.8.14
Release:        1
Summary:        Resource monitor that shows usage and stats for processor, memory, disks, network and processes.
License:        Apache v2
URL:            https://github.com/aristocratos/%{name}
Source:         https://github.com/aristocratos/%{name}/archive/v%{version}.tar.gz
BuildArch:      noarch
Requires:       bash >= 4.4

%description
- Easy to use, with a game inspired menu system.
- Fast and responsive UI with UP, DOWN keys process selection.
- Function for showing detailed stats for selected process.
- Ability to filter processes.
- Easy switching between sorting options.
- Send SIGTERM, SIGKILL, SIGINT to selected process.
- UI menu for changing all config file options.
- Auto scaling graph for network usage.
- Shows message in menu if new version is available

%prep
%setup -n %{name}-%{version}

%build
sed 's,/usr/bin/env bash,/bin/bash,g' -i bashtop

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
chmod +x %{name}
cp %{name} %{buildroot}/usr/bin/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/bin/%{name}

%changelog
* Mon Apr 27 2020 Jamie Curnow <jc@jc21.com> - 0.8.14-1
- v0.8.14

