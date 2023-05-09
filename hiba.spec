Name: hiba
Version: 1.0
Release: 1
Summary: a system built on top of regular OpenSSH certificate-based authentication
License: BSD
URL: https://github.com/google/%{name}
Source: https://github.com/google/hiba/archive/refs/heads/main.tar.gz
Packager: Ryan Shea <ryanshea@google.com>

%description
HIBA is a system built on top of regular OpenSSH certificate-based
authentication that allows to manage flexible authorization of principals on
pools of target hosts without the need to push customized authorized_users files
periodically.

%prep
%setup -q

%files
%license LICENSE
