# revision 15878
# category Package
# catalog-ctan /info/ctex-faq
# catalog-date 2009-11-09 15:03:08 +0100
# catalog-license fdl
# catalog-version undef
Name:		texlive-ctex-faq
Version:	20091109
Release:	1
Summary:	LaTeX FAQ by the Chinese TeX Society (ctex.org)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/ctex-faq
License:	FDL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ctex-faq.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ctex-faq.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
