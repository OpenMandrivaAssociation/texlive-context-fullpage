Name:		texlive-context-fullpage
Version:	47085
Release:	2
Summary:	Overfull pages with ConTeXt
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/context/contrib/context-fullpage
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-fullpage.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-fullpage.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-context

%description
The (ConTeXt) module copies the functionality of the fullpage,
and adds a styling parameter, given in the \usemodule command.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/interface/third/t-fullpage.xml
%{_texmfdistdir}/tex/context/third/fullpage
%doc %{_texmfdistdir}/doc/context/third/fullpage

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
