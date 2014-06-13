# revision 15878
# category Package
# catalog-ctan /info/ctex-faq
# catalog-date 2009-11-09 15:03:08 +0100
# catalog-license fdl
# catalog-version undef
Name:		texlive-ctex-faq
Version:	20091109
Release:	7
Summary:	LaTeX FAQ by the Chinese TeX Society (ctex.org)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/ctex-faq
License:	FDL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ctex-faq.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ctex-faq.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
Most questions were collected on the bbs.ctex.org forum, and
were answered in detail by the author.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/ctex-faq/README
%doc %{_texmfdistdir}/doc/latex/ctex-faq/ctex-faq.pdf
%doc %{_texmfdistdir}/doc/latex/ctex-faq/src/ctex-faq.sty
%doc %{_texmfdistdir}/doc/latex/ctex-faq/src/ctex-faq.tex
%doc %{_texmfdistdir}/doc/latex/ctex-faq/src/make.bat

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20091109-2
+ Revision: 750666
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20091109-1
+ Revision: 718181
- texlive-ctex-faq
- texlive-ctex-faq
- texlive-ctex-faq
- texlive-ctex-faq

