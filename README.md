# km_metrics
The base metric exporter for Keymeow. 
It's a messy python codebase I hacked together in a few hours (I'll refactor it eventually). 

To export, just run `python3 main.py`.

# writing metrics
Metrics are stored in `metrics/base.py`. 
A few helper functions are defined, and I think you should get a decent idea of how to write your own metrics from the default ones provided. 
If something is confusing, feel free to open an issue or contact me.

# defining keyboards
Keyboards are stored in `keyboards/`.
This is a little bit jankier and the system most in need of change at the moment. 
Keyboards are defined very imperatively. This has the advantage of being very flexible,
and has the disadvantage of being extremely inelegant and unreadable.

The main thing you need to know is that keyboards store 
a dictionary mapping finger to a physical key position. Idiomatically, the order of insertion
should be top-to-bottom, left-to-right physically, as this is how [keymeow](https://github.com/semilin/keymeow)
tries to map layouts onto keyboards. Again, see the default keyboards for examples.
