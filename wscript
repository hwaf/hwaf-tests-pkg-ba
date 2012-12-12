# -*- python -*-

import waflib.Logs as msg

def pkg_deps(ctx):
    ctx.use_pkg('pkg-aa')
    ctx.use_pkg('pkg-ab')
    return

def configure(ctx):
    return

def build(ctx):
    ctx(
        features="cxx cxxprogram",
        name="pkg-ba",
        source="src/pkg-ba.cxx",
        target="pkg-ba",
        use="ROOT pkg-aa pkg-ab",
        )

    if ctx.cmd != 'clean':
        ctx.check_cxx(
            features='cxx cxxprogram',
            msg='checking pkg-ba',
            okmsg='ok',
            fragment='''\
            #include "pkg-aa/h1d.hh"
            #include "pkg-ab/h1d.hh"

            #include <iostream>

            int main(int, char**) {
              std::cout << "::: pkg-ba..." << std::endl
                        << "::: testing pkg_aa..." << std::endl;
              pkg_aa::test_h1d();
              std::cout << "::: testing pkg_ab..." << std::endl;
              pkg_ab::test_h1d();
              std::cout << "::: done." << std::endl;
              return 0;
            }
            ''',
            use="ROOT pkg-aa pkg-ab",
            execute = True,
            mandatory = True,
            )
        pass
    
    return

def install(ctx):
    return
