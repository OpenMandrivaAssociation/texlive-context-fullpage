# revision 23167
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-fullpage
# catalog-date 2011-01-27 09:54:35 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-context-fullpage
Version:	20110127
Release:	7
Summary:	Overfull pages with ConTeXt
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-fullpage
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-fullpage.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-fullpage.doc.tar.xz
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
%{_texmfdistdir}/tex/context/third/fullpage/t-fullpage.mkii
%{_texmfdistdir}/tex/context/third/fullpage/t-fullpage.mkiv
%doc %{_texmfdistdir}/doc/context/third/fullpage/README
%doc %{_texmfdistdir}/doc/context/third/fullpage/fullpage-doc.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20110127-2
+ Revision: 750496
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110127-1
+ Revision: 718131
- texlive-context-fullpage
- texlive-context-fullpage
- texlive-context-fullpage
- texlive-context-fullpage

