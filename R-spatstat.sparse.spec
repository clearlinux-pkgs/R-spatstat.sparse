#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-spatstat.sparse
Version  : 3.0.1
Release  : 16
URL      : https://cran.r-project.org/src/contrib/spatstat.sparse_3.0-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/spatstat.sparse_3.0-1.tar.gz
Summary  : Sparse Three-Dimensional Arrays and Linear Algebra Utilities
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-spatstat.sparse-lib = %{version}-%{release}
Requires: R-abind
Requires: R-spatstat.utils
Requires: R-tensor
BuildRequires : R-abind
BuildRequires : R-spatstat.utils
BuildRequires : R-tensor
BuildRequires : buildreq-R

%description
and supports standard operations on them.
	     The package also includes utility functions for
	     matrix calculations that are common in
	     statistics, such as quadratic forms.

%package lib
Summary: lib components for the R-spatstat.sparse package.
Group: Libraries

%description lib
lib components for the R-spatstat.sparse package.


%prep
%setup -q -n spatstat.sparse
cd %{_builddir}/spatstat.sparse

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1678831423

%install
export SOURCE_DATE_EPOCH=1678831423
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/spatstat.sparse/CITATION
/usr/lib64/R/library/spatstat.sparse/DESCRIPTION
/usr/lib64/R/library/spatstat.sparse/INDEX
/usr/lib64/R/library/spatstat.sparse/Meta/Rd.rds
/usr/lib64/R/library/spatstat.sparse/Meta/features.rds
/usr/lib64/R/library/spatstat.sparse/Meta/hsearch.rds
/usr/lib64/R/library/spatstat.sparse/Meta/links.rds
/usr/lib64/R/library/spatstat.sparse/Meta/nsInfo.rds
/usr/lib64/R/library/spatstat.sparse/Meta/package.rds
/usr/lib64/R/library/spatstat.sparse/NAMESPACE
/usr/lib64/R/library/spatstat.sparse/NEWS
/usr/lib64/R/library/spatstat.sparse/R/spatstat.sparse
/usr/lib64/R/library/spatstat.sparse/R/spatstat.sparse.rdb
/usr/lib64/R/library/spatstat.sparse/R/spatstat.sparse.rdx
/usr/lib64/R/library/spatstat.sparse/doc/packagesizes.txt
/usr/lib64/R/library/spatstat.sparse/help/AnIndex
/usr/lib64/R/library/spatstat.sparse/help/aliases.rds
/usr/lib64/R/library/spatstat.sparse/help/macros/defns.Rd
/usr/lib64/R/library/spatstat.sparse/help/paths.rds
/usr/lib64/R/library/spatstat.sparse/help/spatstat.sparse.rdb
/usr/lib64/R/library/spatstat.sparse/help/spatstat.sparse.rdx
/usr/lib64/R/library/spatstat.sparse/html/00Index.html
/usr/lib64/R/library/spatstat.sparse/html/R.css
/usr/lib64/R/library/spatstat.sparse/tests/linalgeb.R
/usr/lib64/R/library/spatstat.sparse/tests/sparse3Darrays.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/spatstat.sparse/libs/spatstat.sparse.so
/usr/lib64/R/library/spatstat.sparse/libs/spatstat.sparse.so.avx2
/usr/lib64/R/library/spatstat.sparse/libs/spatstat.sparse.so.avx512
