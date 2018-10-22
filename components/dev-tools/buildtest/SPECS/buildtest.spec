#----------------------------------------------------------------------------bh-
# This RPM .spec file is part of the OpenHPC project.
#
# It may have been modified from the default version supplied by the underlying
# release package (if available) in order to apply patches, perform customized
# build/install configurations, and supply additional files to support
# desired integration conventions.
#
#-------------------------------------------------------------------------------

%include %{_sourcedir}/OHPC_macros
%{!?PROJ_DELIM: %global PROJ_DELIM -ohpc}

%define pname buildtest-framework

Summary:   Software Stack Testing Framework 
Name:      %{pname}%{PROJ_DELIM}
Version:   0.6.1
Release:   1%{?dist}
License:   GPLv3
Group:     %{PROJ_NAME}/dev-tools
URL:       https://buildtestdocs.readthedocs.io/en/latest/index.html
Source0:   https://pypi.io/packages/source/b/buildtest-framework/buildtest-framework-%{version}.tar.gz  
Source1:   https://pypi.io/packages/source/b/buildtest-configs/buildtest-configs-%{version}.tar.gz
Source2:   https://pypi.io/packages/source/P/Perl-buildtest-config/Perl-buildtest-config-%{version}.tar.gz
Source3:   https://pypi.io/packages/source/P/Python-buildtest-config/Python-buildtest-config-%{version}.tar.gz
Source4:   https://pypi.io/packages/source/R/R-buildtest-config/R-buildtest-config-%{version}.tar.gz
Source5:   https://pypi.io/packages/source/R/Ruby-buildtest-config/Ruby-buildtest-config-%{version}.tar.gz
Source6:   OHPC_macros
Requires:  cmake
%if !0%{?OHPC_BUILD}
BuildRequires: lmod%{PROJ_DELIM}
%endif
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-root

%define install_path %{OHPC_LIBS}/%{pname}/%{version}


%description
buildtest is an Automated Test Generating Framework for writing test cases 
efficiently and quickly for scientific applications. buildtest will generate 
test scripts for any app & version automatically and tests can be recreated as 
many times. 

buildtest makes use of EasyBuild easyconfig files to determine which module + 
toolchain to use. You will need module environment EnvironmentModules or Lmod 
on your system to use this framework

%prep
%setup -n %{pname}-%{version}

#%build
#python3 setup.py build

%install
mkdir -p %{buildroot}%{install_path}
pwd
python3 setup.py install --single-version-externally-managed -O1 --root=%{buildroot}%{install_path} --record=INSTALLED_FILES

#cd %{buildroot}%{install_path}
#tar xf %{SOURCE0} 
#tar xf %{SOURCE1} 
#tar xf %{SOURCE2} 
#tar xf %{SOURCE3} 
#tar xf %{SOURCE4} 
#tar xf %{SOURCE5} 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{OHPC_HOME}

%changelog
* Mon Sep 15 2014  <karl.w.schulz@intel.com> - 
- Initial build.

