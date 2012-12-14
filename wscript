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
        name="app-pkg-ba",
        source="src/pkg-ba.cxx",
        target="app-pkg-ba",
        use="ROOT pkg-aa pkg-ab",
        )

    # use task-a -> b -> cxx
    ctx(
        features="cxx cxxshlib",
        name="pkg-ba",
        source="src/ba.in",
        target="pkg-ba",
        use="ROOT pkg-aa pkg-ab",
        )

    ctx(
        features     = 'py',
        name         = 'py-pkgba',
        source       = 'python/pkgba.py',
        install_path = '${INSTALL_AREA}/python',
        )

    return

def install(ctx):
    return
