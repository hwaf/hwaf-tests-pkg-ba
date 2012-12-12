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

    return

def install(ctx):
    return

### define a few dummy tasks --------------------------------------------------
from waflib import TaskGen
TaskGen.declare_chain(
    name='task-a',
    rule='/bin/cp ${SRC} ${TGT}',
    ext_in='.in',
    ext_out='.a',
    )
TaskGen.declare_chain(
    name='task-b',
    rule='/bin/cp ${SRC} ${TGT}',
    ext_in='.a',
    ext_out='.b',
    )
TaskGen.declare_chain(
    name='task-c',
    rule='/bin/cp ${SRC} ${TGT}',
    ext_in='.b',
    ext_out='.cxx',
    reentrant = False,
    )
