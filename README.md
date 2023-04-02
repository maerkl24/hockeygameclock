![Hockey Game Clock Banner](assets/banner.png)

[![Format](https://github.com/maerkl24/hockeygameclock/actions/workflows/format.yml/badge.svg)](https://github.com/maerkl24/hockeygameclock/actions/workflows/format.yml)
[![Linting](https://github.com/maerkl24/hockeygameclock/actions/workflows/linting.yml/badge.svg)](https://github.com/maerkl24/hockeygameclock/actions/workflows/linting.yml)
[![Tests](https://github.com/maerkl24/hockeygameclock/actions/workflows/tests.yml/badge.svg)](https://github.com/maerkl24/hockeygameclock/actions/workflows/tests.yml)
[![Docs](https://github.com/maerkl24/hockeygameclock/actions/workflows/docs.yml/badge.svg)](https://github.com/maerkl24/hockeygameclock/actions/workflows/docs.yml)
[![UI Generation](https://github.com/maerkl24/hockeygameclock/actions/workflows/generation.yml/badge.svg)](https://github.com/maerkl24/hockeygameclock/actions/workflows/generation.yml)

# Hockey Game Clock

A nice hockey game clock for timekeepers.

## Run the Hockey Game Clock with Python

```shell
python hockeygameclock
```

## TODOs

- [ ] Frontend
  - [ ] Use StackedWidget in MainWindow to change between pages
    - [ ] Finalize UI Clock page
    - [ ] Finalize UI Settings page
  - [ ] Implement page selection (create and connect button functions)
  - [ ] Implement frontend backend connections
- [ ] Backend
  - [ ] Implement ``Settings`` class
  - [ ] Finalize concept for Timer (using current approach or QTimer)
  - [ ] Write tests (100% coverage)
- [ ] Packaging/Executable
