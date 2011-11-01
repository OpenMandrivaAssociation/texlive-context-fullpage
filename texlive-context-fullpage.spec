Name:		texlive-context-fullpage
Version:	20110127
Release:	1
Summary:	Overfull pages with ConTeXt
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-fullpage
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-fullpage.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-fullpage.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-context
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Requires(post):	texlive-context.bin

%description
The (ConTeXt) module copies the functionality of the fullpage,
and adds a styling parameter, given in the \usemodule command.

%pre
    %_texmf_mtxrun_pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mtxrun_post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mtxrun_pre
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mtxrun_post
	%_texmf_mktexlsr_post
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
