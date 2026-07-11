%global tl_name lstbayes
%global tl_revision 48160

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Listings language driver for Bayesian modeling languages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lstbayes
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lstbayes.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lstbayes.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lstbayes.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides language drivers for the listings package for
several languages not included in that package: BUGS, JAGS, and Stan.

