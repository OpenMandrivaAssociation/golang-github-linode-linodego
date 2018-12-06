%global goipath github.com/linode/linodego
Version:        0.7.0
%gometa

%ifnarch %{ix86} %{arm}
%bcond_without tests
%endif

Name:           %{goname}
Release:        1%{?dist}
Summary:        Go client for Linode REST v4 API
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
%if %{with tests}
BuildRequires:  golang(github.com/dnaeon/go-vcr/recorder)
BuildRequires:  golang(golang.org/x/oauth2)
BuildRequires:  golang(gopkg.in/resty.v1)
%endif


%description
%{summary}.


%package devel
Summary:        %{summary}
BuildArch:      noarch


%description devel
%{summary}.

This package contains the source code needed for building packages that import
the %{goipath} Go namespace.


%prep
%forgeautosetup


%install
%goinstall


%if %{with tests}
%check
# environment variables to use the API response fixtures
export LINODE_FIXTURE_MODE=play
export LINODE_TOKEN=awesometokenawesometokenawesometoken
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Tue Dec 04 2018 Carl George <carl@george.computer> - 0.7.0-1
- Latest upstream
- Skip tests on 32bit architectures

* Tue Nov 27 2018 Carl George <carl@george.computer> - 0.6.2-1
- Initial package
