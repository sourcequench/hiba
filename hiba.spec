Name: hiba
Version: 1.0
Release: 1
Summary: a system built on top of regular OpenSSH certificate authentication
License: BSD
URL: https://github.com/google/%{name}
Source: https://github.com/google/%{name}/%{name}-%{version}.tar.gz
Packager: Ryan Shea <ryanshea@google.com>

%description
HIBA is a system built on top of regular OpenSSH certificate-based
authentication that allows for flexible authorization of principals on
pools of target hosts without the need to push customized authorized principal
files periodically.

%prep
%setup -q

%files
%license LICENSE
