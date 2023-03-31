Name:		texlive-lstbayes
Version:	48160
Release:	2
Summary:	Listings language driver for Bayesian modeling languages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lstbayes
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lstbayes.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lstbayes.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lstbayes.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides language drivers for the listings package
for several languages not included in that package: BUGS, JAGS,
and Stan.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/lstbayes
%{_texmfdistdir}/tex/latex/lstbayes
%doc %{_texmfdistdir}/doc/latex/lstbayes

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
