%global gem_name ruby-openid

%if 0%{?rhel} == 6 || 0%{?fedora} < 17
%define rubyabi 1.8
%else
%define rubyabi 1.9.1
%endif
%if 0%{?rhel} == 6
%global gem_dir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gem_docdir %{gem_dir}/doc/%{gem_name}-%{version}
%global gem_cache %{gem_dir}/cache/%{gem_name}-%{version}.gem
%global gem_spec %{gem_dir}/specifications/%{gem_name}-%{version}.gemspec
%global gem_instdir %{gem_dir}/gems/%{gem_name}-%{version}
%global gem_libdir %{gem_dir}/gems/%{gem_name}-%{version}/lib
%endif

Name:           rubygem-%{gem_name}
Version:        2.2.3
Release:        2%{?dist}
Summary:        Ruby library for verifying and serving OpenID identities

Group:          Development/Libraries

License:        ASL 2.0
URL:            https://github.com/openid/ruby-openid
Source0:        http://rubygems.org/downloads/%{gem_name}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%if 0%{?fedora}
BuildRequires:  rubygems-devel
%endif
BuildArch:      noarch
BuildRequires:  ruby
BuildRequires:  rubygem(minitest)
Requires:       ruby(abi) = %{rubyabi}
Provides:       rubygem(%{gem_name}) = %{version}

%description
The Ruby OpenID library, with batteries included.

A Ruby library for verifying and serving OpenID identities. 
Ruby OpenID makes it easy to add OpenID authentication to 
your web applications.

%package doc
Group: Documentation
Summary: Documentation for ruby-openid
Requires: %{name} = %{version}-%{release}

%description doc
Documentation distributed with the ruby-openid

%prep
%setup -q -c -T

mkdir -p .%{gem_dir}
gem install --local --install-dir .%{gem_dir} \
            --force --rdoc %{SOURCE0}


%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/


%check
# some tests need net connection
# https://github.com/openid/ruby-openid/issues/36
# we don't run tests for now
# export LANG=en_US.utf8
# cd %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}
# testrb -Ilib test

%clean
rm -rf %{buildroot}


%files
%dir %{gem_instdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/INSTALL.md
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/NOTICE
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/UPGRADE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}



%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/test
%doc %{gem_instdir}/examples



%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 06 2012 Vít Ondruch <vondruch@redhat.com> - 2.1.7-6
- Fixed test suite dependencies.

* Mon Feb 06 2012 Vít Ondruch <vondruch@redhat.com> - 2.1.7-5
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul  7 2009 Allisson Azevedo <allisson@gmail.com> 2.1.7-1
- Update to 2.1.7

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 21 2009 Allisson Azevedo <allisson@gmail.com> 2.1.4-1
- Update to 2.1.4

* Tue Sep  9 2008 Allisson Azevedo <allisson@gmail.com> 2.1.2-1
- Update to 2.1.2

* Mon May 19 2008 Allisson Azevedo <allisson@gmail.com> 2.0.4-1
- Update to 2.0.4

* Sat Feb  9 2008 Allisson Azevedo <allisson@gmail.com> 2.0.3-3
- Remove examples for doc package

* Fri Feb  1 2008 Allisson Azevedo <allisson@gmail.com> 2.0.3-2
- Remove CFLAGS in build section
- Create ruby-openid-doc package for docs
- Add examples for doc package
- Remove zero-length files in doc package
- Fix file-not-utf8

* Tue Jan 29 2008 Allisson Azevedo <allisson@gmail.com> 2.0.3-1
- Initial RPM release
