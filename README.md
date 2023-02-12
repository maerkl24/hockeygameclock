![Hockey Game Clock Banner](assets/banner.png)

[![Analysis Status](https://github.com/maerkl24/hockeygameclock/actions/workflows/analysis.yml/badge.svg)](https://github.com/maerkl24/hockeygameclock/actions/workflows/analysis.yml)
[![Test](https://github.com/maerkl24/hockeygameclock/actions/workflows/test.yml/badge.svg)](https://github.com/maerkl24/hockeygameclock/actions/workflows/test.yml)
[![Documentation Status](https://github.com/maerkl24/hockeygameclock/actions/workflows/documentation.yml/badge.svg)](https://github.com/maerkl24/hockeygameclock/actions/workflows/documentation.yml)
[![Generation Status](https://github.com/maerkl24/hockeygameclock/actions/workflows/generation.yml/badge.svg)](https://github.com/maerkl24/hockeygameclock/actions/workflows/generation.yml)

# Hockey Game Clock

A nice hockey game clock for timekeepers.

## Getting Started

### Setup Environment

To setup the development environment execute the

```bat
:: Setup environment
setup_env.bat
```

### Execute Tools

```bat
:: Execute tools
exec_tools.bat
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
