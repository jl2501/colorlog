import logging
import kaleidoscope
from collections import UserDict

def get_default_colormap():
    return(
        {
            'DEBUG'     : {'level_color': kaleidoscope.Color('bright lightcyan on lightblack'),
                           'message_color' : kaleidoscope.Color('bright lightcyan on black')},

            'INFO'      : {'level_color': kaleidoscope.Color('bright black on lightblack'),
                           'message_color': kaleidoscope.Color('bright lightblack on black')},

            'WARNING'   : {'level_color': kaleidoscope.Color('bright black on lightyellow'),
                           'message_color': kaleidoscope.Color('bright lightyellow on black')},

            'ERROR'     : {'level_color': kaleidoscope.Color('bright lightred on lightwhite'),
                           'message_color': kaleidoscope.Color('bright lightred on black')},

            'CRITICAL'  : {'level_color': kaleidoscope.Color('bright lightwhite on lightred'),
                           'message_color': kaleidoscope.Color('bright lightred on black')}
        }
    )


class ColorFormatter(logging.Formatter):
    ''' 
    Description:
        Python Logging facility Formatter subclass that uses the LogColorMapping to create
        a formatted log message with the level in the first color and the rest of the
        message in the second color.

    Notes:
        To extend this, add needed attributes to the LogRecord in format(), but
        reference those attributes in the format string in __init__
    '''
    def __init__(self, colormap=None, fmt=None, datefmt=None, style='%'):
        ''' 
        Input:
            colormap: nested dict with the following structure:
                outer key: string version of logging levels:  
                    (DEBUG, INFO, WARNING, ERROR, CRITICAL)

                inner key: one of "level_color" or "message_color", used to color the
                    level and the message output
                
            fmt, datefmt, style: passed to super().__init__() as is.
        '''
        if fmt is None:
            fmt = ("%(level_color)s%(levelname)s:%(color_reset)s" +
                   "%(message_color)s %(name)s: %(message)s %(color_reset)s")
        super().__init__(fmt=fmt, datefmt=datefmt, style=style)

        if colormap is None:
            self.colormap = get_default_colormap()
        else:
            self.colormap = colormap


    def format(self, record):
        strlevel = logging.getLevelName(record.levelno)
        record.color_reset = kaleidoscope.Color.terminal_reset()
        record.level_color = self.colormap[strlevel]['level_color'].terminal_codes()
        record.message_color = self.colormap[strlevel]['message_color'].terminal_codes()
        s = super().format(record)
        return s

