# Falkon plugin to kill CTRL+S

- Finds QAction that owns the "CTRL+S" key
- Overwrites the QShortcut with ""
- Done.

Quick and easy. *And by "quick" i mean it took me 5 hours, and by "easy" I mean that the docs for the python binding of Falkon did not compile.*

## Requirements

Require **PyFalkon** - make sure it is active, the default `alpine` package has it disabled.

You need to see something like this to make it working:
```
Falkon: Python plugin support initialized
```

## How to install

Take the "killctrls" directory and put it into `~/.config/falkon/plugins/` (or whatever the equivalent in Windows is)

## License

CC-BY-SA, feel free to use it as a base for other hardcoded keybindings

## Motivation

Why does anyone need this plugin? Well, if you use `code-server` or any fancy new HTML5+ application, you may come across applications that allow you to use `CTRL+S` to save your work. Neat, right? Yes, if your browser respects these javascript `bind`s then it works fine. Not so much with Qt. Falkon seems to be a great browser, but there are hardcoded shortcuts (see `src/lib/app/mainmenu.cpp` as of time of writing) 
The **proper** way to solve this would be to have QtWebEngine respect the javascript bind and not forward it to the Qt application - but this is an uphill battle others have fought before, so instead of bashing your head against the wall and monkey-patching source files and keeping those forks up to date, we use the fancy plugin system and just get rid of said issue.
If we really want to be fancy, we could use a toggle-able button to enable/disable this functionality, but since this is running only this application (code-server/vscodium/...) anyways (and I haven't saved a website in forever) I think we can just roll with it.
